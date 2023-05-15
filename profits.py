from sympy import symbols, simplify

# define the variables
a, b, c, n = symbols("a b c n")

# define the expression
expr=((600 + a*(210*n - 90) + b*(135*n - 135) + c*(450 - 90*n))/420)*(-0.820238095238095*a*n - 0.214285714285714*a - 0.678571428571429*b*n - 0.321428571428571*b - 0.214285714285714*c*n - 0.928571428571428*c + 6.23214285714286) - (5 - 2*c - a - b)*((600 + a*(210*n - 90) + b*(135*n - 135) + c*(450 - 90*n))/420) - 2*c**2


simplified_expr = simplify(expr)

print(simplified_expr)
