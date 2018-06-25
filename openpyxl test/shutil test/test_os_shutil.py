import os
import shutil
import time

a = os.getcwd()
print('结果', a)
sfile = 'e:/教程/python/练习/Hello-World/openpyxl test/shutil test/a/a.xlsx'
dfile = 'e:/教程/python/练习/Hello-World/openpyxl test/shutil test/c' + \
    time.strftime("%Y%m%d")
try:
    os.mkdir(dfile)
except:
    pass
try:
    b = shutil.copy(sfile, dfile)
    print("完成", sfile, "到", dfile)
except FileNotFoundError as err:
    print('有错误:', err)
