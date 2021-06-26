class Cards:
  def __init__(self, name, cost):
    self.name = name
    self.cost = cost


class Units (Cards):
  def __init__(self, name, cost, power, resistance):
    super().__init__(name, cost)
    self.power = power
    self.resistance = resistance
  
  def attack(self, target):
    if isinstance(target, Units) == False:
      print('Must be played on a Unit card')
      return
    target.resistance -= self.power
    if target.resistance <= 0:
      print(f'{target} has died, Game Over\n')
    return self
  
  def show_stats(self):
    print(f'Name: {self.name}, Power: {self.power}, Resistance: {self.resistance}\n')
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
    
    print(f'"{self.name}" was played on "{target}", and now has {target.power} Power and {target. resistance} Resistance\n')
  
  def __repr__(self):
      return self.name

class Player:
  def __init__(self, name):
    
    self.name = name
    self.units = []
    self.effects = []

  def add_unit(self, card_name):
    if isinstance(card_name, Units)==True:
      self.units.append(card_name)
    else:
      print('Must be a "Unit" card')
    return self
  
  def add_effect(self, card_name):
    if isinstance(card_name, Effects):
      self.effects.append(card_name)
    else:
      print('Must be an "Effect" card')
    return self
  
  def __repr__(self):
      return self.name