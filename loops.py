def create_username(username):
    if len(username) <= 5:
        print("Invalid username. Username must be at least 5 charachters long")
    elif len(username) > 15: 
        print("Invalid username. Username must be at least 15 charachters long")
    else:
        print("You have created a valid username")

create_username("sammi")

def check_nums(num1, num2):
    if num1 > num2:
        return True
    return False

result= check_nums(10, 3)
#print(result)

#print(check_nums(3,10))

def true_or_false(result):
    if result == True:
        print("The result is True")
        return
    #if result == False:
    print("The result is False")

return_test= true_or_false(result)
#print(return_test)


if return_test == None:
    print("False statement")
else:
    print("True statement")


#x= 5
def greater_than_0(num):
    while num > 0:
        num = num-1
        if num == 2:
            continue
            #break
        #print("Not there yet, num= " + str(num))
    print("num=" + str(num))


greater_than_0(5)

a= [1, 2]
b= [4, 5]

for i in a:
    for j in b:
        print(i, j)

friends= [["25", 14, 13], "25"]
for friend in friends:
    print(friend)
    print("outer loop")
    for letter in friend:
        print("inner loop")
        print(letter)
        for alpha in letter:
            print(alpha)

def newfunc():
    print("new_function")