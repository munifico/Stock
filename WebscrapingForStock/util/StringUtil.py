'''
Created on 2019. 7. 5.

@author: SIDeok
'''

#문자열 좌측 padding
def lpad(str, len, chr) : 
    return str.rjust(len, chr);

#문자열 좌측 padding
def rpad(str, len, chr) : 
    return str.ljust(len, chr);