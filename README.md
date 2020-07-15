# py-wunderkammer-waveshare

Python tools for working with "wunderkammer" databases and Waveshare e-ink display.

## Scripts

### wunderkammer.py

```
$> python3 ./scripts/wunderkammer.py {PATH_TO_WUNDERKAMMER_DATABASE}
```

#### Notes

This package does not contain a `setup.py` script or `requirements.txt` file yet. It assumes a few things:

1. That you have installed the [Waveshare e-Paper Python libraries](https://github.com/waveshare/e-Paper/tree/master/RaspberryPi%26JetsonNano/python) and that the `wunderkammer.py` script knows where they are.
2. That you are using a [7x5 inch e-Paper HAT](https://github.com/waveshare/e-Paper/blob/master/RaspberryPi%26JetsonNano/python/lib/waveshare_epd/epd7in5bc_V2.py).
3. That the [Python Imaging Library](https://en.wikipedia.org/wiki/Python_Imaging_Library) is installed.

It also expects to be working with a "wunderkammer" style SQLite database as produced by the [wunderkammer-db](https://github.com/aaronland/go-wunderkammer#wunderkammer-db) tool (or equivalent) which is part of the [go-wunderkammer](https://github.com/aaronland/go-wunderkammer) package.

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
* https://www.waveshare.com/wiki/7.5inch_e-Paper_HAT
* https://github.com/waveshare/e-Paper