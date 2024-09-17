import random
# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name
    def battleCry(self):
        return "¡Odin os posee a todos!"
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return f"{self.name} ha recibido {self.damage} puntos de daño"
        else:
            #self.health =< 0:
            return f"{self.name} ha muerto en acto de combate"
# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)
    def attack():
        Soldier.attack()
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return f"Un 'Saxon' ha recibido {self.damage} puntos de daño"
        else:
            #self.health =< 0:
            return "Un 'Saxon' ha muerto en combate"
# Davicente
class War():
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []
    def addViking(self, viking):
        Viking.self.viking = viking
        self.viking_army.append(self.viking)
    def addSaxon(self, saxon):
        Saxon.self.saxon = saxon
        self.saxon_army.append(self.saxon)
    def vikingAttack(self):
        saxon1 = random.choice(self.saxon_army)
        viking1 = random.choice(self.viking_army)
        saxon1.receiveDamage(viking1.strength)
        if saxon1(self.health) <= 0:
            saxon_army.remove(saxon1)
        else:
            return f"El Saxon ha recibido {viking1.strength} puntos de daño"
    def saxonAttack(self):
        saxon2 = random.choice(self.saxon_army)
        viking2 = random.choice(self.viking_army)
        viking2.receiveDamage(saxon2.strength)
        if viking2(self.health) <= 0:
            viking_army.remove(viking2)
        else:
            return f"{viking2.name} ha recibido {saxon2.strength} puntos de daño"
    def showStatus(self):
        if len(self.saxon_army) == 0:
            return "¡Los Vikingos han ganado la guerra del siglo!"
        elif len(self.viking_army) == 0:
            return  "Los Sajones han luchado por sus vidas y sobreviven otro día..."
        else:
            return "Los Vikingos y los Sajones todavía están en plena batalla."
    pass
#yop
class War2():
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []
    def addViking(self, viking):
        Viking.self.viking = viking
        self.viking_army.append(self.viking)
    def addSaxon(self, saxon):
        Saxon.self.saxon = saxon
        self.saxon_army.append(self.saxon)
    def vikingAttack(self):
        saxon3 = random.choice(self.saxon_army)
        viking3 = random.choice(self.viking_army)
        saxon3.receiveDamage(viking3.strength)
        if saxon3(self.health) <= 0:
            saxon_army.remove(saxon3)
        else:
            return f"El Saxon ha recibido {viking3.strength} puntos de daño"
    def saxonAttack(self):
        saxon4 = random.choice(self.saxon_army)
        viking4 = random.choice(self.viking_army)
        viking4.receiveDamage(saxon4.strength)
        if viking4(self.health) <= 0:
            viking_army.remove(viking4)
        else:
            return f"{viking4.name} ha recibido {saxon4.strength} puntos de daño"
    def showStatus(self):
        if len(self.saxon_army) == 0:
            return "¡Los Vikingos han ganado la guerra del siglo!"
        elif len(self.viking_army) == 0:
            return  "Los Sajones han luchado por sus vidas y sobreviven otro día..."
        else:
            return "Los Vikingos y los Sajones todavía están en plena batalla."
    pass