import sympy as sym
import numpy as np

# Define symbols
q1, q2, q3, q4, q5, q6, q7, q8, a1, b2, c3, d4, e1, e5, e6, e7, e8, f2, f5, f6, f7, f8, g3, g5, g6, g7, g8, h4, h5, h6, h7, h8, n = sym.symbols('q1 q2 q3 q4 q5 q6 q7 q8 a1 b2 c3 d4 e1 e5 e6 e7 e8 f2 f5 f6 f7 f8 g3 g5 g6 g7 g8 h4 h5 h6 h7 h8 n')

# Define parameters
#alpha = sym.Symbol('alpha')
#cost = sym.Symbol('cost')
#s = sym.Symbol('s')
#each time you change network also change prices, costs, utility
alpha=10
cost=5
s=0.5


# Define profit functions
P1 = alpha - s*q5 - q1
P2 = alpha - s*q6 - q2
P3 = alpha - s*q7 - q3
P4 = alpha - s*q8 - q4
P5 = alpha - s*q1 - s*q6 - s*q7 - s*q8 - q5
P6 = alpha - s*q2 - s*q5 - s*q7 - s*q8 - q6
P7 = alpha - s*q3 - s*q5 - s*q6 - s*q8 - q7
P8 = alpha - s*q4 - s*q5 - s*q6 - s*q7 - q8



C1 = cost - a1 - n*e1
C2 = cost - b2 - n*f2
C3 = cost - c3 - n*g3
C4 = cost - d4 - n*h4
C5 = cost - e5 - e1 - n*a1 - e6 - e7 - e8 - n*f5 - n*f6 - n*f7 - n*f8 - n*g5 - n*g6 - n*g7 - n*g8 - n*h5 - n*h6 - n*h7 - n*h8
C6 = cost - f6 - f2 - n*b2 - f5 - f7 - f8 - n*e5 - n*e6 - n*e7 - n*e8 - n*g5 - n*g6 - n*g7 - n*g8 - n*h5 - n*h6 - n*h7 - n*h8
C7 = cost - g7 - g3 - n*c3 - g5 - g6 - g8 - n*f5 - n*f6 - n*f7 - n*f8 - n*e5 - n*e6 - n*e7 - n*e8 - n*h5 - n*h6 - n*h7 - n*h8
C8 = cost - h8 - h4 - n*d4 - h5 - h6 - h7 - n*f5 - n*f6 - n*f7 - n*f8 - n*g5 - n*g6 - n*g7 - n*g8 - n*e5 - n*e6 - n*h7 - n*e8




prof1 = (P1-C1)*q1 - 2*a1**2
prof2 = (P2-C2)*q2 - 2*b2**2
prof3 = (P3-C3)*q3 - 2*c3**2
prof4 = (P4-C4)*q4 - 2*d4**2
prof5 = (P5-C5)*q5 - 10*e1**2 - 10*e5**2 - 10*e6**2 - 10*e7**2 - 10*e8**2
prof6 = (P6-C6)*q6 - 10*f2**2 - 10*f5**2 - 10*f6**2 - 10*f7**2 - 10*f8**2
prof7 = (P7-C7)*q7 - 10*g3**2 - 10*g5**2 - 10*g6**2 - 10*g7**2 - 10*g8**2
prof8 = (P8-C8)*q8 - 10*h4**2 - 10*h5**2 - 10*h6**2 - 10*h7**2 - 10*h8**2




# Take derivatives
dq1 = sym.diff(prof1, q1)
dq2 = sym.diff(prof2, q2)
dq3 = sym.diff(prof3, q3)
dq4 = sym.diff(prof4, q4)
dq5 = sym.diff(prof5, q5)
dq6 = sym.diff(prof6, q6)
dq7 = sym.diff(prof7, q7)
dq8 = sym.diff(prof8, q8)


# Set derivatives to 0 and solve for q1, q2, q3
soln = sym.solve((dq1, dq2, dq3, dq4, dq5, dq6, dq7, dq8), (q1, q2, q3, q4, q5, q6, q7, q8))

# Print optimal values of q1, q2, q3
print("Optimal value of q1:", soln[q1])
print("Optimal value of q2:", soln[q2])
print("Optimal value of q3:", soln[q3])
print("Optimal value of q4:", soln[q4])
print("Optimal value of q5:", soln[q5])
print("Optimal value of q6:", soln[q6])
print("Optimal value of q7:", soln[q7])
print("Optimal value of q8:", soln[q8])


