# hero.py
class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
  def __init__(self, name, starting_health=100):
    '''Instance properties:
      name: String
      starting_health: Integer
      current_health: Integer
    '''

    # we know the name of our hero, so we assign it here
    self.name = name
    # similarly, our starting health is passed in, just like name
    self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  my_hero = Hero("wonder women ", 200)
  print(my_hero.name)
  print(my_hero.current_health)

  def battle(self, opponent):
  ''' Current Hero will take turns fighting the opponent hero passed in.
  '''
  # TODO: Fight each hero until a victor emerges.
  # Phases to implement:
  #1) randomly choose winner, print the name of the victor
  # Hint: Look into random library, more specifically the choice metho
   name and max_block