# You can find friends through walls, but not enemies.
# Watch out for smooth, frictionless ice patches!

def lowestHealthPaladin(friends = hero.findFriends(),onlyPaladin = True):
# 找到生命值最低的武士
    lowestHealth = 99999
    lowestFriend = None
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
    elif paladin.health < paladin.maxHealth*1/3:
        hero.command(paladin, "shield")
    else:
        enemy = chooseTarget(paladin)
        if enemy:
            hero.command(paladin, "attack", enemy)
            
            

def chooseTarget(friend):
# 根据士兵类型决定要攻击什么
    targetList=["witch"]
    sList = ["archer","paladin"] # "archer","knight"
    fristtargets = None
    for t in targetList:
        if len(hero.findByType(t)) >0:
            fristtargets = hero.findByType(t)
            break
    if friend.type in sList and fristtargets:
        return friend.findNearest(fristtargets)
    else:
        return friend.findNearest(friend.findEnemies())
        
        
def commandFriends():
    friends = hero.findFriends()
    for f in friends:
        if f.type == "paladin":
            commandPaladin(f)
        else:
            enemy = chooseTarget(f)
            if enemy and hero.isPathClear(f.pos, enemy.pos):
                hero.command(f, "attack", enemy)
            

def summonDiff(summonTypes = ["griffin-rider","soldier","archer"]):
    #按summonTypes 序列召唤
    summontype = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(summontype):
        hero.summon(summontype) 
                

def attack(enemy = None , bashEnemy = True , cleaveEnemy = True):
    if enemy == None:
        enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy)<20 and hero.isPathClear(hero.pos, enemy.pos):
        if hero.isReady("bash") and bashEnemy:
            hero.bash(enemy)
        elif hero.isReady("cleave") and cleaveEnemy and hero.distanceTo(enemy) <= 10:
            hero.cleave(enemy)
        elif hero.canCast("chain-lightning", enemy) :
            hero.cast("chain-lightning", enemy)
        else:
            hero.attack(enemy)



while True:
    summonDiff()
    commandFriends()
    flag = hero.findFlag()
    if flag and flag.color is "violet":
        hero.move(flag.pos)
        if hero.distanceTo(flag)<8:
            hero.pickUpFlag(flag)
    elif flag and flag.color is "black":
        friends = hero.findFriends
        for f in friends:
            hero.command(f,"move",flag.pos)
        hero.removeFlag(flag)
    cata = hero.findByType("catapult")
    if len(cata)>0:
        attack(hero.findNearest(cata))
    else:
        attack()
        



# 用药水治疗士兵和用剑武装农民。

# 注意项目和单元队列。
while True:
    item = hero.findNearestItem()
    unit = hero.findNearestFriend()
    if not item or not unit:
        continue
    # 使用“type”属性来区分单位和项目
    # 如果物品是“药剂potion”而单位是“士兵”：
    if item.type == "potion" and unit.type =="soldier":
        # 说单位名称（id）：
        hero.say(unit.id)
    # 如果项目是“剑sword”而单位是“农民”：
    if item.type == "sword" and unit.type =="peasant":
        # 说单位名称（id）：
        hero.say(unit.id)
    # 否则说“下一步”（或其他）。
    hero.say("下一步")
       


# Sort out and deliver items:
# Yak - potion, Yeti - mushroom, Skeleton - lightstone.
yetiPos = {"x": 60, "y": 36}
yakPos = {"x": 40, "y": 52}
skeletonPos = {"x": 58, "y": 56}

peasant = hero.findFriends()[0]
items = peasant.findItems()
for item in items:
    # Command the peasant "pickUpItem" an item:
    hero.command(peasant,"pickUpItem",item)
    pass

while True:
    # Check an item on the top of the stack.
    topItem = peasant.peekItem()
    if not topItem:
        break
    # If topItem type is "potion":
    if topItem.type == "potion":
        # Command to "dropItem" it to yaks:
        hero.command(peasant,"dropItem",yakPos)
    # If topItem type is "mushroom":
    if topItem.type == "mushroom":
        # Command to "dropItem" to yetis:
        hero.command(peasant,"dropItem",yetiPos)
    # If topItem type is "lightstone":
    if topItem.type == "lightstone":
        # Command to "dropItem" to skeletons:
        hero.command(peasant,"dropItem",skeletonPos)