p1 = P1.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3], q4: soln[q4], q5: soln[q5], q6: soln[q6], q7: soln[q7], q8: soln[q8]})
p2 = P2.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3], q4: soln[q4], q5: soln[q5], q6: soln[q6], q7: soln[q7], q8: soln[q8]})
p3 = P3.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3], q4: soln[q4], q5: soln[q5], q6: soln[q6], q7: soln[q7], q8: soln[q8]})
p4 = P4.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3], q4: soln[q4], q5: soln[q5], q6: soln[q6], q7: soln[q7], q8: soln[q8]})
p5 = P5.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3], q4: soln[q4], q5: soln[q5], q6: soln[q6], q7: soln[q7], q8: soln[q8]})
p6 = P6.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3], q4: soln[q4], q5: soln[q5], q6: soln[q6], q7: soln[q7], q8: soln[q8]})
p7 = P7.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3], q4: soln[q4], q5: soln[q5], q6: soln[q6], q7: soln[q7], q8: soln[q8]})
p8 = P8.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3], q4: soln[q4], q5: soln[q5], q6: soln[q6], q7: soln[q7], q8: soln[q8]})


co1 = C1.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3], q4: soln[q4], q5: soln[q5], q6: soln[q6], q7: soln[q7], q8: soln[q8]})
co2 = C2.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3], q4: soln[q4], q5: soln[q5], q6: soln[q6], q7: soln[q7], q8: soln[q8]})
co3 = C3.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3], q4: soln[q4], q5: soln[q5], q6: soln[q6], q7: soln[q7], q8: soln[q8]})
co4 = C4.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3], q4: soln[q4], q5: soln[q5], q6: soln[q6], q7: soln[q7], q8: soln[q8]})
co5 = C5.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3], q4: soln[q4], q5: soln[q5], q6: soln[q6], q7: soln[q7], q8: soln[q8]})
co6 = C6.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3], q4: soln[q4], q5: soln[q5], q6: soln[q6], q7: soln[q7], q8: soln[q8]})
co7 = C7.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3], q4: soln[q4], q5: soln[q5], q6: soln[q6], q7: soln[q7], q8: soln[q8]})
co8 = C8.subs({q1: soln[q1], q2: soln[q2], q3: soln[q3], q4: soln[q4], q5: soln[q5], q6: soln[q6], q7: soln[q7], q8: soln[q8]})


Prof1 = (p1 - co1)*soln[q1] - 2*a1**2
Prof2 = (p2 - co2)*soln[q2] - 2*b2**2
Prof3 = (p3 - co3)*soln[q3] - 2*c3**2
Prof4 = (p4 - co4)*soln[q4] - 2*d4**2
Prof5 = (p5 - co5)*soln[q5] - 10*e1**2 - 10*e5**2 - 10*e6**2 - 10*e7**2 - 10*e8**2
Prof6 = (p6 - co6)*soln[q6] - 10*f2**2 - 10*f5**2 - 10*f6**2 - 10*f7**2 - 10*f8**2
Prof7 = (p7 - co7)*soln[q7] - 10*g3**2 - 10*g5**2 - 10*g6**2 - 10*g7**2 - 10*g8**2
Prof8 = (p8 - co8)*soln[q8] - 10*h4**2 - 10*h5**2 - 10*h6**2 - 10*h7**2 - 10*h8**2



#########################################################

Utility= alpha*(soln[q1]) - ((soln[q1])**2)/2 - s*((soln[q1])*(soln[q8])) - ((p1)*(soln[q1])) + alpha*(soln[q2]) - ((soln[q2])**2)/2 - s*((soln[q2])*(soln[q8])) - ((p2)*(soln[q2])) + alpha*(soln[q3]) - ((soln[q3])**2)/2 - s*((soln[q3])*(soln[q8])) - ((p3)*(soln[q3])) + alpha*(soln[q4]) - ((soln[q4])**2)/2 - s*((soln[q4])*(soln[q8])) - ((p4)*(soln[q4])) + alpha*(soln[q5]) - ((soln[q5])**2)/2 - s*((soln[q5])*(soln[q8])) - ((p5)*(soln[q5])) + alpha*(soln[q6]) - ((soln[q6])**2)/2 - s*((soln[q6])*(soln[q8])) - ((p6)*(soln[q6]))  + alpha*(soln[q7]) - ((soln[q7])**2)/2 - s*((soln[q7])*(soln[q8])) - ((p7)*(soln[q7])) + alpha*(soln[q8]) - ((soln[q8])**2)/2 - s*((soln[q8])*(soln[q1])) - s*((soln[q8])*(soln[q2])) - s*((soln[q8])*(soln[q3])) - s*((soln[q8])*(soln[q4])) - s*((soln[q8])*(soln[q5])) - s*((soln[q8])*(soln[q6])) - s*((soln[q8])*(soln[q7]))  - ((p8)*(soln[q8])) 


