width = int(input())
length = int(input())
height = int(input())

carton = 1
free_space = int((width * length * height) / carton)
occupied_space = 0
command = input()

while True:
    if command == 'Done':
        break

    occupied_space = int(command)
    free_space -= occupied_space

    if free_space <= 0:
        break

    command = input()

if command == 'Done':
    print(f'{free_space} Cubic meters left.')

if free_space <= 0:
    print(f'No more free space! You need {abs(free_space)} Cubic meters more.')
