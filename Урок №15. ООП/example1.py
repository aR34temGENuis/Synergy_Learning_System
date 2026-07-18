class Transport:

   def __init__(self, name, max_speed, mileage):
      self.name = name
      self.max_speed = max_speed
      self.mileage = mileage
   def __str__(self):
      return f'Название автомобиля: {self.name}. Скорость {self.max_speed}. Пробег {self.mileage}.'

Autobus = Transport('Renault Logan', 180, 12)

print(Autobus)    