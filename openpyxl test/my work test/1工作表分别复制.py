'''用python实现excel(.xlsx)按工作表分别复制到另一份.xlsx中'''
from openpyxl import load_workbook
from openpyxl import Workbook

def d_copysheets(loadfl,loadsheets,savefl,savesheets):
    """loadsheets,savesheets为sheet名的列表"""
    assert len(loadsheets)==len(savesheets)
    try:
        wb1=load_workbook(filename=loadfl)
        wb2=load_workbook(filename=savefl)
        for i,sheet in enumerate(loadsheets):
            ws1=wb1[sheet]
            ws2=wb2[savesheets[i]]
            for i,row in enumerate(ws2.iter_rows()):
                for j,cell in enumerate(row):
                    ws2.cell(row=i+1, column=j+1, value=None)
            for i,row in enumerate(ws1.iter_rows()):
                for j,cell in enumerate(row):
                    ws2.cell(row=i+1, column=j+1, value=cell.value)
    except FileNotFoundError as err:
        return print('文件名错误:',err)
    except KeyError as err:
        return print('工作表Sheet名错误:',err)
    else:
        wb2.save(savefl)
        wb2.close()
        wb1.close()
        return print('已将',loadfl,loadsheets,'复制到',savefl,savesheets)

def main():
    loadfl=input('输入源文件（.xlsx）：')
    loadsheets=input('输入源工作表列表(如："Sheet1,Sheet2")：').split(',')
    savefl=input('输入保存文件（.xlsx）：')
    savesheets=input('输入保存的工作表列表(如："Sheet1,Sheet2")：').split(',')
    if input('确认输入"ok"回车后，开始操作：')=='ok':
        d_copysheets(loadfl,loadsheets,savefl,savesheets)
    input('按任意键退出:')
    return

if __name__ == '__main__':
    main()