# Use mushrooms to defeat the Yeti.
# Use potions to heal the hero.
yeti = hero.findNearestEnemy()
peasant = hero.findFriends()[0]
# Use "pickUpItem" command to take items.
items = peasant.findItems()
for i in items:
    hero.command(peasant,"pickUpItem",i)
# Use "dropItem" command to put the top item.
# Drop the key near the door to open it.
key = peasant.findNearestByType("gold-key")
hero.command(peasant,"pickUpItem",key)
hero.command(peasant,"dropItem")
# Use peasant.peekItem() to get know the item on the top.
# Mushrooms to the yeti, potions to the hero.


# Aaaand one (or two) final hit to the yeti.



# Useful constants.
trapAttackRange = 3;
radiusStep = 10;
center = {"x": 68, "y": 68};

# Go, Go, GO!

while True:
    hazas = hero.findHazards()
    va = Vector(68,68)
    va = Vector.subtract(va,hero.pos)
    va = Vector.normalize(va)
    va = Vector.multiply(va,3)
    nearest = hero.findNearest(hazas)
    distance = hero.distanceTo(nearest)
    if distance <5:
        va = Vector.rotate(va,Math.PI / 2)
    va = Vector.add(va,hero.pos)
    hero.move(va)



####### Fragile Maze 冰迷宫

distanceBetweenRooms = 16
startRoom = {"x": 18, "y": 19}
startR = {"x": 18, "y": 19,"u":1,"r":1,"d":0,"l":0}

hero.wait(1.2)
hadposs = []  #已经走过的房间点
def newRoom():
    new = {"x": hero.pos.x, "y": hero.pos.y,"u":0,"r":0,"d":0,"l":0}
    if hero.isPathClear(hero.pos, {"x": hero.pos.x, "y": hero.pos.y + distanceBetweenRooms}):
        new.u = 1
    if hero.isPathClear(hero.pos, {"x": hero.pos.x, "y": hero.pos.y - distanceBetweenRooms}):
        new.d = 1
    if hero.isPathClear(hero.pos, {"x": hero.pos.x + distanceBetweenRooms, "y": hero.pos.y }):
        new.r = 1
    if hero.isPathClear(hero.pos, {"x": hero.pos.x - distanceBetweenRooms, "y": hero.pos.y }):
        new.l = 1
    return new


def whichRoom(apos,hadposslist):
    for i,h in enumerate(hadposslist):
        if  Math.abs(h.x - apos.x) <3 and Math.abs(h.y - apos.y) <3:
            return i,h
    return None

while hero.pos.x<108 or hero.pos.y <90:
    if not whichRoom(hero.pos, hadposs):
        hadposs.append(newRoom())
    i,nowRoom = whichRoom(hero.pos, hadposs)
    if nowRoom.u == 1 and not whichRoom( {"x": hero.pos.x, "y": hero.pos.y + distanceBetweenRooms} , hadposs):
        hero.wait(0.2)
        hero.moveXY(nowRoom.x,nowRoom.y + distanceBetweenRooms)
    elif nowRoom.r == 1 and not whichRoom( {"x": hero.pos.x + distanceBetweenRooms , "y": hero.pos.y } , hadposs):
        hero.wait(0.2)
        hero.moveXY(nowRoom.x + distanceBetweenRooms,nowRoom.y)    
    elif nowRoom.d == 1 and not whichRoom( {"x": hero.pos.x  , "y": hero.pos.y - distanceBetweenRooms } , hadposs):
        hero.wait(0.2)
        hero.moveXY(nowRoom.x ,nowRoom.y - distanceBetweenRooms)



# GOLDEN CHOICE
# You must collect the required amount of gold.
# The gate keeper will tell you how much you need.
# Always move in the direction of the exit.
# For each row you can take only one coin.
# Choose only one from the nearest coins in the next row.

# Distance between rows and coins.
distanceX = 4
distanceY = 6
zeroPoint = {"x": 14, "y": 14}
coinLines = 10

