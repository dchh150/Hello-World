from d工作表分别复制 import d_copysheets

def main():
    d_copysheets('a.xlsx',['Sheet1'],'b.xlsx',['Sheet1'])

if __name__ == '__main__':
    if input("输入ok开始复制，输入其他退出：")=="ok":
        main()
        