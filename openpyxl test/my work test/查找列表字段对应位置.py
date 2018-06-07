def findwhere(fromlists,findlists,splitchar='\t'):
    from_list=fromlists.split(splitchar)
    find_list=findlists.split(splitchar)
    resule=[]
    for xfind in find_list:
        for i,xfrom in enumerate(from_list):
            if xfrom==xfind:
                resule.append(i+1)
                break
        else:
            resule.append(r'N/A')
    return print('查找字段在原表头的位置为:\n',resule)

def main():
    fromlists=input('请输入原表头字段：\n')
    findlists=input('请输入需要查找的字段：\n')
    if input('是否需要额外指定分隔符？（默认为tab制表符，额外指定请输入"y"）:')=="y":
        splitchar=input('请输入字段分隔符：')
    else:
        splitchar='\t'
    print('当前分隔符为："'+splitchar+'"。')
    findwhere(fromlists,findlists,splitchar)
    print('====='*10)
    return

if __name__ == '__main__':
    while input("输入exit退出，输入其他继续：")!="exit":
        main()

