num1 = input("What is your name: ")
num2 = int(input("What is your basic salary?: "))

house_allowance= 0.20 * num2
transport_allowance= 0.10 * num2

gross_salary=house_allowance+transport_allowance+num2

if gross_salary<=100000:
    num4=gross_salary*0.98
    final_salary = num4
    print("Salary summary")
    print("Your gross salary is",gross_salary)
    print("Your final salary is",final_salary)

elif gross_salary >= 100000:
    num5=gross_salary*0.95
    final_salary=num5
    print("Salary summary")
    print("Your gross salary is",gross_salary)
    print("Your final salary is",final_salary)

if final_salary>=100000:
    print("High income")
else:
    print("Standard income")
    






