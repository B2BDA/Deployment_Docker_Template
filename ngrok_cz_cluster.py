# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:04:49 2020

@author: bishw
"""

from pyngrok import ngrok
ngrok.kill()
public_url = ngrok.connect(8501)
print(public_url)