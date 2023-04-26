#x = 10
#if x > 5:
    #raise Exception('x should not exceed 5. The value of x was {}'.format(x))


#assert x >= 5, 'x should not exceed 5. The value of x was {}'.format(x)

#print("Hello World")

def sum(num1, num2):
    total= num1 + num2
    return total

answer= sum(2,2)
#print(answer)

def modify_x():
    assert x <= 5, 'x should not exceed 5. The value of x was {}'.format(x)
    print('x is being modified')
    print(x)

"""try: 
    x=50
    modify_x()
except AssertionError as error:
    print(error)
    print('modify_x() function was not successfully executed')

print("Hello World")"""

try: 
    f= open('my_file1.txt')
except FileNotFoundError as fnf_error:
    print(fnf_error)
    print('file does not exist')

try:
    x=4
    modify_x()
except AssertionError as error:
    print(error)
    print('modify_x() function was not successfully executed')
else:
    print("everything looking good")
finally:
    print("We did it!")