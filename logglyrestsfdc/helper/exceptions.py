__author__ = 'ssinha'
class SFDCRestExceptions(Exception):
    def __init__(self, exc):
        self.msg = exc['messages']
        self.code = exc['code']


    def __str__(self):
        return self.msg, self.code

