# py-wunderkammer-waveshare

## Scripts

### wunderkammer.py

```
$> python3 ./scripts/wunderkammer.py {PATH_TO_WUNDERKAMMER_DATABASE}
```

## Running stuff on startup

### systemd

Running stuff automatically on startup:

`sudo {SOME TEXT EDITOR} /lib/systemd/system/wunderkammer.service` and then:

```
[Unit]
Description=Show images from a wunderkammer database
After=multi-user.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/py-wunderkammer-waveshare/script/wunderkammer.py

[Install]
WantedBy=multi-user.target
```

Then:

```
sudo systemctl daemon-reload
sudo systemctl enable blink.service
sudo reboot
```

#### Running stuff on timers

`sudo {SOME TEXT EDITOR} /lib/systemd/system/wunderkammer.timer` and then:

```
[Unit]
Description=Run wunderkammer
Requires=wunderkammer.service

[Timer]
Unit=blink.service
OnCalendar=*-*-* *:0:0

[Install]
WantedBy=wunderkammer.service
```

#### Useful links

* https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup/all
* https://www.freedesktop.org/software/systemd/man/systemd.timer.html
* https://www.freedesktop.org/software/systemd/man/systemd.time.html

## See also

* https://github.com/aaronland/go-wunderkammer
* https://github.com/aaronland/ios-wunderkammer