import sympy as sym
import numpy as np

# Define symbols
q1, q2, q3, a1, a2, b1, b2, b3, c1, c2, n = sym.symbols('q1 q2 q3 a1 a2 b1 b2 b3 c1 c2 n')

# Define parameters
#alpha = sym.Symbol('alpha')
#cost = sym.Symbol('cost')
#s = sym.Symbol('s')
#each time you change network also change:
#prices (depending on the demand)
#costs (depending on the technologies)
#utility (depending on the demand)
#name in the graph (name of the network and substiution level)

alpha=10
cost=5
s=0.5



# Define profit functions
P1 = alpha - s*q2 - q1
P2 = alpha - s*q1 - s*q3 - q2
P3 = alpha - s*q2 - q3

C1 = cost - a1 - a2 - n*b1 - n*b2 - n*c1
C2 = cost - b1 - b2 - b3 - n*a1 - n*a2 - n*c1
C3 = cost - c1 - c2 - n*a1 - n*b1

prof1 = (P1-C1)*q1 - 4*a1**2 - 4*a2**2
prof2 = (P2-C2)*q2 - 6*b1**2 - 6*b2**2 - 6*b3**2
prof3 = (P3-C3)*q3 - 4*c1**2 - 4*c2**2

# Take derivatives
dq1 = sym.diff(prof1, q1)
dq2 = sym.diff(prof2, q2)
dq3 = sym.diff(prof3, q3)

# Set derivatives to 0 and solve for q1, q2, q3
soln = sym.solve((dq1, dq2, dq3), (q1, q2, q3))

# Print optimal values of q1, q2, q3
print("Optimal value of q1:", soln[q1])
print("Optimal value of q2:", soln[q2])
print("Optimal value of q3:", soln[q3])


p1 = P1.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3]})
p2 = P2.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3]})
p3 = P3.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3]})


co1 = C1.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3]})
co2 = C2.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3]})
co3 = C3.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3]})


Prof1 = (p1 - co1)*soln[q1] - 4*a1**2 - 4*a2**2
Prof2 = (p2 - co2)*soln[q2] - 6*b1**2 - 6*b2**2 - 6*b3**2
Prof3 = (p3 - co3)*soln[q3] - 4*c1**2 - 4*c2**2
Utility= alpha*(soln[q1]) - ((soln[q1])**2)/2 - s*((soln[q1])*(soln[q2])) - s*((soln[q1])*(soln[q3])) - ((p1)*(soln[q1])) + alpha*(soln[q2]) - ((soln[q2])**2)/2 - s*((soln[q2])*(soln[q1])) - s*((soln[q2])*(soln[q3])) - ((p2)*(soln[q2])) + alpha*(soln[q3]) - ((soln[q3])**2)/2 - s*((soln[q3])*(soln[q1])) - s*((soln[q3])*(soln[q2])) - ((p3)*(soln[q3])) 


print("Profits with optimal quantities for firm 1:", Prof1)
print("Profits with optimal quantities for firm 2:", Prof2)
print("Profits with optimal quantities for firm 3:", Prof3)


# Compute the second derivative of the function with respect to a1, a2
f_double_prime_Prof1_a1 = Prof1.diff(a1, 2)
f_double_prime_Prof1_a2 = Prof1.diff(a2, 2)

# Compute the second derivative of the function with respect to b1, b2, b3
f_double_prime_Prof2_b1 = Prof2.diff(b1, 2)
f_double_prime_Prof2_b2 = Prof2.diff(b2, 2)
f_double_prime_Prof2_b3 = Prof2.diff(b3, 2)

# Compute the second derivative of the function with respect to c1, c2
f_double_prime_Prof3_c1 = Prof3.diff(c1, 2)
f_double_prime_Prof3_c2 = Prof3.diff(c2, 2)



# Values of n to check for concavity
n_values = np.arange(0, 1.01, 0.01)

