from _future_ import annotations
from abc import ABC, abstractmethod

# Enemy abstractions

class RangedEnemy(ABC):
    
    @abstractmethod
    def attackPattern(self) -> str:
        pass
    
class MeleeEnemy(ABC):
    
    @abstractmethod
    def attackPattern(self) -> str:
        pass
    
class MageEnemy(ABC):
    
    @abstractmethod
    def attackPattern(self) -> str:
        pass
    
class Clan(ABC):
    
    @abstractmethod
    def spawnMelee(self) -> List[MeleeEnemy]:
        pass
    
    @abstractmethod
    def spawnRanged(self) -> List[RangedEnemy]:
        pass
    
    @abstractmethod
    def spawnMage(self) -> List[MageEnemy]:
        pass
    
    
class ShadowRanged(RangedEnemy):
    
    def attackPattern(self) ->  str:
        return "Shadow arrows"
        
class ShadowMelee(MeleeEnemy):
    
    def attackPattern(self) ->  str:
        return "Shadow knives akimbo"
        
class ShadowMage(MageEnemy):
    
    def attackPattern(self) ->  str:
        return "Shadow magic: Necromancy"
        

class CrusaderRanged(RangedEnemy):
    
    def attackPattern(self) ->  str:
        return "Holy fire arrows"
        
class CrusaderMelee(MeleeEnemy):
    
    def attackPattern(self) ->  str:
        return "Holy charge"
        
class CrusaderMage(MageEnemy):
    
    def attackPattern(self) ->  str:
        return "Holy magic: Demon quell"
        
## Spawn clamns

class ShadowKin(Clan):
    
    def spawnMelee(self) -> List[MeleeEnemy]:
        return [ShadowMelee() for i in range(1)]
    
    def spawnRanged(self) -> List[RangedEnemy]:
        return [ShadowRanged() for i in range(3)]
    
    def spawnMage(self) -> List[MageEnemy]:
        return [ShadowMage() for i in range(5)]

class Crusaders(Clan):
    
    def spawnMelee(self) -> List[MeleeEnemy]:
        return [CrusaderMelee() for i in range(5)]
    
    def spawnRanged(self) -> List[RangedEnemy]:
        return [CrusaderRanged() for i in range(3)]
    
    def spawnMage(self) -> List[MageEnemy]:
        return [CrusaderMage() for i in range(1)]
        
        
def Guild(clan: Clan):
    
    m, r, s = clan.spawnMelee(), clan.spawnRanged(), clan.spawnMage()
    
    for i in m:
        print(i.attackPattern())
        
    for i in r:
        print(i.attackPattern())
    
    for i in s:
        print(i.attackPattern())
        
cl = int(input("Select your class: ShadowKin[0] or Crusaders[1]"))
match cl:
    case 0:
        Guild(ShadowKin())
    case 0:
        Guild(Crusaders())
    case _:
        print("Nope")