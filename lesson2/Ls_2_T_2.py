
k = 1  # index for 2nd element
i = 0  # index for 1st element

while True:
    print('Please choice the action:')
    print('1. Input data\n2. View the data\n3. End the program')
    choice = input("Input your choice by typing the number of choice: ")

    if choice == "1":
        data = (input("Input your data separated with comma: ").split(","))

    elif choice == "2":
        print("Your original data -", data)
        while k < len(data) and i < len(data):
            data[i], data[k] = data[k], data[i]
            k += 2
            i += 2
        print("Your data after replacement ", data)
    elif choice == "3":
        break
    else:
        print("Error. Enter only number in range 1-3.")
