#import xlrd
#import openpyxl
#import csv

filename1 = r"D:\MyDocuments\Desktop\pythontest\REPORT_站点新增_工单详情_.xlsx"
filename2 = r"D:\MyDocuments\Desktop\pythontest\REPORT_站点新增_工单详情_.csv"
filename3 = r"D:\MyDocuments\Desktop\pythontest\单优统计规则设定.xlsx"
#data = xlrd.open_workbook(filename1)
#wb = openpyxl.load_workbook(filename=filename1, read_only=True)

'''
with open(filename2) as fl:
    csv_fl = csv.reader(fl)
    for i,cow in enumerate(csv_fl):
        if i >3:
            break
        print(cow)
'''


import pandas as pd
df_工单当前状态 = pd.read_excel(filename3,sheet_name = "工单当前状态")
file = df_工单当前状态[df_工单当前状态["是否具备单优条件（已单验）"].isin(["是","单一条件无法判断"])]
df_所属规划期 = pd.read_excel(filename3,sheet_name = "所属规划期")

print(file)

