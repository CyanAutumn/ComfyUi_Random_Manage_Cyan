import re

class Base(object):
    buf_text:str

    def __init__(self,tag):
        self.buf_text=tag
    
    def __str__(self):
        return self.buf_text