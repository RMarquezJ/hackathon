class Cards:
  def __init__(self, name, cost):
    self.name = name
    self.cost = cost


class Units (Cards):
  def __init__(self, name, cost, power, resistance):
    super().__init__(name, cost)
    self.power = power
    self.resistance = resistance
  

  



class Effects(Cards):
  def __init__(self, name, cost, stat, magnitude):
    super().__init__(name, cost)
    self.stat = stat
    self.magnitude = magnitude

    def affect(unit):
      pass