import math

a = int(input("What is a? "))
b = int(input("What is b? "))
c = int(input("What is c? "))

delta = b * b - (4 * a * c)

if delta == 0:
    print("There is one solution, sir.")
    solution = -b / (2 * a)
    print("Solution:", solution)
elif delta > 0:
    print("There are two solutions, sir.")
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print("The first solution is:", x1)
    print("The second solution is:", x2)
else:
    print("There is no solution for this equation, sir.")