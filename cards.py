class Cards:
  def __init__(self, name, cost):
    self.name = name
    self.cost = cost


class Units (Cards):
  def __init__(self, name, cost, power, resistance):
    super().__init__(name, cost)
    self.power = power
    self.resistance = resistance
  
  def show_stats(self):
    print(f'Name: {self.name}, Power: {self.power}, Resistance: {self.resistance}')


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


red_ninja = Units('Red Belt Ninja', 3, 3, 4)

red_ninja.show_stats()

# red_ninja.resistance +=3

hard_algorithm = Effects('Hard Algorithm', 2, 'resistance', 3)

hard_algorithm.affect(red_ninja)

red_ninja.show_stats()