print("Profits with optimal quantities for firm 1:", Prof1)
print("Profits with optimal quantities for firm 2:", Prof2)
print("Profits with optimal quantities for firm 3:", Prof3)
print("Profits with optimal quantities for firm 4:", Prof4)
print("Profits with optimal quantities for firm 5:", Prof5)
print("Profits with optimal quantities for firm 6:", Prof6)
print("Profits with optimal quantities for firm 7:", Prof7)
print("Profits with optimal quantities for firm 8:", Prof8)



# Compute the second derivative of the function with respect to a1, a2
f_double_prime_Prof1_a1 = Prof1.diff(a1, 2)
f_double_prime_Prof2_b2 = Prof2.diff(b2, 2)
f_double_prime_Prof3_c3 = Prof3.diff(c3, 2)
f_double_prime_Prof4_d4 = Prof4.diff(d4, 2)
f_double_prime_Prof5_e1 = Prof5.diff(e1, 2)
f_double_prime_Prof5_e5 = Prof5.diff(e5, 2)
f_double_prime_Prof5_e6 = Prof5.diff(e6, 2)
f_double_prime_Prof5_e7 = Prof5.diff(e7, 2)
f_double_prime_Prof5_e8 = Prof5.diff(e8, 2)
f_double_prime_Prof6_f2 = Prof5.diff(f2, 2)
f_double_prime_Prof6_f5 = Prof6.diff(f5, 2)
f_double_prime_Prof6_f6 = Prof6.diff(f6, 2)
f_double_prime_Prof6_f7 = Prof6.diff(f7, 2)
f_double_prime_Prof6_f8 = Prof6.diff(f8, 2)
f_double_prime_Prof7_g3 = Prof7.diff(g3, 2)
f_double_prime_Prof7_g5 = Prof7.diff(g5, 2)
f_double_prime_Prof7_g6 = Prof7.diff(g6, 2)
f_double_prime_Prof7_g7 = Prof7.diff(g7, 2)
f_double_prime_Prof7_g8 = Prof7.diff(g8, 2)
f_double_prime_Prof8_h4 = Prof8.diff(h4, 2)
f_double_prime_Prof8_h5 = Prof8.diff(h5, 2)
f_double_prime_Prof8_h6 = Prof8.diff(h6, 2)
f_double_prime_Prof8_h7 = Prof8.diff(h7, 2)
f_double_prime_Prof8_h8 = Prof8.diff(h8, 2)

# Values of n to check for concavity
n_values = np.arange(0, 1.01, 0.01)

