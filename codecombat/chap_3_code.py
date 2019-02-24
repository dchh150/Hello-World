
def findBestCoin(coins = None , moveTo = False):
    """
    数组中寻找最合适的金币
    moveTo == False ,返回金币对象；True ,英雄移动去获取金币
    """
    bestCoin = None
    maxRating = 0
    if coins == None:
        coins = hero.findItems()
    # 试着计算"价值/距离"来决定你要收集哪个金币。
    for coin in coins:
        coinRating = coin.value / hero.distanceTo(coin)
        if coinRating > maxRating:
            maxRating = coinRating
            bestCoin = coin
    if bestCoin == None:
        bestCoin = hero.findNearestItem()
    if moveTo and bestCoin:
        hero.moveXY(bestCoin.pos.x , bestCoin.pos.y)
    else:
        return bestCoin


def attack(enemy = None , bashEnemy = True , cleaveEnemy = True):
    if enemy == None:
        enemy = hero.findNearestEnemy()
    if enemy:
        if hero.isReady("bash") and bashEnemy:
            hero.bash(enemy)
        elif hero.isReady("cleave") and cleaveEnemy and hero.distanceTo(enemy) <= 10:
            hero.cleave(enemy)
        else:
            hero.attack(enemy)


