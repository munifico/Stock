'''
Created on 2018. 8. 22.

@author: SIDeok
'''
import pyodbc;

class StockDB :
    def __init__(self) :
        self.conn = pyodbc.connect(Driver='{Microsoft Access Driver (*.mdb, *.accdb)}',DBQ='D:\주식 백테스트\workspace\WebscrapingForStock\ms_access\StockDB.mdb')
        
    def getCursor(self) :
        try :
            return self.conn.cursor()
        except AttributeError :
            self.conn = pyodbc.connect(Driver='{Microsoft Access Driver (*.mdb, *.accdb)}',DBQ='D:\주식 백테스트\workspace\WebscrapingForStock\ms_access\StockDB.mdb')
            return self.conn.cursor()
    
    def setRelease(self) :
        self.conn.cursor().close();
        
    def setCommit(self) : 
        self.conn.cursor().commit();
        
    def setRollback(self) : 
        self.conn.cursor().rollback();
