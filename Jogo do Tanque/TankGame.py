from Tank import Tank

tanks = {'a':Tank('Kauê'), 'b':Tank('Gustavo'), 'c':Tank('Diego')}
alive_tanks = len(tanks)

while alive_tanks > 1:
    for tank_name in sorted(tanks.keys()):
        print(tank_name, tanks[tank_name])
    first = input('Quem atirou? ').lower()
    second = input('Atirou em quem? ').lower()
    try:
        first_tank = tanks[first]
        second_tank = tanks[second]
    except KeyError as name:
        print('Não existe esse tanque!', name)
        continue
    if not first_tank.alive or not second_tank.alive:
        print('Um dos tanques está morto!')
        continue
    print('*' * 30)
    first_tank.fire_at(second_tank)
    if not second_tank.alive:
        alive_tanks -= 1
    print('*' * 30)

for tank in tanks.values():
    if tank.alive:
        print(tank.name, 'é o vencedor!')
        break