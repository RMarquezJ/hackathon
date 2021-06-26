class Cards:
  def __init__(self, name, cost):
    self.name = name
    self.cost = cost


class Units (Cards):
  def __init__(self, name, cost, power, resistance):
    super().__init__(name, cost)
    self.power = power
    self.resistance = resistance

  def play(self, which_player):
    print(f'Player {which_player} has summoned {self.name}')
  
  def attack(self, target):
    if isinstance(target, Units) == False:
      print('Must be played on a Unit card')
      return
    target.resistance -= self.power
    if target.resistance <= 0:
      print(f'{target} has died, Game Over')
    return self
  
  def show_stats(self):
    print(f'Name: {self.name}, Power: {self.power}, Resistance: {self.resistance}')
    return self
  
  def __repr__(self):
      return self.name


class Effects(Cards):
  def __init__(self, name, cost, stat, magnitude):
    super().__init__(name, cost)
    self.stat = stat
    self.magnitude = magnitude

  def affect(self, target):
    if isinstance(target, Units) == False:
      print('Must be played on a Unit card')
      return
    if self.stat == 'resistance':
      target.resistance += self.magnitude
    elif self.stat == 'power':
      target.power += self.magnitude
    
    print(f'{target} now has {target.power} Power and {target. resistance} Resistance\n')


red_ninja = Units('Red Belt Ninja', 3, 3, 4)
black_ninja = Units('Black Belt Ninja', 4, 5, 4)
hard_algorithm = Effects('Hard Algorithm', 2, 'resistance', 3)
not_managed_promise = Effects('Not Managed Promise', 1, 'resistance', -2)
pair_programming = Effects('Pair Programming', 3, 'power', 2)

red_ninja.play(1)
hard_algorithm.affect(red_ninja)
black_ninja.play(2)
not_managed_promise.affect(red_ninja)
pair_programming.affect(red_ninja)
red_ninja.attack(black_ninja)