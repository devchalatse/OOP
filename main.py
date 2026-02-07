class Calculator():
    def addition(x, y):
        return x + y
    
    def subtraction(x, y):
        return x - y
    
    def divide(x, y):
        return x / y
    
    def modulus(x, y):
        return x % y
    

num = Calculator

y = int(input('Enter the value of y: '))
x = int(input('Enter the value of x: '))

total = x + y
total2 = x - y
total3 = x / y
total4 = x % y

print(f'{x} + {y} = {total}')
print(f'{x} - {y} = {total2}')
print(f'{x} / {y} = {total3}')
print(f'{x} % {y} = {total4}')


