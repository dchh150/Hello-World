from d工作表分别复制 import d_copysheets
import datetime
'''
读取很慢，待定
将单优和挂起清单黏贴到统计中
    过程管控周报统计-20180711-有fdd.xlsx-本周开网优化清单,本周挂起清单
    每日质量通报统计20180711-新版本-无fdd.xlsx-开网优化工单,挂起工单
    ftp/开网优化_挂起工单_20180711-无FDD.xlsx-Sheet1
    ftp/REPORT_开网优化_工单详情_20180711.xlsx-Sheet1
'''
def main():
    today_ti = datetime.datetime.now()
    today = today_ti.strftime("%Y%m%d") # 例：'20180625'
    jindu_path='E:/2017工作-ET/开网优化/进度统计/每周进度/{}/'.format(today)   #20180711/ftp/
    d_copysheets(
        jindu_path+'ftp/开网优化_挂起工单_{}.xlsx'.format(today),
        ['Sheet1'],
        jindu_path+'过程管控周报统计-{}-有fdd.xlsx'.format(today),
        ['本周挂起清单']
        )
    d_copysheets(
        jindu_path+'ftp/开网优化_挂起工单_{}-无FDD.xlsx'.format(today),
        ['Sheet1'],
        jindu_path+'每日质量通报统计{}-新版本-无fdd.xlsx'.format(today),
        ['挂起工单']
        )
    d_copysheets(
        jindu_path+'ftp/REPORT_开网优化_工单详情_{}-无FDD.xlsx'.format(today),
        ['Sheet1'],
        jindu_path+'每日质量通报统计{}-新版本-无fdd.xlsx'.format(today),
        ['开网优化工单'],
        17
        )
    d_copysheets(
        jindu_path+'ftp/REPORT_开网优化_工单详情_{}.xlsx'.format(today),
        ['Sheet1'],
        jindu_path+'过程管控周报统计-{}-有fdd.xlsx'.format(today),
        ['本周开网优化清单'],
        18
        )
    


if __name__ == '__main__':
    if input("输入ok开始复制，输入其他退出：")=="ok":
        main()
        