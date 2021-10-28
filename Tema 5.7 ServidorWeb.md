# Servidor Web



## Servidor usando python/flask

Seguiremos el siguiente [proyecto/tutorial](https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/3) y los pasos de este otro [Control de gpio desde la web](https://randomnerdtutorials.com/raspberry-pi-web-server-using-flask-to-control-gpios/)

```python
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      GPIO.output(changePin, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0

```

[Tutorial mas complejo](https://randomnerdtutorials.com/raspberry-pi-publishing-mqtt-messages-to-esp8266/)

## Servidor web con wordpress

[Proyecto/tutorial](https://projects.raspberrypi.org/en/projects/lamp-web-server-with-wordpress)

