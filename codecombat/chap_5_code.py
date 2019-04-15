while True:
    potion = hero.findFriendlyMissiles()[0]
    firetraps = hero.findHazards()
    # Remember that a Fire Trap will trigger if you move closer than 3 meters!
    omarn = hero.findByType("potion-master")[0]
    if potion:
        dest = potion.targetPos;
        # Go get the potion.
        a = Vector.subtract(dest,hero.pos)
        a = Vector.normalize(a)
        a = Vector.multiply(a,4)
        nearest = hero.findNearest(firetraps)
        nearestD = hero.distanceTo(nearest)
        if nearestD < 5 :
            b = Vector.subtract(hero.pos,nearest.pos)
            b = Vector.normalize(b)
            b = Vector.multiply(b,4)
            a = Vector.add(a,b)
        a =  Vector.add(a,hero.pos)
        hero.move(a)
        pass
    else:
        if omarn and hero.distanceTo(omarn) > 10:
            # Move back to Omarn.
            a = Vector.subtract(omarn.pos,hero.pos)
            a = Vector.normalize(a)
            a = Vector.multiply(a,4)
            nearest = hero.findNearest(firetraps)
            nearestD = hero.distanceTo(nearest)
            if nearestD < 5 :
                b = Vector.subtract(hero.pos,nearest.pos)
                b = Vector.normalize(b)
                b = Vector.multiply(b,4)
                a = Vector.add(a,b)
            a =  Vector.add(a,hero.pos)
            hero.move(a)

            # Warning: isPathClear doesn't work with Hazards!
            pass
        else:
            hero.say("Hup, hup!")