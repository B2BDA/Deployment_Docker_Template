# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:08:53 2020

@author: bishw
"""

from pydantic import BaseModel

class Sample(BaseModel):
    name: str
    age: float