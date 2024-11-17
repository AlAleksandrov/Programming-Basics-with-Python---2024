n = int(input())
result = 1
is_enough = False

for i in range(1, n+1):

    for j in range(i):
        print(result, end=" ")

        if result == n:
            is_enough = True
            break

        result += 1
    if is_enough:
        break
    print()
