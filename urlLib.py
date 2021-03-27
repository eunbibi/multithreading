# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 15:19:39 2021
@author: anna_eunbi
"""

# gotta install first: pip install 

import urllib.request
urllib.request.urlopen
                                    #put the address that you wanna open and read
request_url = urllib.request.urlopen('https://centennialcollege.zoom.us//')

#read the url html
print(request_url.read())

