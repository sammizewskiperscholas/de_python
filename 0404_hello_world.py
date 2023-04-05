import random

print("Hello World")

x= 1+2+3+4
y= 3
y= 5
name= 'Sammi'
print(x)

i= 100 
print(i)

for i in range(1,5):
    print(i)

print("This is outside of the for loop " + str(i))

name_id= id(name)
type_var= type(name)

print(name_id, type_var)
print(id(name), type(name))


friends= ['sammi', 'ben']
for friend in friends:
    print(friend)
    print("outer loop")
    for letter in friend:
        print("inner loop")
        print(letter)

def convert_seconds(seconds):
    hours= seconds // 3600
    minutes= (seconds - hours * 3600) // 60
    remaining_seconds= seconds - hours * 3600 - minutes * 60
    print(hours, minutes, remaining_seconds)
    return hours, minutes, remaining_seconds


return_statement= convert_seconds(5000)
hours, minutes, remaing_seconds= convert_seconds(5000)
#print(hours)
#print(minutes)
#print(remaining_seconds)
#print(type(hours))
print(return_statement)
print(type(return_statement))

print(globals())


favorite_number= 9

def testing_scope():
    x= "cat"
    y= "dog"
    print("My favorite number is "+ str(favorite_number))
    print(locals())

    #return x
    def new_local_scope():
        z="elephant"
        print("We are in the new_local_scope")
        x=150
        print(x, y, z, favorite_number)
        print(locals())
        #y="doggy"
        return x
    x= new_local_scope()
    print(x)
    print(y)
    return x

cat= testing_scope()


print(help(print))

#I am adding a test comment

print("Testing 123")

print("Making a change")

print("I am making a change to the file")    

def new_func():
    print("new function")
