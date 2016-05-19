#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import codecs
import re
import requests as r
import urllib
import os
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import Tag
from subprocess import call

usock = urllib.urlopen("https://www.packtpub.com/packt/offers/free-learning")
soup = BeautifulSoup(usock.read())        

title = 'Book of the day: '

for div in [x for x in soup.findAll('div') if type(x) is Tag]:
    attrs = dict(div.attrs)
    if 'class' in attrs and attrs['class'] == 'dotd-title':
        title += div.text
        break


os.system("echo 'message:" + title + "' | zenity --notification --listen")
