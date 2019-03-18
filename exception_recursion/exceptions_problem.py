# Universal Gravity Calculator (15pts)
# In physics, the force of gravity between two objects can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters


# Make a calculator that does all of the following 
# (3pts) takes the inputs for mass 1, mass 2.and distance between the two objects (m1, m2, and r) 
# (4pts) contains exceptions for any potential errors (value and dividebyzero).
# (3pts) keeps asking for inputs until they are valid (see while loop from notes)
# (4pts) calculate the force of gravity in Newtons and print the result to the user in scientific notation to two decimals.


G = 6.67e-11
done = False

while not done:
    try:
        mass_1 = float(input("Put in the mass of the first object in kilograms. "))/1000
        done = True
    except ValueError:
        print("That is not a real number")

done = False

while not done:
    try:
        mass_2 = float(input("Put in the mass of the second object in kilograms. "))/1000
        done = True
    except ValueError:
        print("That is not a real number")

done = False

while not done:
    try:
        radius = float(input("What is the radius between the two objects in meters? "))
        force = G*mass_1*mass_2/(radius**2)
        rounded_force = round(force)
        print("The gravity between the two objects is {:0.2e}.".format(force))
        done = True
    except ValueError:
        print("That is not a real number.")
    except ZeroDivisionError:
        print("The two objects cannot be in the same place")
