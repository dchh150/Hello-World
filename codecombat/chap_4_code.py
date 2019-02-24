
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