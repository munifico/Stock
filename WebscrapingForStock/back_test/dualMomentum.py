'''
Created on 2019. 7. 5.

@author: SIDeok
'''
from cmath import sqrt
from turtledemo.penrose import star

from pandas._libs.index import datetime;
from pandas.plotting import register_matplotlib_converters;

from StringUtil import lpad, rpad;
import matplotlib.pyplot as plt; 
from ms_access.connectDB import StockDB;

from pandas import Series, DataFrame; #pandas 라이브러리

# db 커넥션 설정
DB = StockDB()
cs = DB.getCursor()

#주가지수 조회
cs.execute("select BASE_DT, KOSPI_INDEX from TB_KOSPI_INDEX WHERE BASE_DT > DateSerial(2009,07,06) ORDER BY BASE_DT")
rows = cs.fetchall() 

arrIndexVal = [];
arrDateVal = [];
for info in rows :
    arrIndexVal.append(info[1]);
    arrDateVal.append(info[0].date());
#     arrDateVal.append(str(info[0].year) + '-' + lpad(str(info[0].month),2,'0') + '-' + lpad(str(info[0].day),2,'0'));
#     dictIndex.__setitem__(str(info[0].year) + str(info[0].month) + str(info[0].day), info[1])

serIndex = Series(arrIndexVal, arrDateVal);

#3개월 절대모멘텀
adjustValue = [];
adjustDate = [];
max = arrIndexVal[90];
min = arrIndexVal[90];
mdd = 0;
adjustValue.append(arrIndexVal[90]);
adjustDate.append(arrDateVal[90]);
for i in range(91,arrIndexVal.__len__() - 1) : 
    adjustDate.append(arrDateVal[i]);
    if arrIndexVal[i - 90] > arrIndexVal[i] :
        adjustValue.append(adjustValue[i-91]);
    else :
        adjustValue.append(adjustValue[i-91] + (arrIndexVal[i] - arrIndexVal[i-1]))
    if adjustValue[i-90] > max :
        max = adjustValue[i-90]
    else :
        min = adjustValue[i-90]
        if mdd < (1 - (min/max)) * 100 :
            mdd = (1 - (min/max)) * 100

# 6개월 절대모멘텀
# adjustValue = [];
# adjustDate = [];
# max = arrIndexVal[180];
# min = arrIndexVal[180];
# mdd = 0;
# adjustValue.append(arrIndexVal[180]);
# adjustDate.append(arrDateVal[180]);
# for i in range(181,arrIndexVal.__len__() - 1) : 
#     adjustDate.append(arrDateVal[i]);
#     if arrIndexVal[i - 180] > arrIndexVal[i] :
#         adjustValue.append(adjustValue[i-181]);
#     else :
#         adjustValue.append(adjustValue[i-181] + (arrIndexVal[i] - arrIndexVal[i-1]))
#     if adjustValue[i-180] > max :
#         max = adjustValue[i-180]
#     else :
#         min = adjustValue[i-180]
#         if mdd < (1 - (min/max)) * 100 :
#             mdd = (1 - (min/max)) * 100

# 9개월 절대모멘텀
# adjustValue = [];
# adjustDate = [];
# max = arrIndexVal[270];
# min = arrIndexVal[270];
# mdd = 0;
# adjustValue.append(arrIndexVal[270]);
# adjustDate.append(arrDateVal[270]);
# for i in range(271,arrIndexVal.__len__() - 1) : 
#     adjustDate.append(arrDateVal[i]);
#     if arrIndexVal[i - 270] > arrIndexVal[i] :
#         adjustValue.append(adjustValue[i-271]);
#     else :
#         adjustValue.append(adjustValue[i-271] + (arrIndexVal[i] - arrIndexVal[i-1]))
#     if adjustValue[i-270] > max :
#         max = adjustValue[i-270]
#     else :
#         min = adjustValue[i-270]
#         if mdd < (1 - (min/max)) * 100 :
#             mdd = (1 - (min/max)) * 100

#1년 절대모멘텀
# adjustValue = [];
# adjustDate = [];
# max = arrIndexVal[360];
# min = arrIndexVal[360];
# mdd = 0;
# adjustValue.append(arrIndexVal[360]);
# adjustDate.append(arrDateVal[360]);
# for i in range(361,arrIndexVal.__len__() - 1) : 
#     adjustDate.append(arrDateVal[i]);
#     if arrIndexVal[i - 360] > arrIndexVal[i] :
#         adjustValue.append(adjustValue[i-361]);
#     else :
#         adjustValue.append(adjustValue[i-361] + (arrIndexVal[i] - arrIndexVal[i-1]))
#     if adjustValue[i-360] > max :
#         max = adjustValue[i-360]
#     else :
#         min = adjustValue[i-360]
#         if mdd < (1 - (min/max)) * 100 :
#             mdd = (1 - (min/max)) * 100
         
    


# 그래프 그리기
serAdjust = Series(adjustValue, adjustDate);

register_matplotlib_converters();

plt.plot(serIndex.index, serIndex.values,'r', label="kospi");
plt.plot(serAdjust.index, serAdjust.values,'b', label="M/M");
plt.legend(loc='upper left');
plt.xlabel("mdd: "  + str(round(mdd, 2)) + ", startVal: " + str(adjustValue[0]) + ", endVal: " + str(round(adjustValue[adjustValue.__len__()-1], 2)));
plt.ylabel(adjustDate[0].__str__() + " ~ "  + adjustDate[adjustDate.__len__()-1].__str__() + ", rate: " + str(round(adjustValue[adjustValue.__len__()-1]/adjustValue[0], 2)**(1/((adjustDate[adjustDate.__len__()-1] - adjustDate[0]).days/365))));

plt.show();

# for i in serIndex.values :
#     print(i);
# for i in serIndex.index :
#     print(i);