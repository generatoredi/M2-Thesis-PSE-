import sympy as sp

a, b, c, n = sp.symbols('a b c n')

# Define the expression (profits, this will go to the system)
expr=expr=(0.0785714285714287*a*n - 0.314285714285714*a - 0.735714285714286*b*n + 0.0785714285714287*b + 0.0785714285714287*c*n - 0.421428571428572*c + 6.71428571428572)*(0.0357142857142857*a*n - 0.142857142857143*a + 0.392857142857143*b*n + 0.0357142857142857*b + 0.0357142857142857*c*n + 0.535714285714286*c + 2.14285714285714) - (5 - (c) - ((n)*(b)))*(0.0357142857142857*a*n - 0.142857142857143*a + 0.392857142857143*b*n + 0.0357142857142857*b + 0.0357142857142857*c*n + 0.535714285714286*c + 2.14285714285714) - 4*c**2



# calculate the first derivative wrt a,b,c (change everytime)
d_expr = sp.diff(expr, c)


print("first derivative with respect to c is:")
print(d_expr)