def makeGoldMap(coins):
    template = [[0 for j in range(2 * coinLines - 1)] for i in range(coinLines)]
    for coin in coins:
        row = int((coin.pos.y - zeroPoint.y) / distanceY)
        col = int((coin.pos.x - zeroPoint.x) / distanceX)
        template[row][col] = coin.value
    return template

# Prepare the gold map. It looks like:
# [[1, 0, 9, 0, 4],
#  [0, 1, 0, 9, 0],
#  [8, 0, 2, 0, 9]]
goldMap = makeGoldMap(hero.findItems())

# Find your path.

#从下层开始更新每个值， 到顶层
for i in range(1,len(goldMap)):
    for j in range(len(goldMap[i])):
        nowV = goldMap[i][j]
        if nowV > 0:
            if j == 0:
                leftV = nowV
            else:
                leftV=goldMap[i-1][j-1]+ nowV
            if j == len(goldMap[i]) - 1 :
                rightV = nowV
            else:
                rightV = goldMap[i-1][j+1] + nowV
            if leftV > rightV:
                goldMap[i][j] = leftV
            else:
                goldMap[i][j] = rightV

#对比顶层找出最大值
maxv = 0
topmaxj = None
for j,v in enumerate(goldMap[len(goldMap)-1]):
    if v > maxv:
        maxv = v
        topmaxj = j 

goodRoad =[topmaxj]

for i in range(len(goldMap)-1,0):
    if topmaxj == len(goldMap[i])-1 or goldMap[i][topmaxj-1] > goldMap[i][topmaxj +1] :
        j = topmaxj -1
    else:
        j = topmaxj +1
    goodRoad.append(j)


######## 数字华容道-骨架之谜  ############

# Solve the puzzle and the treasures will be yours.
# Say numbers from 1 to 8 to move skeletons.

# The necromancer always knows the puzzle state.
boneMaster = hero.findFriends()[0]
puzzleState = boneMaster.getPuzzleState()
# The result state should be this:
goalState = [[1,2,3],[4,5,6],[7,8,0]]

# Solve, Solve, Solve!
dxdy = [[-1,0],[0,1],[1,0],[0,-1]]
dire = [0,1,2,3]  #上，右，下，左

def whereNum(n,state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == n:
                return i,j
    return (None,None)
    


def zeroCanMove(goodNum = []):
    puzzle=boneMaster.getPuzzleState()
    zx,zy = whereNum(0,puzzle)
    res = [0,0,0,0] #四个方向不可走
    for i in dire:
        xx = zx + dxdy[i][0]
        yy = zy + dxdy[i][1]
        if xx<=2 and xx >=0 and yy<=2 and yy>=0 and puzzle[xx][yy] not in goodNum:
            res[i] = 1
    return res
    


def move0(forway):
    puzzle=boneMaster.getPuzzleState()
    zx,zy = whereNum(0,puzzle)
    for i in dire:
        if forway == i:
            xx = zx + dxdy[i][0]
            yy = zy + dxdy[i][1]
    hero.say(puzzle[xx][yy])


def zeroMove(x,y,goodNum = []):
    wall = []
    way = []
    wall.append(zeroCanMove(goodNum))
    while True:
        puzzle=boneMaster.getPuzzleState()
        zx,zy = whereNum(0,puzzle)
        dx = (x-zx)
        dy = (y-zy)
        if dx == 0 and dy==0:
            break
        if Math.abs(dx)>Math.abs(dy):
            if dx>0:
                dway = 2
            else:
                dway = 0
        else:
            if dy>0:
                dway = 1
            else:
                dway = 3
        gotodire = None
        for i in range(dway,dway+4):
            if wall[-1][i%4]:
                #假如当前i%4这个方向可以走：
                gotodire = i%4
                break
        if gotodire == None and len(way) == 0:
            hero.say("can't move 0 to ")
            break
        elif gotodire == None:
            #四个方向不可走，则回退
            gotodire = (way[-1]+2)%4
            move0(gotodire)
            way.pop(-1)
            wall.pop(-1)
        else:
            move0(gotodire)
            way.append(gotodire)
            wall.append(zeroCanMove(goodNum))
        #更新走过来的不再回去
        wall[-1][(gotodire+2)%4] = 0
        

