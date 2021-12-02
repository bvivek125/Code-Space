import sys

def main():
    number_of_arguements()
    x=int(sys.argv[1])
    operator=sys.argv[2]
    y=int(sys.argv[3])
    result = calculate(x,operator,y)
    print(result)

def calculate(x,operator,y):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x -y 
    elif operator == '*':
        return x*y
    else:
        print("Please use the included operators +,-,*")

def number_of_arguements():
    if len(sys.argv) > 4:
        print("Too many arguements")
        sys.exit(1)
    elif len(sys.argv) < 1:
        print("Not enough arguements")
        sys.exit(1)
    else:
        print("Calculating....")

main()