#将站点新增csv导入数据库中。

import sqlite3
import csv

sql_file = r"D:\MyDocuments\Desktop\pythontest\站点新增_工单数据库.sqlite3"
csv_file = r"D:\MyDocuments\Desktop\pythontest\REPORT_站点新增_工单详情_.csv"

def createDB(csv_file,sql_file,table_name = "站点新增_工单详情", begin_cow =1,encoding="GB18030"):
    #创建数据表并导入csv;begin_cow- 正式数据开始行
    assert '"' not in table_name ,"""table_name 参数字符串中不能包含双引号(")"""
    with open(csv_file,mode='r', encoding= encoding, newline="") as csvfl:
        csv_rd = csv.DictReader(csvfl)
        col_names = []
        for n in csv_rd.fieldnames:
            if '"' in n:
                n = n.replace('"',"'")    #把表头带双引号的替换为单引号
            if n in col_names:
                n += ("_"+str(col_names.count(n)+1) )    #把重复的表头加后缀
            col_names.append(n)
        sqlm = '''CREATE TABLE IF NOT EXISTS "%s" ("%s") ;''' % (table_name, '" TEXT, "'.join(col_names) )
        con = sqlite3.connect(sql_file)
        cur = con.cursor()
        with con:
            cur.execute('''DROP TABLE IF EXISTS "%s" ;''' % table_name )
            cur.execute(sqlm)  #完成创建表table_name

        csvfl.seek(0)    #文件指针到开头
        reader = csv.reader(csvfl)
        for i in range(begin_cow):
            next(reader)
        stmt = '''INSERT INTO "%s" VALUES (%s) ;''' % (table_name,','.join('?' * len(col_names)) )
        with con:
            cur.executemany(stmt, reader)
        con.close()

        return print("数据导入完成：\n  源csv："+csv_file+"\n  目标db："+sql_file+"\n    表名："+table_name)



if __name__ == "__main__":
    createDB(csv_file,sql_file)


