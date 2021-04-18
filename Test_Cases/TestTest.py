from TheGame.character.impl.Mage import Mage
from TheGame.character.impl.Hunter import Hunter
from TheGame.character.impl.Warrior import Warrior

mage = Mage()
hunter = Hunter()
warrior = Warrior()

print(mage.use_common_attack())
print(hunter.use_common_attack())
print(warrior.use_common_attack())
