class Tank:
  def __init__(self, name):
    self.name = name
    self.alive = True
    self.ammo = 5
    self.armor = 60

  # Status do Tanque

  def __str__(self):
    if self.alive:
      return f'{self.name} - Armadura: {self.armor}, Munição: {self.ammo}'
    else:
      return f'{self.name} MORREU.'

  # Atirar em outro tanque

  def fire_at(self, enemy):
    if self.ammo >= 1:
      self.ammo -= 1
      print(self.name, 'atirou em', enemy.name)
      enemy.hit()
    else:
      print(self.name, 'não tem munição!')

  # Dano em alguem

  def hit(self):
    self.armor -= 20
    print(self.name, 'tomou dano!')
    if self.armor <= 0:
      self.explode()

  # Morte de um tanque

  def explode(self):
    self.alive = False
    print(self.name, 'explodiu!')