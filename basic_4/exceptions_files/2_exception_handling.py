try:
    num1 = 2
    num2 = 0
    print(num1 / num2)
    print("Done Calculation")
except ZeroDivisionError:
    print("Error Devided by Zero")
except (ValueError, TypeError):
    print("Error Occured")

try:
    num1 = 2
    num2 = 0
    print(num1 / num2)
except:
    print("Error")
finally:
    print("final calculation")
