#!/usr/bin/env python3

from waveshare_epd import epd7in5_v2
from PIL import Image

from urllib.request import urlopen

import sqlite3
import json
import io

import sys
import logging
import random

class source:
    def __init__(self):
        pass

    def load_image(self, url):

        try:
            fh = urlopen(url)
            im = Image.open(fh)
        except Exception as e:
            logging.error(e)
            return None

    def get_image(self, url):
        raise Exception("Not implemented")

class wunderkammer_source(source):

    def __init__(self):
        pass

    def get_image(self, url):

        try:

            conn = sqlite3.connect(url)
            cursor = conn.cursor()

            cursor.execute("SELECT body FROM oembed ORDER BY RANDOM() LIMIT 1")
            row = cursor.fetchone()

            oembed_data = json.loads(row[0])
            data_url = oembed_data["data_url"]

            rsp = urlopen(data_url)
            return Image.open(rsp)
        
        except Exception as e:
            logging.error(e)
            return None
        
def render_image(epd, im):

    im_w, im_h = im.size

    epd_w = epd.width
    epd_h = epd.height

    h_ratio = epd_w / im_w
    v_ratio = epd_h / im_h

    ratio = min(h_ratio, v_ratio)

    new_w = int(im_w * ratio)
    new_h = int(im_h * ratio)

    im = im.resize((new_w, new_h), Image.ANTIALIAS)

    x = float(epd_w - new_w) / 2.0
    y = float(epd_h = new_h) / 2.0

    x = int(x)
    y = int(y)

    epd_im = Image.new("1", (epd_w, epd_h), 0)
    epd_im.paste(im, (x, y))
              
    epd.display(epd.getbuffer(epd_im))
    return True

if __name__ == "__main__":

    epd = epd7in5_V2.EPD()
    epd.init()

    src_uri = sys.argv[1]
    src = wunderkammer_source()

    im = src.get_image(src_uri)

    if not im:
        logging.warning("Failed to retrieve image")
        sys.exit(1)

    render_image(epd, im)
    sys.exit(0)
