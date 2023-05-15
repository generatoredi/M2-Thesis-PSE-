from sympy import symbols, solve

# Define the variables
a1, a2, b1, b2, b3, c1, c2, q1, q2, q3, n, a, b, c = symbols('a1 a2 b1 b2 b3 c1 c2 q1 q2 q3 n a b c')

# Define the equations
eq1=(5 - 0.8*q2 - 0.8*q3 + a +  n*b )/2 - q1

eq2=(5 - 0.8*q1 + b +   n*a +  n*c)/2 - q2

eq3=(5 - 0.8*q1 + c + n*b)/2 - q3


# Solve for q1 in terms of q2, q3
solutions = solve([eq1, eq2, eq3], [q1, q2, q3], dict=True)
q1_expr = solutions[0][q1]

# Make sure that q1 is not a function of q2 or q3
if q2 in q1_expr.free_symbols or q3 in q1_expr.free_symbols:
    print("Error: q1 depends on q2 or q3.")
else:
    print("q1 =", q1_expr)

# Similarly, solve for q2 and q3 in terms of q1, and make sure that they don't depend on q1
q2_expr = solve([eq1, eq2, eq3], [q1, q2, q3], dict=True)[0][q2]
q3_expr = solve([eq1, eq2, eq3], [q1, q2, q3], dict=True)[0][q3]
if q1 in q2_expr.free_symbols or q3 in q2_expr.free_symbols:
    print("Error: q2 depends on q1 or q3.")
else:
    print("q2 =", q2_expr)
if q1 in q3_expr.free_symbols or q2 in q3_expr.free_symbols:
    print("Error: q3 depends on q1 or q2.")
else:
    print("q3 =", q3_expr)
