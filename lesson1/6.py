num_1 = int(input("Input emount of kms you run daily: "))
num_2 = int(input("Input emount of kms you wish to run daily: "))
day = 1
cof = 1.1
while num_1 <= num_2: 
    day = day + 1
    num_1 = num_1 * cof
    print (f'{day} day: {num_1:.2f} kms')
print (f"You will run at least {num_2} kms in {day} days!")
