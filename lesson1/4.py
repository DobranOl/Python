#great thanks to Sergei
user_num = int(input("Input your biiiig number: "))

check_num = user_num % 10
user_num = user_num // 10

while user_num > 0:
    if user_num % 10 > check_num:
        check_num = user_num % 10
    user_num = user_num // 10

print("The biggest number is:", check_num)