# Check concavity for each value of n
for n_val in n_values:
    # Substitute n with the current value   .subs(n, n_val)
    f_double_prime_Prof1_a1_n = f_double_prime_Prof1_a1.subs({n: n_val})
    f_double_prime_Prof2_b2_n = f_double_prime_Prof2_b2.subs({n: n_val})
    f_double_prime_Prof3_c3_n = f_double_prime_Prof3_c3.subs({n: n_val})
    f_double_prime_Prof4_d4_n = f_double_prime_Prof4_d4.subs({n: n_val})
    f_double_prime_Prof5_e1_n = f_double_prime_Prof5_e1.subs({n: n_val})
    f_double_prime_Prof5_e5_n = f_double_prime_Prof5_e5.subs({n: n_val})
    f_double_prime_Prof5_e6_n = f_double_prime_Prof5_e6.subs({n: n_val})
    f_double_prime_Prof5_e7_n = f_double_prime_Prof5_e7.subs({n: n_val})
    f_double_prime_Prof5_e8_n = f_double_prime_Prof5_e8.subs({n: n_val})
    f_double_prime_Prof6_f2_n = f_double_prime_Prof6_f2.subs({n: n_val})
    f_double_prime_Prof6_f5_n = f_double_prime_Prof6_f5.subs({n: n_val})
    f_double_prime_Prof6_f6_n = f_double_prime_Prof6_f6.subs({n: n_val})
    f_double_prime_Prof6_f7_n = f_double_prime_Prof6_f7.subs({n: n_val})
    f_double_prime_Prof6_f8_n = f_double_prime_Prof6_f8.subs({n: n_val})
    f_double_prime_Prof7_g3_n = f_double_prime_Prof7_g3.subs({n: n_val})
    f_double_prime_Prof7_g5_n = f_double_prime_Prof7_g5.subs({n: n_val})
    f_double_prime_Prof7_g6_n = f_double_prime_Prof7_g6.subs({n: n_val})
    f_double_prime_Prof7_g7_n = f_double_prime_Prof7_g7.subs({n: n_val})
    f_double_prime_Prof7_g8_n = f_double_prime_Prof7_g8.subs({n: n_val})
    f_double_prime_Prof8_h4_n = f_double_prime_Prof8_h4.subs({n: n_val})
    f_double_prime_Prof8_h5_n = f_double_prime_Prof8_h5.subs({n: n_val})
    f_double_prime_Prof8_h6_n = f_double_prime_Prof8_h6.subs({n: n_val})
    f_double_prime_Prof8_h7_n = f_double_prime_Prof8_h7.subs({n: n_val})
    f_double_prime_Prof8_h8_n = f_double_prime_Prof8_h8.subs({n: n_val})
    # Check if the second derivatives are non-positive
    if (f_double_prime_Prof1_a1_n.is_nonpositive and f_double_prime_Prof2_b2_n.is_nonpositive
            and f_double_prime_Prof3_c3_n.is_nonpositive and f_double_prime_Prof4_d4_n.is_nonpositive
            and f_double_prime_Prof5_e1_n.is_nonpositive and f_double_prime_Prof5_e5_n.is_nonpositive
            and f_double_prime_Prof5_e6_n.is_nonpositive and f_double_prime_Prof5_e7_n.is_nonpositive
            and f_double_prime_Prof5_e8_n.is_nonpositive and f_double_prime_Prof6_f5_n.is_nonpositive
            and f_double_prime_Prof6_f2_n.is_nonpositive and f_double_prime_Prof7_g3_n.is_nonpositive
            and f_double_prime_Prof6_f6_n.is_nonpositive and f_double_prime_Prof6_f7_n.is_nonpositive
            and f_double_prime_Prof6_f8_n.is_nonpositive and f_double_prime_Prof7_g5_n.is_nonpositive
            and f_double_prime_Prof7_g6_n.is_nonpositive and f_double_prime_Prof7_g7_n.is_nonpositive
            and f_double_prime_Prof7_g8_n.is_nonpositive and f_double_prime_Prof8_h4_n.is_nonpositive
            and f_double_prime_Prof8_h5_n.is_nonpositive and f_double_prime_Prof8_h6_n.is_nonpositive
            and f_double_prime_Prof8_h7_n.is_nonpositive and f_double_prime_Prof8_h8_n.is_nonpositive):
            
         print(f"All functions are concave for n = {n_val}")
else:
         print(f"Some functions are not concave for n = {n_val}")


        
        

# define first derivatives of the profits with respect to a1, a2, b1, b2, b3, c1, and c2
f_Prof1_a1 = Prof1.diff(a1)
f_Prof2_b2 = Prof2.diff(b2)
f_Prof3_c3 = Prof3.diff(c3)
f_Prof4_d4 = Prof4.diff(d4)
f_Prof5_e1 = Prof5.diff(e1)
f_Prof5_e5 = Prof5.diff(e5)
f_Prof5_e6 = Prof5.diff(e6)
f_Prof5_e7 = Prof5.diff(e7)
f_Prof5_e8 = Prof5.diff(e8)
f_Prof6_f2 = Prof6.diff(f2)
f_Prof6_f5 = Prof6.diff(f5)
f_Prof6_f6 = Prof6.diff(f6)
f_Prof6_f7 = Prof6.diff(f7)
f_Prof6_f8 = Prof6.diff(f8)
f_Prof7_g3 = Prof7.diff(g3)
f_Prof7_g5 = Prof7.diff(g5)
f_Prof7_g6 = Prof7.diff(g6)
f_Prof7_g7 = Prof7.diff(g7)
f_Prof7_g8 = Prof7.diff(g8)
f_Prof8_h4 = Prof8.diff(h4)
f_Prof8_h5 = Prof8.diff(h5)
f_Prof8_h6 = Prof8.diff(h6)
f_Prof8_h7 = Prof8.diff(h7)
f_Prof8_h8 = Prof8.diff(h8)


