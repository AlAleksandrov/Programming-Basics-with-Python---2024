steps_target = 10_000

total_steps = 0
command = input()

while True:
    if command == 'Going home':
        command = input()
        steps = int(command)
        total_steps += steps
        break

    steps = int(command)
    total_steps += steps

    if total_steps >= steps_target:
        break

    command = input()

if total_steps >= steps_target:
    diff = total_steps - steps_target
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    diff = steps_target - total_steps
    print(f'{diff} more steps to reach goal.')