# Check concavity for each value of n
for n_val in n_values:
    # Substitute n with the current value
    f_double_prime_Prof1_a1_n = f_double_prime_Prof1_a1.subs(n, n_val)
    f_double_prime_Prof1_a2_n = f_double_prime_Prof1_a2.subs(n, n_val)
    f_double_prime_Prof2_b1_n = f_double_prime_Prof2_b1.subs(n, n_val)
    f_double_prime_Prof2_b2_n = f_double_prime_Prof2_b2.subs(n, n_val)
    f_double_prime_Prof2_b3_n = f_double_prime_Prof2_b3.subs(n, n_val)
    f_double_prime_Prof3_c1_n = f_double_prime_Prof3_c1.subs(n, n_val)
    f_double_prime_Prof3_c2_n = f_double_prime_Prof3_c2.subs(n, n_val)

    # Check if the second derivatives are non-positive
    if (f_double_prime_Prof1_a1_n.is_nonpositive and f_double_prime_Prof1_a2_n.is_nonpositive
            and f_double_prime_Prof2_b1_n.is_nonpositive and f_double_prime_Prof2_b2_n.is_nonpositive
            and f_double_prime_Prof2_b3_n.is_nonpositive and f_double_prime_Prof3_c1_n.is_nonpositive
            and f_double_prime_Prof3_c2_n.is_nonpositive):
        print(f"All functions are concave for n = {n_val}")
    else:
        print(f"Some functions are not concave for n = {n_val}")
        
        

# define first derivatives of the profits with respect to a1, a2, b1, b2, b3, c1, and c2
f_Prof1_a1 = Prof1.diff(a1)
f_Prof1_a2 = Prof1.diff(a2)
f_Prof2_b1 = Prof2.diff(b1)
f_Prof2_b2 = Prof2.diff(b2)
f_Prof2_b3 = Prof2.diff(b3)
f_Prof3_c1 = Prof3.diff(c1)
f_Prof3_c2 = Prof3.diff(c2)

# set first derivatives to zero and solve for a1, a2, b1, b2, b3, c1, and c2
eq1=f_Prof1_a1
eq2=f_Prof1_a2
eq3=f_Prof2_b1
eq4=f_Prof2_b2
eq5=f_Prof2_b3
eq6=f_Prof3_c1
eq7=f_Prof3_c2

# Solve equations and store results
solutions = sym.solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7), (a1,a2,b1,b2,b3,c1,c2))

A1 = solutions[a1]
A2 = solutions[a2]
B1 = solutions[b1]
B2 = solutions[b2]
B3 = solutions[b3]
C1 = solutions[c1]
C2 = solutions[c2]

print("Solutions for a1,a2,b1,b2,b3,c1,c2:")
print("A1:", A1)
print("A2:", A2)
print("B1:", B1)
print("B2:", B2)
print("B3:", B3)
print("C1:", C1)
print("C2:", C2)


n = sym.symbols('n')
n_values = np.array([0, 0.2, 0.4, 0.5, 0.8, 1])

for n_val in n_values:
    print("For n =", n_val)
    print("A1 =", A1.subs(n, n_val))
    print("A2 =", A2.subs(n, n_val))
    print("B1 =", B1.subs(n, n_val))
    print("B2 =", B2.subs(n, n_val))
    print("B3 =", B3.subs(n, n_val))
    print("C1 =", C1.subs(n, n_val))
    print("C2 =", C2.subs(n, n_val))
    

##########################################################


import numpy as np
import sympy as sym

# Define your 8 variables as symbolic expressions
n, A1, A2, B1, B2, B3, C1, C2 = sym.symbols('n A1 A2 B1 B2 B3 C1 C2')

# Define your function as the sum of 4 symbolic expressions