# set first derivatives to zero and solve for a1, a2, b1, b2, b3, c1, and c2
eq1 = f_Prof1_a1
eq2 = f_Prof2_b2
eq3 = f_Prof3_c3
eq4 = f_Prof4_d4
eq5 = f_Prof5_e1
eq6 = f_Prof5_e5
eq7 = f_Prof5_e6
eq8 = f_Prof5_e7
eq9 = f_Prof5_e8
eq10 = f_Prof6_f2
eq11 = f_Prof6_f5
eq12 = f_Prof6_f6
eq13 = f_Prof6_f7
eq14 = f_Prof6_f8
eq15 = f_Prof7_g3
eq16 = f_Prof7_g5
eq17 = f_Prof7_g6
eq18 = f_Prof7_g7
eq19 = f_Prof7_g8
eq20 = f_Prof8_h4
eq21 = f_Prof8_h5
eq22 = f_Prof8_h6
eq23 = f_Prof8_h7
eq24 = f_Prof8_h8


# Solve equations and store results
solutions = sym.solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, eq11, eq12, eq13, eq14, eq15, eq16, eq17, eq18, eq19, eq20, eq21, eq22, eq23, eq24), (a1, b2, c3, d4, e1, e5, e6, e7, e8, f2, f5, f6, f7, f8, g3, g5, g6, g7, g8, h4, h5, h6, h7, h8))

A1 = solutions[a1]
B2 = solutions[b2]
C3 = solutions[c3]
D4 = solutions[d4]
E1 = solutions[e1]
E5 = solutions[e5]
E6 = solutions[e6]
E7 = solutions[e7]
E8 = solutions[e8]
F2 = solutions[f2]
F5 = solutions[f5]
F6 = solutions[f6]
F7 = solutions[f7]
F8 = solutions[f8]
G3 = solutions[g3]
G5 = solutions[g5]
G6 = solutions[g6]
G7 = solutions[g7]
G8 = solutions[g8]
H4 = solutions[h4]
H5 = solutions[h5]
H6 = solutions[h6]
H7 = solutions[h7]
H8 = solutions[h8]


print("Solutions for a1, b2, c3, d4, e1, e5, e6, e7, e8, f2, f5, f6, f7, f8, g3, g5, g6, g7, g8, h4, h5, h6, h7, h8:")
print("A1:", A1)
print("B2:", B2)
print("C3:", C3)
print("D4:", D4)
print("E1:", E1)
print("E5:", E5)
print("E6:", E6)
print("E7:", E7)
print("E8:", E8)
print("F2:", F2)
print("F5:", F5)
print("F6:", F6)
print("F7:", F7)
print("F8:", F8)
print("G3:", G3)
print("G5:", G5)
print("G6:", G6)
print("G7:", G7)
print("G8:", G8)
print("H4:", H4)
print("H5:", H5)
print("H6:", H6)
print("H7:", H7)
print("H8:", H8)



n = sym.symbols('n')
n_values = np.array([0, 0.2, 0.4, 0.5, 0.8, 1])

for n_val in n_values:
    print("For n =", n_val)
    print("A1 =", A1.subs(n, n_val))
    print("B2 =", B2.subs(n, n_val))
    print("C3 =", C3.subs(n, n_val))
    print("D4 =", D4.subs(n, n_val))
    print("E1 =", E1.subs(n, n_val))
    print("E5 =", E5.subs(n, n_val))
    print("E6 =", E6.subs(n, n_val))
    print("E7 =", E7.subs(n, n_val))
    print("E8 =", E8.subs(n, n_val))
    print("F2 =", F2.subs(n, n_val))
    print("F5 =", F5.subs(n, n_val))
    print("F6 =", F6.subs(n, n_val))
    print("F7 =", F7.subs(n, n_val))
    print("F8 =", F8.subs(n, n_val))
    print("G3 =", G3.subs(n, n_val))
    print("G5 =", G5.subs(n, n_val))
    print("G6 =", G6.subs(n, n_val))
    print("G7 =", G7.subs(n, n_val))
    print("G8 =", G8.subs(n, n_val))
    print("H4 =", H4.subs(n, n_val))
    print("H5 =", H5.subs(n, n_val))
    print("H6 =", H6.subs(n, n_val))
    print("H7 =", H7.subs(n, n_val))
    print("H8 =", H8.subs(n, n_val))



