# class House():

#     def __init__(self, builder):
#         self.stories = builder.stories
#         self.doors = builder.doors
#         self.roof = builder.roof

#     def house(self):
#         return f"{self.stories} - {self.doors} - {self.roof}"

# class HouseBuilder():

#     def __init__(self):
#         pass

#     def setStories(self, stories):
#         self.stories = stories
#         return self
    
#     def setDoors(self, doors):
#         self.doors = doors
#         return self

#     def setRoof(self, roof):
#         self.roof = roof
#         return self

#     def build(self):
#         return House(self)


# class Director():

#     def __init__(self, builder):
#         self.builder = builder

#     def build_1_story(self):
#         return self.builder.setStories(1).setDoors(1).setRoof("Flat").build()
    
#     def build_2_story(self):
#         return self.builder.setStories(2).setDoors(2).setRoof("Pointy").build()


# HB = HouseBuilder()
# director = Director(HB)

# one_story = director.build_1_story()
# print(one_story.house())


class Enemy():

    def __init__(self, enemygenerator):
        self.type = enemygenerator.type
        self.clan = enemygenerator.clan
        self.baseHP = enemygenerator.baseHP
        self.baseAttack = enemygenerator.baseAttack
        self.baseDefense = enemygenerator.baseDefense

    def info(self):
        return f"{self.type} - {self.clan} : HP - {self.baseHP} Attack - {self.baseAttack} Defense - {self.baseDefense}"

class EnemyGenerator():

    def __init__(self):
        pass

    def setType(self, type):
        self.type = type
        return self

    def setClan(self, clan):
        self.clan = clan
        return self

    def setBaseHP(self, baseHP):
        self.baseHP = baseHP
        return self

    def setBaseAttack(self, baseAttack):
        self.baseAttack = baseAttack
        return self

    def setBaseDefense(self, baseDefense):
        self.baseDefense = baseDefense
        return self

    def spawn(self):
        return Enemy(self)

class Spawner():

    def __init__(self, enemygenerator):
        self.enemygenerator = enemygenerator

    def spawnElf(self):
        return self.enemygenerator.setType("Ranged").setClan("ForestElf").setBaseHP(500).setBaseAttack(50).setBaseDefense(35).spawn()
    
    def spawnAssassin(self):
        return self.enemygenerator.setType("Melee").setClan("Darkin").setBaseHP(300).setBaseAttack(90).setBaseDefense(45).spawn()


EG = EnemyGenerator()

spawner = Spawner(EG)
assassin = spawner.spawnAssassin()
print(assassin.info())