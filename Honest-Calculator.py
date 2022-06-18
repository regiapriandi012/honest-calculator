# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
while True:
    print(msg_0)
    calc = input()

    x, oper, y = calc.split(" ")
    if x.isalpha() or y.isalpha():
        print(msg_1)
    elif oper == "+" or oper == "-" or oper == "*" or oper == "/":
        if oper == "+":
            print(float(x) + float(y))
            break
        elif oper == "-":
            print(float(x) - float(y))
            break
        elif oper == "*":
            print(float(x) * float(y))
            break
        elif oper == "/" and float(y) != 0:
            print(float(x) / float(y))
            break
        elif oper == "/" and float(y) == 0:
            print(msg_3)

    else:
        print(msg_2)