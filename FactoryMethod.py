from _future_ import annotations
from abc import ABC, abstractmethod

class Enemy(ABC):
    
    @abstractmethod
    def attackPattern(self) -> str:
        pass
    

class EnemySpawner(ABC):
    
    @abstractmethod
    def spawn(self) -> List[Enemy]:
        pass
    
class RangedEnemy(Enemy):
    
    def attackPattern(self) -> str:
        return "arrow attack"
        
class MeleeEnemy(Enemy):
    
    def attackPattern(self) -> str:
        return "hammer attack"
        

class CheeseStratSpawner(EnemySpawner):
    
    def _init_(self):
        pass
    
    def spawn(self) -> List[Enemy]:
        a = MeleeEnemy()
        b = [RangedEnemy() for i in range(3)]
        return [a]+b
        
class YoloSpawner(EnemySpawner):
    
    def spawn(self) -> List[Enemy]:
        m = [MeleeEnemy() for i in range(5)]
        return m
        
        
def StratGenerator(spawn: EnemySpawner) -> None:
    
    party = spawn().spawn()
    for i in party:
        print(i.attackPattern())
        
        
strat = int(input("How would you like to attack?"))

if (strat == 0):
    StratGenerator(CheeseStratSpawner)
else:
    StratGenerator(YoloSpawner)