Prof1 = (p1 - co1)*soln[q1] - 4*a1**2 - 4*a2**2
Prof1_rep = Prof1.subs(a1, solutions[a1]).subs(a2, solutions[a2]).subs(b1, solutions[b1]).subs(b2, solutions[b2]).subs(b3, solutions[b3]).subs(c1, solutions[c1]).subs(c2, solutions[c2].subs(A1, solutions[a1]).subs(A2, solutions[a2]).subs(B1, solutions[b1]).subs(B2, solutions[b2]).subs(B3, solutions[b3]).subs(C1, solutions[c1]).subs(C2, solutions[c2]))     

Prof2 = (p2 - co2)*soln[q2] - 6*b1**2 - 6*b2**2 - 6*b3**2
Prof2_rep = Prof2.subs(a1, solutions[a1]).subs(a2, solutions[a2]).subs(b1, solutions[b1]).subs(b2, solutions[b2]).subs(b3, solutions[b3]).subs(c1, solutions[c1]).subs(c2, solutions[c2].subs(A1, solutions[a1]).subs(A2, solutions[a2]).subs(B1, solutions[b1]).subs(B2, solutions[b2]).subs(B3, solutions[b3]).subs(C1, solutions[c1]).subs(C2, solutions[c2]))

Prof3 = (p3 - co3)*soln[q3] - 4*c1**2 - 4*c2**2
Prof3_rep = Prof3.subs(a1, solutions[a1]).subs(a2, solutions[a2]).subs(b1, solutions[b1]).subs(b2, solutions[b2]).subs(b3, solutions[b3]).subs(c1, solutions[c1]).subs(c2, solutions[c2].subs(A1, solutions[a1]).subs(A2, solutions[a2]).subs(B1, solutions[b1]).subs(B2, solutions[b2]).subs(B3, solutions[b3]).subs(C1, solutions[c1]).subs(C2, solutions[c2]))

Utility= alpha*(soln[q1]) - ((soln[q1])**2)/2 - s*((soln[q1])*(soln[q2])) - ((p1)*(soln[q1])) + alpha*(soln[q2]) - ((soln[q2])**2)/2 - s*((soln[q2])*(soln[q1])) - s*((soln[q2])*(soln[q3])) - ((p2)*(soln[q2])) + alpha*(soln[q3]) - ((soln[q3])**2)/2 - s*((soln[q3])*(soln[q2])) - ((p3)*(soln[q3]))
Utility_rep= Utility.subs(a1, solutions[a1]).subs(a2, solutions[a2]).subs(b1, solutions[b1]).subs(b2, solutions[b2]).subs(b3, solutions[b3]).subs(c1, solutions[c1]).subs(c2, solutions[c2].subs(A1, solutions[a1]).subs(A2, solutions[a2]).subs(B1, solutions[b1]).subs(B2, solutions[b2]).subs(B3, solutions[b3]).subs(C1, solutions[c1]).subs(C2, solutions[c2]))

f = Prof1_rep + Prof2_rep + Prof3_rep + Utility_rep
f_rep = f.subs(a1, solutions[a1]).subs(a2, solutions[a2]).subs(b1, solutions[b1]).subs(b2, solutions[b2]).subs(b3, solutions[b3]).subs(c1, solutions[c1]).subs(c2, solutions[c2].subs(A1, solutions[a1]).subs(A2, solutions[a2]).subs(B1, solutions[b1]).subs(B2, solutions[b2]).subs(B3, solutions[b3]).subs(C1, solutions[c1]).subs(C2, solutions[c2]))     
print(f_rep)

from sympy import simplify
f_simp=simplify(f_rep)
print(f_simp)

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym


def evaluate_f(n):
    return f_simp.subs({'n': n})
n_vals = np.arange(0, 1.01, 0.01)
f_vals = np.array([evaluate_f(n) for n in n_vals])
f_max_val = np.max(f_vals)
n_max = n_vals[np.argmax(f_vals)]
plt.plot(n_vals, f_vals)
plt.title('Network D | b=0.5')
plt.xlabel('γ')
plt.ylabel('Welfare')
plt.text(0.47, f_max_val -4.5, f"Maximum Welfare: {f_max_val:.2f} at γ={n_max:.2f}", ha='center')
plt.show()