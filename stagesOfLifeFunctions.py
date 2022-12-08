def lifeStage(age):
    if age < 2:
        print("You are a baby.")
    elif age >= 2 and age < 4:
        print("You are a toddler.")
    elif age >= 4 and age < 13:
        print("You are a kid.")
    elif age >= 13 and age < 20:
        print("You are a teenager.")
    elif age >= 20 and age < 65:
        print("You are an adult.")
    elif age >= 65:
        print("You are an elder.")

lifeStage(34)
lifeStage(1)
lifeStage(8)
lifeStage(19)
lifeStage(65)
lifeStage(2)