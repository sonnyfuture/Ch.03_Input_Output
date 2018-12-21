'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Eddie H. Agic
1. Write a line of code that will print your name.
'''

print("Eddie")

'''
2. Write a program that asks someone for their name and then prints their name to the screen?
'''

name = input("Your Name: ")
print(name)

'''
3. Predict the output of the following lines of code and then test them? Write down your prediction and the output.
print (17/9) - PREDICTION: Will do division
print (17//9) - PREDICTION: Will floor
print (17%9) - PREDICTION: Will modulus
'''

print(17/9)
print(17//9)
print(17%9)

#I was correct on all of them. =)

'''
4. Write a a program where a user enters a base and height and you print the area of a triangle.
'''

height=int(input("Enter Height: "))
base=int(input("Enter Base: "))
print((height*base)/2)

'''
5. Change this program so it works.
A=May the Force be with you!
print(a)
'''

force_message=("May the Force be with you!")
print(force_message)


'''
6. Write a line of code that will ask the user for the length of a square's
side and then print the area of the square
'''

side=int(input("Side Length: "))
print(side**2)

'''7. Ask a user for the length of radii of an ellipse and then print its area. 
Area=pi*a*b where a and b are the lengths of the major radii.
'''

radii_a=int(input("Radius 1: "))
radii_b=int(input("Radius 2: "))
print(3.14*radii_a*radii_b)

'''
8. Ask a user for moles, volume and temperature of a gas and print out the pressure. PV=nRT where n is the number of moles, T is the absolute temperature, V is the
volume, and R is the gas constant 8.3144.
'''

moles=int(input("Mole(s): "))
volume=int(input("Volume: "))
temperature=int(input("Temperature: "))
print("P=",(moles*(8.3144)*temperature)/volume)

'''
9. Ask a user for an integer and then print the square root.
INCORRECT: Your code just divides by 2'''

integer=int(input("Insert Integer: "))
print(integer**(1/2))

'''
10. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. Ask the user for mass and acceleration
and then print out the Force on one line and "Get it?" on the next.
'''

mass=int(input("Mass: "))
acceleration=int(input("Acceleration: "))
print("F=",mass*acceleration)
print("Get it?")
