from random import choice
from ability import Ability
from weapon import Weapon
from armor import Armor

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''
          Instance properties:
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
    
    def add_ability(self, ability):
      ''' Add ability to abilities list '''

      # We use the append method to add ability objects to our list.
      self.abilities.append(ability)

    def attack(self):
      '''
        Calculate the total damage from all ability attacks.
        return: total_damage:Int
      '''
      total_damage = 0

      for ability in self.abilities:
        total_damage += ability.attack()
      
      return total_damage
    
    def add_armor(self, armor):
      '''
        Add armor to self.armors
        Armor: Armor Object
      '''
      # We use the append method to add armor objects to our list.
      self.armors.append(armor)

    def defend(self, damage_amt):
      '''Calculate the total block amount from all armor blocks.
        return: total_block:Int
      '''
      total_block = 0

      for armor in self.armors:
        total_block += armor.block()

      return total_block


    def take_damage(self, damage):
      '''Updates self.current_health to reflect the damage minus the defense.
      '''
      self.current_health -= damage - self.defend(damage)


    def is_alive(self):
      '''Return True or False depending on whether the hero is alive or not.
      '''
      #Check the current_health of the hero.
      # if it is <= 0, then return False. Otherwise, they still have health
      # and are therefore alive, so return True
      return self.current_health > 0
    
    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # Fight each hero until a victor emerges.
        # Phases to implement:
        if not len(self.abilities) and not len(opponent.abilities):
          print("Draw")
        else:
          while self.is_alive() and opponent.is_alive():
            my_attack = self.attack()
            opp_attack = opponent.attack()

            self.take_damage(opp_attack)
            opponent.take_damage(my_attack)
        
        if self.is_alive():
          print(f"{self.name} won!")
        else:
          print(f"{opponent.name} won!")

        # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        # 1) else, start the fighting loop until a hero has won
        # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
        # 3) After each attack, check if either the hero (self) or the opponent is alive
        # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
        
        random_winner = choice([self, opponent])
        print(f"{random_winner.name} won!")
    
    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
    
    ability = Ability("Great Debugging", 50)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    print(hero.abilities)

    ability2 = Ability("Skydiving", 100)
    hero.add_ability(ability)
    print(hero.abilities)

    print(hero.attack())

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)

    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)

    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
    
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)

    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
