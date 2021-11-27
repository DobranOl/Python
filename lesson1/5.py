earning = int(input("Input your company profit: "))
costs = int(input("Input your company costs: "))
profit = earning - costs
if earning > costs:
    print('Your company works for profit! Congrats!')
    emp_num = int(input("Input the number of employees: "))
    Rent = (profit / earning) * 100
    pf_per_empl = profit / emp_num
    print  (f"Profitability is: {Rent:.2f}%")
    print (f"Profit per employee is: {pf_per_empl:.2f}")
else: 
    print ("Your company is operating at a loss!")