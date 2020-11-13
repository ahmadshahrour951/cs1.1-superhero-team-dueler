from random import choice

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
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
    
    def fight(self, opponent):
        '''
        Current Hero will take turns fighting the opponent hero passed in.
        '''
        random_winner = choice([self, opponent])
        print(f"{random_winner.name} won!")


if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)
