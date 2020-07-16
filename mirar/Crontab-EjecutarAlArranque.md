
https://www.raspberrypi.org/blog/how-to-run-a-script-at-start-up-on-a-raspberry-pi-using-crontab/



4. Run on boot
To make the service restart automatically on boot, edit the `/etc/rc.local` file
$ sudo vim /etc/rc.local
Just add the following to the end of the file just before exit 0:
...
pm2 start /path/to/backend/repo/bin/www
/etc/init.d/nginx start
exit 0