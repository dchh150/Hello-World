import random
values=list(range(1,11))+'J Q K'.split()
suits='黑桃 红心 梅花 方块'.split()
deck=['{} {}'.format(s,v) for v in values for s in suits]
#print(deck)
random.shuffle(deck)
#print(deck)
while deck:
    input(deck.pop())
