length = int(input())
width = int(input())

cake_slice = 1
area_cake = length * width
all_pieces = int(area_cake / cake_slice)

while True:
    command = input()

    if command == 'STOP':
        break

    pieces = int(command)
    all_pieces -= pieces

    if all_pieces <= 0:
        break

if command == 'STOP':
    print(f'{all_pieces} pieces are left.')

if all_pieces <= 0:
    print(f'No more cake left! You need {abs(all_pieces)} pieces more.')
