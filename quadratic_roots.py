import cmath
a=int(input("Enter values of a"))

b=int(input("Enter values of b"))

c=int(input("Enter values of c"))

D=(b**2)-(4*a*c)

print("Root 1 (+ve root) : ", ((-b)+(cmath.sqrt(D)))/(2*a),"\nRoot 2 (-ve root) : ",((+b)+(cmath.sqrt(D)))/(2*a))