##########################################################


import numpy as np
import sympy as sym


# Define your function as the sum of 4 symbolic expressions
Prof1 = (p1 - co1)*soln[q1] - 2*a1**2
Prof1_rep = Prof1.subs(a1, solutions[a1]).subs(b2, solutions[b2]).subs(c3, solutions[c3]).subs(d4, solutions[d4]).subs(e5, solutions[e5]).subs(f6, solutions[f6]).subs(g7, solutions[g7]).subs(h4, solutions[h4]).subs(h5, solutions[h5]).subs(h6, solutions[h6]).subs(h7, solutions[h7]).subs(h8, solutions[h8]).subs(g3, solutions[g3]).subs(g5, solutions[g5]).subs(g6, solutions[g6]).subs(g8, solutions[g8]).subs(e1, solutions[e1]).subs(e6, solutions[e6]).subs(e7, solutions[e7]).subs(e8, solutions[e8]).subs(f2, solutions[f2]).subs(f5, solutions[f5]).subs(f7, solutions[f7]).subs(f8, solutions[f8])

Prof2 = (p2 - co2)*soln[q2] - 2*b2**2
Prof2_rep = Prof2.subs(a1, solutions[a1]).subs(b2, solutions[b2]).subs(c3, solutions[c3]).subs(d4, solutions[d4]).subs(e5, solutions[e5]).subs(f6, solutions[f6]).subs(g7, solutions[g7]).subs(h4, solutions[h4]).subs(h5, solutions[h5]).subs(h6, solutions[h6]).subs(h7, solutions[h7]).subs(h8, solutions[h8]).subs(g3, solutions[g3]).subs(g5, solutions[g5]).subs(g6, solutions[g6]).subs(g8, solutions[g8]).subs(e1, solutions[e1]).subs(e6, solutions[e6]).subs(e7, solutions[e7]).subs(e8, solutions[e8]).subs(f2, solutions[f2]).subs(f5, solutions[f5]).subs(f7, solutions[f7]).subs(f8, solutions[f8])

Prof3 = (p3 - co3)*soln[q3] - 2*c3**2
Prof3_rep = Prof3.subs(a1, solutions[a1]).subs(b2, solutions[b2]).subs(c3, solutions[c3]).subs(d4, solutions[d4]).subs(e5, solutions[e5]).subs(f6, solutions[f6]).subs(g7, solutions[g7]).subs(h4, solutions[h4]).subs(h5, solutions[h5]).subs(h6, solutions[h6]).subs(h7, solutions[h7]).subs(h8, solutions[h8]).subs(g3, solutions[g3]).subs(g5, solutions[g5]).subs(g6, solutions[g6]).subs(g8, solutions[g8]).subs(e1, solutions[e1]).subs(e6, solutions[e6]).subs(e7, solutions[e7]).subs(e8, solutions[e8]).subs(f2, solutions[f2]).subs(f5, solutions[f5]).subs(f7, solutions[f7]).subs(f8, solutions[f8])

Prof4 = (p4 - co4)*soln[q4] - 2*d4**2
Prof4_rep = Prof4.subs(a1, solutions[a1]).subs(b2, solutions[b2]).subs(c3, solutions[c3]).subs(d4, solutions[d4]).subs(e5, solutions[e5]).subs(f6, solutions[f6]).subs(g7, solutions[g7]).subs(h4, solutions[h4]).subs(h5, solutions[h5]).subs(h6, solutions[h6]).subs(h7, solutions[h7]).subs(h8, solutions[h8]).subs(g3, solutions[g3]).subs(g5, solutions[g5]).subs(g6, solutions[g6]).subs(g8, solutions[g8]).subs(e1, solutions[e1]).subs(e6, solutions[e6]).subs(e7, solutions[e7]).subs(e8, solutions[e8]).subs(f2, solutions[f2]).subs(f5, solutions[f5]).subs(f7, solutions[f7]).subs(f8, solutions[f8])

