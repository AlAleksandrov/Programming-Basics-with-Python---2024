name_animal = input()
result = ""

if name_animal == "dog":
    result = "mammal"
elif (name_animal == "crocodile"
      or name_animal == "tortoise"
      or name_animal == "snake"):
    result = "reptile"
else:
    result = "unknown"

print(result)