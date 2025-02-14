
def summonAttack():
    # 如果钱够了就招募士兵。
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")

    enemy = hero.findNearest(hero.findEnemies())
    if enemy:
        
        # 遍历你所有的士兵，命令他们攻击。
        soldiers = hero.findFriends()
        for soldier in soldiers:
            if soldier:
                hero.command(soldier, "attack", enemy)    # 使用 attack 命令让你的士兵们攻击。


def findBestCoin(coins = None , moveTo = False , people = hero):
    """
    数组中寻找最合适的金币
    moveTo == False ,返回金币对象；True ,英雄移动去获取金币
    """
    bestCoin = None
    maxRating = 0
    if coins == None:
        coins = people.findItems()
    # 试着计算"价值/距离"来决定你要收集哪个金币。
    for coin in coins:
        coinRating = coin.value / people.distanceTo(coin)
        if coinRating > maxRating:
            maxRating = coinRating
            bestCoin = coin
    if bestCoin == None:
        bestCoin = people.findNearestItem()
    if moveTo and bestCoin:
        people.moveXY(bestCoin.pos.x , bestCoin.pos.y)
    else:
        return bestCoin


def summonDiff(summonTypes = ["soldier","soldier","archer"]):
    #按summonTypes 序列召唤
    summontype = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(summontype):
        hero.summon(summontype)


def commandDefend(defendPoints):
    #分配士兵到defendPoints的点中守备
    soldiers = hero.findByType("soldier")
    archers = hero.findByType("archer")
    for i in range( len(soldiers) ):
        friend = soldiers[i]
        point = defendPoints[i % len(defendPoints)]
        hero.command(friend,"defend",point)
    for i in range( len(archers) ):
        friend = archers[i]
        point = defendPoints[i % len(defendPoints)]
        hero.command(friend,"defend",point)


def chooseTarget(friend):
# 根据士兵类型决定要攻击什么
    targetList=["witch","warlock","tower","catapult","fangrider"]
    fristtargets = None
    for t in targetList:
        if len(hero.findByType(t)) >0:
            fristtargets = hero.findByType(t)
            break
    if friend.type in ["soldier","paladin"] and fristtargets:
        return friend.findNearest(fristtargets)
    else:
        return friend.findNearest(friend.findEnemies())


def lowestHealthPaladin(onlyPaladin = False):
# 找到生命值最低的武士
    lowestHealth = 99999
    lowestFriend = None
    friends = hero.findFriends()
    for friend in friends:
        if onlyPaladin and friend.type != "paladin":
            continue
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend
    return lowestFriend


def commandPaladin(paladin):
    # 使用函数 lowestHealthPaladin() 找到生命值最低的武士，并治疗
    # 你能使用 paladin.canCast("heal") 和 command(paladin, "cast", "heal", target)
    # 武士也能防御：command(paladin, "shield")
    # 不要忘了他们还能攻击
    lowest = lowestHealthPaladin()
    if lowest and paladin.canCast("heal"):
        hero.command(paladin, "cast", "heal",lowest)
    elif paladin.health < paladin.maxHealth*1/2:
        hero.command(paladin, "shield")
    else:
        enemy = paladin.findNearestEnemy()
        if enemy:
            hero.command(paladin, "attack", enemy)

