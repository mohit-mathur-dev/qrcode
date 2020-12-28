# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 09:38:50 2020

@author: Mohit Mathur
"""

import pyqrcode
import png

def qrcode():
    q=pyqrcode.create(input())
    q.png('qrcode.png', scale=6)
    print("QR Generated")
    
if __name__=='__main__' :
    qrcode()