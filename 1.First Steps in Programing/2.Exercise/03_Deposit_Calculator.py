deposit = float(input())
deposit_mounts = int(input())
glp = float(input())

total = deposit + deposit_mounts * ((deposit * glp / 100) / 12)

print(total)
