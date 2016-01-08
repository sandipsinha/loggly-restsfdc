__author__ = 'ssinha'
class SFDCRestExceptions(Exception):
    messages = None
    code = None
    def __init__(self, exc = {'messages':None, 'code': None}):
        self.messages = exc['messages']
        self.code = exc['code']


    def __str__(self):
        return self.msg, self.code

