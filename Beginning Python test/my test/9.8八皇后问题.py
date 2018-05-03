def conflict(state,nextX):
    nextY=len(state)
    for y in range(nextY):
        if abs(state[y]-nextX) in (0,nextY-y):
            return True
    return False

def queens(num=8,state=()):
    if len(state)==num-1:
        #若到只是最后一行位置未知，生成最后一行没有冲突的位置
        for pos in range(num):
            if not conflict(state,pos):
                yield (pos,)
    else:
        #不只是最后一行位置未知
        for pos in range(num):
            if not conflict(state,pos):
                #找出还未知的第一行中没有冲突的位置
                for each_hight_result in queens(num,state+(pos,)):
                    #将上一句找出的位置元组递归，迭代剩下行合适的元组
                    yield (pos,)+each_hight_result
                    #生成 本行找出的合适位置 和剩下几行合适位置的元组
                    

if __name__=="__main__":
    print(list(queens(4,(1,3,0))))
    print(len(list(queens())))
    
    
