# FizzBuzz quiz

def input_data(ref):
    while True:
        try:
            num = int(input("Enter an integer: "))
            if num > ref:
                return num
                break
            else:
                print("Enter a positive number greater than the value of {}".format(ref))
                print
        except ValueError:
            print("An integer, not float or string please")
            print()

if __name__ == '__main__':
    start_num = input_data(0)
    end_num = input_data(start_num)
    for i in range(start_num,end_num+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)