Prof5 = (p5 - co5)*soln[q5] - 10*e1**2 - 10*e5**2 - 10*e6**2 - 10*e7**2 - 10*e8**2
Prof5_rep = Prof5.subs(a1, solutions[a1]).subs(b2, solutions[b2]).subs(c3, solutions[c3]).subs(d4, solutions[d4]).subs(e5, solutions[e5]).subs(f6, solutions[f6]).subs(g7, solutions[g7]).subs(h4, solutions[h4]).subs(h5, solutions[h5]).subs(h6, solutions[h6]).subs(h7, solutions[h7]).subs(h8, solutions[h8]).subs(g3, solutions[g3]).subs(g5, solutions[g5]).subs(g6, solutions[g6]).subs(g8, solutions[g8]).subs(e1, solutions[e1]).subs(e6, solutions[e6]).subs(e7, solutions[e7]).subs(e8, solutions[e8]).subs(f2, solutions[f2]).subs(f5, solutions[f5]).subs(f7, solutions[f7]).subs(f8, solutions[f8])

Prof6 = (p6 - co6)*soln[q6] - 10*f2**2 - 10*f5**2 - 10*f6**2 - 10*f7**2 - 10*f8**2
Prof6_rep = Prof6.subs(a1, solutions[a1]).subs(b2, solutions[b2]).subs(c3, solutions[c3]).subs(d4, solutions[d4]).subs(e5, solutions[e5]).subs(f6, solutions[f6]).subs(g7, solutions[g7]).subs(h4, solutions[h4]).subs(h5, solutions[h5]).subs(h6, solutions[h6]).subs(h7, solutions[h7]).subs(h8, solutions[h8]).subs(g3, solutions[g3]).subs(g5, solutions[g5]).subs(g6, solutions[g6]).subs(g8, solutions[g8]).subs(e1, solutions[e1]).subs(e6, solutions[e6]).subs(e7, solutions[e7]).subs(e8, solutions[e8]).subs(f2, solutions[f2]).subs(f5, solutions[f5]).subs(f7, solutions[f7]).subs(f8, solutions[f8])

Prof7 = (p7 - co7)*soln[q7] - 10*g3**2 - 10*g5**2 - 10*g6**2 - 10*g7**2 - 10*g8**2
Prof7_rep = Prof7.subs(a1, solutions[a1]).subs(b2, solutions[b2]).subs(c3, solutions[c3]).subs(d4, solutions[d4]).subs(e5, solutions[e5]).subs(f6, solutions[f6]).subs(g7, solutions[g7]).subs(h4, solutions[h4]).subs(h5, solutions[h5]).subs(h6, solutions[h6]).subs(h7, solutions[h7]).subs(h8, solutions[h8]).subs(g3, solutions[g3]).subs(g5, solutions[g5]).subs(g6, solutions[g6]).subs(g8, solutions[g8]).subs(e1, solutions[e1]).subs(e6, solutions[e6]).subs(e7, solutions[e7]).subs(e8, solutions[e8]).subs(f2, solutions[f2]).subs(f5, solutions[f5]).subs(f7, solutions[f7]).subs(f8, solutions[f8])

Prof8 = (p8 - co8)*soln[q8] - 10*h4**2 - 10*h5**2 - 10*h6**2 - 10*h7**2 - 10*h8**2
Prof8_rep = Prof8.subs(a1, solutions[a1]).subs(b2, solutions[b2]).subs(c3, solutions[c3]).subs(d4, solutions[d4]).subs(e5, solutions[e5]).subs(f6, solutions[f6]).subs(g7, solutions[g7]).subs(h4, solutions[h4]).subs(h5, solutions[h5]).subs(h6, solutions[h6]).subs(h7, solutions[h7]).subs(h8, solutions[h8]).subs(g3, solutions[g3]).subs(g5, solutions[g5]).subs(g6, solutions[g6]).subs(g8, solutions[g8]).subs(e1, solutions[e1]).subs(e6, solutions[e6]).subs(e7, solutions[e7]).subs(e8, solutions[e8]).subs(f2, solutions[f2]).subs(f5, solutions[f5]).subs(f7, solutions[f7]).subs(f8, solutions[f8])


