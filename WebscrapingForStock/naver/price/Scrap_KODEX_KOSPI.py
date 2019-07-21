import urllib.request
from bs4 import BeautifulSoup
import pyodbc
from ms_access.connectDB import StockDB
#주식정보 페이지 숫자만큼 range를 정해준다.
# conn = pyodbc.connect(Driver='{Microsoft Access Driver (*.mdb, *.accdb)}'
# #                      ,DBQ='C:\\Users\\SIDeok\\git\\WebscrapingForStock\\WebscrapingForStock\\ms_access\\StockDB.mdb')
#                       ,DBQ='C:\\Users\\SIDeok\\git\\WebscrapingForStock\\WebScrapingForStock\\ms_access\\StockDB.mdb')
# cs = conn.cursor()
conn = StockDB()
cs = conn.getCursor()

for i in range(1,3) :
    pageCont = urllib.request.urlopen('https://finance.naver.com/item/sise_day.nhn?code=226490&page=' + str(i));
    soup_m = BeautifulSoup(pageCont.read(), "html.parser");
    soup_tab = soup_m.find("table", {"class" : "type2"});
    
    #tr태그를 읽어온뒤 date가 있는 항목만 처리한다.
    tdArray = soup_tab.findAll("span");
    idx = 0;
    for j in tdArray : 
        if(j.contents.__len__() != 0 and j['class'][1] == 'p10') :
            date = j.contents[0];
            val = tdArray[idx+1].contents[0];
            print(str(i) + ", " + date.replace(".","") + " ,  " + val);
            cs.execute("INSERT INTO TB_KODEX_KOSPI VALUES('" + date.replace(".","-") + "'," + val.replace(",","") + ")")
        idx+=1;
        

cs.commit()
cs.close()

print("complete!!!")