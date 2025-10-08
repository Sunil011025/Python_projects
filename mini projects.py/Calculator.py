import os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

def calculator():
    num1=float(input("Enter a number : "))
    for sym in operations:
        print(sym)
    continue_flag=True
    while continue_flag:
        op_sym=input("pick an operation : ")
        num2=float(input("Enter other number : "))
        cal_fun=operations[op_sym]
        output=cal_fun(num1,num2)
        print(f"{num1} {op_sym} {num2} = {output}")

        should_continue=input(f"Enter 'yes' to continue calculation with {output} or 'new' to start new or 'no' to exit : ").lower()
        if should_continue=='yes':
            num1=output
        elif should_continue=='new':
            continue_flag=False
            os.system('cls')
            calculator()
        else :
            continue_flag=False
            print("THANK YOU.....!!!")
calculator()