#change utility depending on s
Utility= alpha*(soln[q1]) - ((soln[q1])**2)/2 - s*((soln[q1])*(soln[q5])) - ((p1)*(soln[q1])) + alpha*(soln[q2]) - ((soln[q2])**2)/2 - s*((soln[q2])*(soln[q6])) - ((p2)*(soln[q2])) + alpha*(soln[q3]) - ((soln[q3])**2)/2 - s*((soln[q3])*(soln[q7])) - ((p3)*(soln[q3])) + alpha*(soln[q4]) - ((soln[q4])**2)/2 - s*((soln[q4])*(soln[q8])) - ((p4)*(soln[q4])) + alpha*(soln[q5]) - ((soln[q5])**2)/2 - s*((soln[q5])*(soln[q1])) - s*((soln[q5])*(soln[q6])) - s*((soln[q5])*(soln[q7])) - s*((soln[q5])*(soln[q8])) - ((p5)*(soln[q5])) + alpha*(soln[q6]) - ((soln[q6])**2)/2 - s*((soln[q6])*(soln[q2])) - s*((soln[q6])*(soln[q5])) - s*((soln[q6])*(soln[q7])) - s*((soln[q6])*(soln[q8])) - ((p6)*(soln[q6]))  + alpha*(soln[q7]) - ((soln[q7])**2)/2 - s*((soln[q7])*(soln[q3])) - s*((soln[q7])*(soln[q5])) - s*((soln[q7])*(soln[q6])) - s*((soln[q7])*(soln[q8])) - ((p7)*(soln[q7])) + alpha*(soln[q8]) - ((soln[q8])**2)/2 - s*((soln[q8])*(soln[q4])) - s*((soln[q8])*(soln[q5])) - s*((soln[q8])*(soln[q6])) - s*((soln[q8])*(soln[q7]))  - ((p8)*(soln[q8])) 
Utility_rep = Utility.subs(a1, solutions[a1]).subs(b2, solutions[b2]).subs(c3, solutions[c3]).subs(d4, solutions[d4]).subs(e5, solutions[e5]).subs(f6, solutions[f6]).subs(g7, solutions[g7]).subs(h4, solutions[h4]).subs(h5, solutions[h5]).subs(h6, solutions[h6]).subs(h7, solutions[h7]).subs(h8, solutions[h8]).subs(g3, solutions[g3]).subs(g5, solutions[g5]).subs(g6, solutions[g6]).subs(g8, solutions[g8]).subs(e1, solutions[e1]).subs(e6, solutions[e6]).subs(e7, solutions[e7]).subs(e8, solutions[e8]).subs(f2, solutions[f2]).subs(f5, solutions[f5]).subs(f7, solutions[f7]).subs(f8, solutions[f8])


f = Prof1_rep + Prof2_rep + Prof3_rep + Prof4_rep + Prof5_rep + Prof6_rep + Prof7_rep + Prof8_rep + Utility_rep
f_rep = f.subs(a1, solutions[a1]).subs(b2, solutions[b2]).subs(c3, solutions[c3]).subs(d4, solutions[d4]).subs(e5, solutions[e5]).subs(f6, solutions[f6]).subs(g7, solutions[g7]).subs(h4, solutions[h4]).subs(h5, solutions[h5]).subs(h6, solutions[h6]).subs(h7, solutions[h7]).subs(h8, solutions[h8]).subs(g3, solutions[g3]).subs(g5, solutions[g5]).subs(g6, solutions[g6]).subs(g8, solutions[g8]).subs(e1, solutions[e1]).subs(e6, solutions[e6]).subs(e7, solutions[e7]).subs(e8, solutions[e8]).subs(f2, solutions[f2]).subs(f5, solutions[f5]).subs(f7, solutions[f7]).subs(f8, solutions[f8])
print(f_rep)

#from sympy import simplify (we stopped simplify to be faster)
f_simp=f_rep

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
plt.title('Network F | b=0.5')
plt.xlabel('γ')
plt.ylabel('Welfare')
plt.text(0.47, f_max_val -3.5, f"Maximum Welfare: {f_max_val:.2f} at γ={n_max:.2f}", ha='center')
plt.show()