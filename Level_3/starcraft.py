from random import *
# Python - class Unit
class Unit:
    # __init__ : automatic calling
    def __init__(self, name, hp, speed):
        # Member variable
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} unit has been created. ".format(self.name))
    
    def move(self,location):
        print("[Move]", end=" ")
        print("{0} : Move in direction {1} [speed : {2}]"\
            .format(self.name, location, self.speed))

# class Attack Unit
class AttackUnit(Unit):# inherit (Unit)
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        # Member variable
        self.damage = damage
    
    def attack(self, location):
        print("{0} : Attack the enemy in the direction {1}. [damage {2}]"\
            .format(self.name,location,self.damage))

    def damaged(self, damage):
        print("{0} : {1} Damaged.".format(self.name, damage))
        self.hp -= damage
        print("{0} : hp:{1}".format(self.name, self.hp))
        if self.hp<=0:
            print("{0} : destroyed".format(self.name))

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"marine",40,1,5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : Use stimpack".format(self.name))
        else:
            print("{0} : So hurt!".format(self.name))  

class Tank(AttackUnit):
    seize_developed = False
    def __init__(self):
         AttackUnit.__init__(self,"Tank",150,1,30)
         self.seize_mode = False
    
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        if self.seize_mode == False:
            print("{0} : Switch to Seize mode".format(self.name))
            self.damage *= 2
            self.seize_mode = True 
        else:
            print("{0} : Turns off Seize mode.".format(self.name))
            self.damage /= 2
            self.seize_mode = False 


# Flyable Unit
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : flies in the direction {1}. [speed : {2}]".format(self.name,location,self.flying_speed))

# Multiple inheritance
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    # move(): Redefining
    def move(self, location):
        print("[Fly move]", end=" ")
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"wraith", 120, 8, 20)
        self.clocked = False
    
    def clocking(self):
        if self.clocked == True:
            print("{0} : turns off clocking".format(self.name))
            self.clocked = False
        else:
            print("{0} : switch to clocking".format(self.name))
            self.clocked = True 





# building
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        Unit.__init__(self, name, hp, 0) # or super().__init__(name,hp,0) but super() : can't inherit multiple
        self.location = location

def game_start():
    print("game start!")

def game_over():
    print("Player: gg")
    print("[Player] is game over")

# game start

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()
t3 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(t3)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1")

Tank.seize_developed = True 
print("Tank Seize Mode development has been completed.")

for unit in attack_units:
    if isinstance(unit,Marine):
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1")

for unit in attack_units:
    unit.damaged(randrange(5,21))

game_over()

