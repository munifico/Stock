'''
Created on 2019. 7. 5.

@author: SIDeok
'''

#쿼리파일 불러오기
def getQuery(path) : 
    file = open(path, "r")
    qr = file.read();
    return qr;
