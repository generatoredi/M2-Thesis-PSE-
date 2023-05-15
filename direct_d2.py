import sympy as sp

a, b, c, n = sp.symbols('a b c n')

#write the normal expression (not the first derivative)
d_expr= -2*c**2 + (a + b + 2*c - 5)*(2*a*(7*n - 3) + 9*b*(n - 1) - 6*c*(n - 5) + 40)/28 - (2*a*(7*n - 3) + 9*b*(n - 1) - 6*c*(n - 5) + 40)*(0.820238095238095*a*n + 0.214285714285714*a + 0.678571428571429*b*n + 0.321428571428571*b + 0.214285714285714*c*n + 0.928571428571428*c - 6.23214285714286)/28

# calculate the second derivative with respect to a,b,c (change)
d2_expr = sp.diff(d_expr, c, 2)

print("Second derivative of the function with respect to c:")
print(d2_expr)
