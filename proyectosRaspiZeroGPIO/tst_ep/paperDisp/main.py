#!/usr/bin/python
import spidev as SPI                # where the display connects
import Image, ImageDraw, ImageFont  # PIL - PythonImageLibrary
import time, datetime, sys, signal, urllib, requests, random
from StringIO import StringIO

from EPD_driver import EPD_driver

def handler(signum, frame):
    print( 'SIGTERM')
    sys.exit(0)
signal.signal(signal.SIGTERM, handler)
random.seed(time.time())

bus = 0 
device = 0
disp = EPD_driver(spi = SPI.SpiDev(bus, device))
print( "disp size : %dx%d"%(disp.xDot, disp.yDot))

print( '------------init and Clear full screen------------')
disp.Dis_Clear_full()
disp.delay()

# display part
disp.EPD_init_Part()
disp.delay()

imagenames = [] # array of tuples ('http://imagelink','description')

searchnames = ['Cat', 'Horst', 'Amiga', 'DAC', 'Raspberry', 'diy', 'Acorn', 'Boing']

# this writes a bunch of image links ad test descriptions to imagenames
def querySearchEngine(val):
    search = "http://api.duckduckgo.com/?q="+val+"&format=json&pretty=1"
    req = requests.get(search)
    if req.status_code == 200:
        del imagenames[:]
        for topic in req.json()["RelatedTopics"]:
            if "Topics" in topic:
                for topic2 in topic["Topics"]:
                    try:
                        url = topic2["Icon"]["URL"]
                        text = topic2["Text"]
                        if url:
                            imagenames.append( (url,text) )
                    except:
                        # print topic
                        pass
            try:
                url = topic["Icon"]["URL"]
                text = topic["Text"]
                if url:
                    imagenames.append( (url,text) )
            except:
                # print topic
                pass
    else:
        print (req.status_code)
   # print( 'search for', val, ' #entries', len(imagenames) #, imagenames)

# function to write the image to the display

def imageToDisplay(img):
    # prepare for display
    im = mainimg.transpose(Image.ROTATE_90)
    listim = list(im.getdata())
    # print im.format, im.size, im.mode, len(listim)
    # convert to list / bitmap
    listim2 = []
    for y in range(0, im.size[1]):
        for x in range(0, im.size[0]/8):
            val = 0
            for x8 in range(0, 8):
                if listim[(im.size[1]-y-1)*im.size[0] + x*8 + (7-x8)] > 128:
                    # print x,y,x8,'ON'
                    val = val | 0x01 << x8
                else:
                    # print x,y,x8,'OFF'
                    pass
            # print val
            listim2.append(val)
    for x in range(0,1000):
        listim2.append(0)
    # print len(listim2)
    ypos = 0
    xpos = 0
    disp.EPD_Dis_Part(xpos, xpos+im.size[0]-1, ypos, ypos+im.size[1]-1, listim2) # xStart, xEnd, yStart, yEnd, DisBuffer
    uploadtime = time.time()

# font for drawing within PIL
myfont10 = ImageFont.truetype("amiga_forever/amiga4ever.ttf", 8)
myfont28 = ImageFont.truetype("amiga_forever/amiga4ever.ttf", 28)

# mainimg is used as screen buffer, all image composing/drawing is done in PIL,
# the mainimg is then copied to the display (drawing on the disp itself is no fun)
mainimg = Image.new("1", (296,128))
draw = ImageDraw.Draw(mainimg)

skip = 0 # used to slow down image changes, but not clock changes
while 1:
    starttime = time.time()
    if skip == 0:
        querySearchEngine(searchnames[random.randint(0,len(searchnames)-1)])
        imagename = imagenames[random.randint(0,len(imagenames)-1)]
        # print '---------------------'
        try:
            req = requests.get(imagename[0], stream=True)
            req.raw.decode_content = True
            im = Image.open(StringIO(req.content))
            # print name, im.format, im.size, im.mode
            im.thumbnail((296,128))
            im = im.convert("1") #, dither=Image.NONE)
            # print 'thumbnail', im.format, im.size, im.mode
            loadtime = time.time()
            # print 't:load+resize:', (loadtime - starttime)

            # clear
            draw.rectangle([0,0,296,128], fill=255)

            # copy to mainimg
            ypos = (disp.xDot - im.size[1])/2
            xpos = (disp.yDot - im.size[0])/2
            # print 'ypos:', ypos, 'xpos:', xpos
            mainimg.paste(im, (xpos,ypos))

            # draw info text
            ts = draw.textsize(imagename[1], font=myfont10)
            tsy = ts[1]+1
            oldy = -1
            divs = ts[0]/250
            for y in range(0, divs):
                newtext = imagename[1][(oldy+1)*len(imagename[1])/divs:(y+1)*len(imagename[1])/divs]
                # print divs, oldy, y, newtext
                oldy = y
                draw.text((1, 1+y*tsy), newtext, fill=255, font=myfont10)
                draw.text((1, 3+y*tsy), newtext, fill=255, font=myfont10)
                draw.text((3, 3+y*tsy), newtext, fill=255, font=myfont10)
                draw.text((3, 1+y*tsy), newtext, fill=255, font=myfont10)
                draw.text((2, 2+y*tsy), newtext, fill=0, font=myfont10)

        except IOError as ex:
            print( 'IOError', str(ex), imagename[0])
            pass

    #draw time
    now = datetime.datetime.now()
    tstr = "%02d:%02d:%02d"%(now.hour,now.minute,now.second)
    # draw a shadow, time
    tpx = 36
    tpy = 96
    for i in range(tpy-4, tpy+32, 2):
        draw.line([0, i, 295, i], fill=255)
    draw.text((tpx-1, tpy  ), tstr, fill=0, font=myfont28)
    draw.text((tpx-1, tpy-1), tstr, fill=0, font=myfont28)
    draw.text((tpx  , tpy-1), tstr, fill=0, font=myfont28)
    draw.text((tpx+2, tpy  ), tstr, fill=0, font=myfont28)
    draw.text((tpx+2, tpy+2), tstr, fill=0, font=myfont28)
    draw.text((tpx  , tpy+2), tstr, fill=0, font=myfont28)
    draw.text((tpx  , tpy  ), tstr, fill=255, font=myfont28)
    drawtime = time.time()
    # print 't:draw:', (drawtime - loadtime)

    convtime = time.time()
    # print 't:conv:', (convtime - loadtime)

    # disp.delay()

    imageToDisplay(mainimg)
    skip = (skip+1)%17

    # print 't:upload:', (uploadtime - loadtime)


