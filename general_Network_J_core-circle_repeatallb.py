import sympy as sym
import numpy as np
import matplotlib.pyplot as plt


# Define symbols
q1, q2, q3, q4, q5, q6, q7, q8, a1, b2, c3, d4, e5, f5, f6, f7, g5, g6, g7, g8, h7, h8, n, a8, c2, d3, e4, b1 = sym.symbols('q1 q2 q3 q4 q5 q6 q7 q8 a1 b2 c3 d4 e5 f5 f6 f7 g5 g6 g7 g8 h7 h8 n a8 c2 d3 e4 b1')


#cost = sym.Symbol('cost')
#s = sym.Symbol('s')
#each time you change network also change prices, costs, utility
alpha=10
cost=5

#add s and n max values here, then for, shift tab, add in the end
#plot, max value append, s values, take out the simplify, then run
# Define range of s values
s_values = np.arange(0, 1.01, 0.05)

# Define lists to store n_max values for each s
n_max_values = []


for s in s_values:
        
    # Define profit functions
    P1 = alpha - s*q5 - q1
    P2 = alpha - s*q6 - q2
    P3 = alpha - s*q7 - q3
    P4 = alpha - s*q8 - q4
    P5 = alpha - s*q1 - s*q6 - s*q7 - s*q8 - q5
    P6 = alpha - s*q2 - s*q5 - s*q7 - s*q8 - q6
    P7 = alpha - s*q3 - s*q5 - s*q6 - s*q8 - q7
    P8 = alpha - s*q4 - s*q5 - s*q6 - s*q7 - q8
    
    
    
    C1 = cost - a1 - a8 - n*b1 - n*h8
    C2 = cost - b2 - b1 - n*c2 - n*a1
    C3 = cost - c3 - c2 - n*d3 - n*b2
    C4 = cost - d4 - d3 - n*e4 - n*c3
    C5 = cost - e5 - e4 - n*f5 - n*d4
    C6 = cost - f6 - f5 - n*g6 - n*e5
    C7 = cost - g7 - g6 - n*h7 - n*f6
    C8 = cost - h8 - h7 - n*a8 - n*g7
    
    
    
    
    prof1 = (P1-C1)*q1 - 4*a1**2 - 4*a8**2
    prof2 = (P2-C2)*q2 - 4*b2**2 - 4*b1**2
    prof3 = (P3-C3)*q3 - 4*c3**2 - 4*c2**2
    prof4 = (P4-C4)*q4 - 4*d4**2 - 4*d3**2
    prof5 = (P5-C5)*q5 - 4*e5**2 - 4*e4**2
    prof6 = (P6-C6)*q6 - 4*f6**2 - 4*f5**2
    prof7 = (P7-C7)*q7 - 4*g7**2 - 4*g6**2
    prof8 = (P8-C8)*q8 - 4*h8**2 - 4*h7**2
    
    
    
    
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
    
    
    
    
    
    Prof1 = (p1 - co1)*soln[q1] - 4*a1**2 - 4*a8**2
    Prof2 = (p2 - co2)*soln[q2] - 4*b2**2 - 4*b1**2
    Prof3 = (p3 - co3)*soln[q3] - 4*c3**2 - 4*c2**2 
    Prof4 = (p4 - co4)*soln[q4] - 4*d4**2 - 4*d3**2
    Prof5 = (p5 - co5)*soln[q5] - 4*e5**2 - 4*e4**2
    Prof6 = (p6 - co6)*soln[q6] - 4*f6**2 - 4*f5**2
    Prof7 = (p7 - co7)*soln[q7] - 4*g7**2 - 4*g6**2
    Prof8 = (p8 - co8)*soln[q8] - 4*h8**2 - 4*h7**2
    
    
    
    
    #########################################################
    
    
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
    f_double_prime_Prof1_a8 = Prof1.diff(a8, 2)
    
    f_double_prime_Prof2_b2 = Prof2.diff(b2, 2)
    f_double_prime_Prof2_b1 = Prof2.diff(b1, 2)
    
    f_double_prime_Prof3_c3 = Prof3.diff(c3, 2)
    f_double_prime_Prof3_c2 = Prof3.diff(c2, 2)
    
    f_double_prime_Prof4_d4 = Prof4.diff(d4, 2)
    f_double_prime_Prof4_d3 = Prof4.diff(d3, 2)
    
    f_double_prime_Prof5_e5 = Prof5.diff(e5, 2)
    f_double_prime_Prof5_e4 = Prof5.diff(e4, 2)
    
    f_double_prime_Prof6_f6 = Prof6.diff(f6, 2)
    f_double_prime_Prof6_f5 = Prof6.diff(f5, 2)
    
    f_double_prime_Prof7_g7 = Prof7.diff(g7, 2)
    f_double_prime_Prof7_g6 = Prof7.diff(g6, 2)
    
    f_double_prime_Prof8_h8 = Prof8.diff(h8, 2)
    f_double_prime_Prof8_h7 = Prof8.diff(h7, 2)
    
    
    # Values of n to check for concavity
    n_values = np.arange(0, 1.01, 0.01)
    
    for n_val in n_values:
        # Substitute n with the current value
        f_double_prime_Prof1_a1_n = f_double_prime_Prof1_a1.subs({n: n_val})
        f_double_prime_Prof1_a8_n = f_double_prime_Prof1_a8.subs({n: n_val})
    
        f_double_prime_Prof2_b2_n = f_double_prime_Prof2_b2.subs({n: n_val})
        f_double_prime_Prof2_b1_n = f_double_prime_Prof2_b1.subs({n: n_val})
    
        f_double_prime_Prof3_c3_n = f_double_prime_Prof3_c3.subs({n: n_val})
        f_double_prime_Prof3_c2_n = f_double_prime_Prof3_c2.subs({n: n_val})
    
        f_double_prime_Prof4_d4_n = f_double_prime_Prof4_d4.subs({n: n_val})
        f_double_prime_Prof4_d3_n = f_double_prime_Prof4_d3.subs({n: n_val})
    
        f_double_prime_Prof5_e5_n = f_double_prime_Prof5_e5.subs({n: n_val})
        f_double_prime_Prof5_e4_n = f_double_prime_Prof5_e4.subs({n: n_val})
    
        f_double_prime_Prof6_f6_n = f_double_prime_Prof6_f6.subs({n: n_val})
        f_double_prime_Prof6_f5_n = f_double_prime_Prof6_f5.subs({n: n_val})
    
        f_double_prime_Prof7_g7_n = f_double_prime_Prof7_g7.subs({n: n_val})
        f_double_prime_Prof7_g6_n = f_double_prime_Prof7_g6.subs({n: n_val})
    
        f_double_prime_Prof8_h8_n = f_double_prime_Prof8_h8.subs({n: n_val})
        f_double_prime_Prof8_h7_n = f_double_prime_Prof8_h7.subs({n: n_val})
    
        # Check if the second derivatives are non-positive
        if (f_double_prime_Prof1_a1_n.is_nonpositive and f_double_prime_Prof1_a8_n.is_nonpositive
                and f_double_prime_Prof2_b2_n.is_nonpositive and f_double_prime_Prof2_b1_n.is_nonpositive
                and f_double_prime_Prof3_c3_n.is_nonpositive and f_double_prime_Prof3_c2_n.is_nonpositive
                and f_double_prime_Prof4_d4_n.is_nonpositive and f_double_prime_Prof4_d3_n.is_nonpositive
                and f_double_prime_Prof5_e5_n.is_nonpositive and f_double_prime_Prof5_e4_n.is_nonpositive
                and f_double_prime_Prof6_f6_n.is_nonpositive and f_double_prime_Prof6_f5_n.is_nonpositive
                and f_double_prime_Prof7_g7_n.is_nonpositive and f_double_prime_Prof7_g6_n.is_nonpositive
                and f_double_prime_Prof8_h8_n.is_nonpositive and f_double_prime_Prof8_h7_n.is_nonpositive):
            print(f"All functions are concave for n = {n_val}")
        else:
            print(f"Some functions are not concave for n = {n_val}")
    
            
            
    
    # define first derivatives of the profits with respect to a1, a2, b1, b2, b3, c1, and c2
    f_Prof1_a1 = Prof1.diff(a1)
    f_Prof1_a8 = Prof1.diff(a8)
    
    f_Prof2_b2 = Prof2.diff(b2)
    f_Prof2_b1 = Prof2.diff(b1)
    
    f_Prof3_c3 = Prof3.diff(c3)
    f_Prof3_c2 = Prof3.diff(c2)
    
    f_Prof4_d4 = Prof4.diff(d4)
    f_Prof4_d3 = Prof4.diff(d3)
    
    f_Prof5_e5 = Prof5.diff(e5)
    f_Prof5_e4 = Prof5.diff(e4)
    
    f_Prof6_f6 = Prof6.diff(f6)
    f_Prof6_f5 = Prof6.diff(f5)
    
    f_Prof7_g7 = Prof7.diff(g7)
    f_Prof7_g6 = Prof7.diff(g6)
    
    f_Prof8_h8 = Prof8.diff(h8)
    f_Prof8_h7 = Prof8.diff(h7)
    
    
    
    # set first derivatives to zero and solve for a1, a2, b1, b2, b3, c1, and c2
    eq1 = f_Prof1_a1
    eq2 = f_Prof1_a8
    eq3 = f_Prof2_b2
    eq4 = f_Prof2_b1
    eq5 = f_Prof3_c3
    eq6 = f_Prof3_c2
    eq7 = f_Prof4_d4
    eq8 = f_Prof4_d3
    eq9 = f_Prof5_e5
    eq10 = f_Prof5_e4
    eq11 = f_Prof6_f6
    eq12 = f_Prof6_f5
    eq13 = f_Prof7_g7
    eq14 = f_Prof7_g6
    eq15 = f_Prof8_h8
    eq16 = f_Prof8_h7
    
    
    
    # Solve equations and store results
    solutions = sym.solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, eq11, eq12, eq13, eq14, eq15, eq16), (a1, a8, b2, b1, c3, c2, d4, d3, e5, e4, f6, f5, g7, g6, h8, h7))
    
    
    
    A1 = solutions[a1]
    A8 = solutions[a8]
    B2 = solutions[b2]
    B1 = solutions[b1]
    C3 = solutions[c3]
    C2 = solutions[c2]
    D4 = solutions[d4]
    D3 = solutions[d3]
    E5 = solutions[e5]
    E4 = solutions[e4]
    F6 = solutions[f6]
    F5 = solutions[f5]
    G7 = solutions[g7]
    G6 = solutions[g6]
    H8 = solutions[h8]
    H7 = solutions[h7]
    
    
    
    print("Solutions for a1, a8, b2, b1, c3, c2, d4, d3, e5, e4, f6, f5, g7, g6, h8, h7:")
    print("A1:", A1)
    print("A8:", A8)
    print("B2:", B2)
    print("B1:", B1)
    print("C3:", C3)
    print("C2:", C2)
    print("D4:", D4)
    print("D3:", D3)
    print("E5:", E5)
    print("E4:", E4)
    print("F6:", F6)
    print("F5:", F5)
    print("G7:", G7)
    print("G6:", G6)
    print("H8:", H8)
    print("H7:", H7)
    
    
    
    
    n = sym.symbols('n')
    n_values = np.array([0, 0.2, 0.4, 0.5, 0.8, 1])
    
    for n_val in n_values:
        print("For n =", n_val)
        print("A1 =", A1.subs(n, n_val))
        print("A8 =", A8.subs(n, n_val))
        print("B2 =", B2.subs(n, n_val))
        print("B1 =", B1.subs(n, n_val))
        print("C3 =", C3.subs(n, n_val))
        print("C2 =", C2.subs(n, n_val))
        print("D4 =", D4.subs(n, n_val))
        print("D3 =", D3.subs(n, n_val))
        print("E5 =", E5.subs(n, n_val))
        print("E4 =", E4.subs(n, n_val))
        print("F6 =", F6.subs(n, n_val))
        print("F5 =", F5.subs(n, n_val))
        print("G7 =", G7.subs(n, n_val))
        print("G6 =", G6.subs(n, n_val))
        print("H8 =", H8.subs(n, n_val))
        print("H7 =", H7.subs(n, n_val))
        print()
    
    
    
    
    ##########################################################

    
    
    # Define your function as the sum of 4 symbolic expressions
    Prof1 = (p1 - co1)*soln[q1] - 4*a1**2 - 4*a8**2
    Prof1_rep = Prof1.subs([(a1, solutions[a1]), (a8, solutions[a8]), (b2, solutions[b2]), (b1, solutions[b1]),(c3, solutions[c3]), (c2, solutions[c2]), (d4, solutions[d4]), (d3, solutions[d3]), (e5, solutions[e5]), (e4, solutions[e4]), (f6, solutions[f6]), (f5, solutions[f5]),(g7, solutions[g7]), (g6, solutions[g6]), (h8, solutions[h8]), (h7, solutions[h7])])
    
    
    Prof2 = (p2 - co2)*soln[q2] - 4*b2**2 - 4*b1**2
    Prof2_rep = Prof2.subs([(a1, solutions[a1]), (a8, solutions[a8]), (b2, solutions[b2]), (b1, solutions[b1]),(c3, solutions[c3]), (c2, solutions[c2]), (d4, solutions[d4]), (d3, solutions[d3]), (e5, solutions[e5]), (e4, solutions[e4]), (f6, solutions[f6]), (f5, solutions[f5]),(g7, solutions[g7]), (g6, solutions[g6]), (h8, solutions[h8]), (h7, solutions[h7])])
    
    
    Prof3 = (p3 - co3)*soln[q3] - 4*c3**2 - 4*c2**2 
    Prof3_rep = Prof3.subs([(a1, solutions[a1]), (a8, solutions[a8]), (b2, solutions[b2]), (b1, solutions[b1]),(c3, solutions[c3]), (c2, solutions[c2]), (d4, solutions[d4]), (d3, solutions[d3]), (e5, solutions[e5]), (e4, solutions[e4]), (f6, solutions[f6]), (f5, solutions[f5]),(g7, solutions[g7]), (g6, solutions[g6]), (h8, solutions[h8]), (h7, solutions[h7])])
    
    
    Prof4 = (p4 - co4)*soln[q4] - 4*d4**2 - 4*d3**2
    Prof4_rep = Prof4.subs([(a1, solutions[a1]), (a8, solutions[a8]), (b2, solutions[b2]), (b1, solutions[b1]),(c3, solutions[c3]), (c2, solutions[c2]), (d4, solutions[d4]), (d3, solutions[d3]), (e5, solutions[e5]), (e4, solutions[e4]), (f6, solutions[f6]), (f5, solutions[f5]),(g7, solutions[g7]), (g6, solutions[g6]), (h8, solutions[h8]), (h7, solutions[h7])])
    
    
    Prof5 = (p5 - co5)*soln[q5] - 4*e5**2 - 4*e4**2
    Prof5_rep = Prof5.subs([(a1, solutions[a1]), (a8, solutions[a8]), (b2, solutions[b2]), (b1, solutions[b1]),(c3, solutions[c3]), (c2, solutions[c2]), (d4, solutions[d4]), (d3, solutions[d3]), (e5, solutions[e5]), (e4, solutions[e4]), (f6, solutions[f6]), (f5, solutions[f5]),(g7, solutions[g7]), (g6, solutions[g6]), (h8, solutions[h8]), (h7, solutions[h7])])
    
    
    Prof6 = (p6 - co6)*soln[q6] - 4*f6**2 - 4*f5**2
    Prof6_rep = Prof6.subs([(a1, solutions[a1]), (a8, solutions[a8]), (b2, solutions[b2]), (b1, solutions[b1]),(c3, solutions[c3]), (c2, solutions[c2]), (d4, solutions[d4]), (d3, solutions[d3]), (e5, solutions[e5]), (e4, solutions[e4]), (f6, solutions[f6]), (f5, solutions[f5]),(g7, solutions[g7]), (g6, solutions[g6]), (h8, solutions[h8]), (h7, solutions[h7])])
    
    
    Prof7 = (p7 - co7)*soln[q7] - 4*g7**2 - 4*g6**2
    Prof7_rep = Prof7.subs([(a1, solutions[a1]), (a8, solutions[a8]), (b2, solutions[b2]), (b1, solutions[b1]),(c3, solutions[c3]), (c2, solutions[c2]), (d4, solutions[d4]), (d3, solutions[d3]), (e5, solutions[e5]), (e4, solutions[e4]), (f6, solutions[f6]), (f5, solutions[f5]),(g7, solutions[g7]), (g6, solutions[g6]), (h8, solutions[h8]), (h7, solutions[h7])])
    
    
    Prof8 = (p8 - co8)*soln[q8] - 4*h8**2 - 4*h7**2
    Prof8_rep = Prof8.subs([(a1, solutions[a1]), (a8, solutions[a8]), (b2, solutions[b2]), (b1, solutions[b1]),(c3, solutions[c3]), (c2, solutions[c2]), (d4, solutions[d4]), (d3, solutions[d3]), (e5, solutions[e5]), (e4, solutions[e4]), (f6, solutions[f6]), (f5, solutions[f5]),(g7, solutions[g7]), (g6, solutions[g6]), (h8, solutions[h8]), (h7, solutions[h7])])
    
    
    
    #change utility depending on s
    Utility= alpha*(soln[q1]) - ((soln[q1])**2)/2 - s*((soln[q1])*(soln[q5])) - ((p1)*(soln[q1])) + alpha*(soln[q2]) - ((soln[q2])**2)/2 - s*((soln[q2])*(soln[q6])) - ((p2)*(soln[q2])) + alpha*(soln[q3]) - ((soln[q3])**2)/2 - s*((soln[q3])*(soln[q7])) - ((p3)*(soln[q3])) + alpha*(soln[q4]) - ((soln[q4])**2)/2 - s*((soln[q4])*(soln[q8])) - ((p4)*(soln[q4])) + alpha*(soln[q5]) - ((soln[q5])**2)/2 - s*((soln[q5])*(soln[q1])) - s*((soln[q5])*(soln[q6])) - s*((soln[q5])*(soln[q7])) - s*((soln[q5])*(soln[q8])) - ((p5)*(soln[q5])) + alpha*(soln[q6]) - ((soln[q6])**2)/2 - s*((soln[q6])*(soln[q2])) - s*((soln[q6])*(soln[q5])) - s*((soln[q6])*(soln[q7])) - s*((soln[q6])*(soln[q8])) - ((p6)*(soln[q6]))  + alpha*(soln[q7]) - ((soln[q7])**2)/2 - s*((soln[q7])*(soln[q3])) - s*((soln[q7])*(soln[q5])) - s*((soln[q7])*(soln[q6])) - s*((soln[q7])*(soln[q8])) - ((p7)*(soln[q7])) + alpha*(soln[q8]) - ((soln[q8])**2)/2 - s*((soln[q8])*(soln[q4])) - s*((soln[q8])*(soln[q5])) - s*((soln[q8])*(soln[q6])) - s*((soln[q8])*(soln[q7]))  - ((p8)*(soln[q8])) 
    Utility_rep = Utility.subs([(a1, solutions[a1]), (a8, solutions[a8]), (b2, solutions[b2]), (b1, solutions[b1]),(c3, solutions[c3]), (c2, solutions[c2]), (d4, solutions[d4]), (d3, solutions[d3]), (e5, solutions[e5]), (e4, solutions[e4]), (f6, solutions[f6]), (f5, solutions[f5]),(g7, solutions[g7]), (g6, solutions[g6]), (h8, solutions[h8]), (h7, solutions[h7])])
    
    
    f = Prof1_rep + Prof2_rep + Prof3_rep + Prof4_rep + Prof5_rep + Prof6_rep + Prof7_rep + Prof8_rep + Utility_rep
    f_rep = f.subs([(a1, solutions[a1]), (a8, solutions[a8]), (b2, solutions[b2]), (b1, solutions[b1]),(c3, solutions[c3]), (c2, solutions[c2]), (d4, solutions[d4]), (d3, solutions[d3]), (e5, solutions[e5]), (e4, solutions[e4]), (f6, solutions[f6]), (f5, solutions[f5]),(g7, solutions[g7]), (g6, solutions[g6]), (h8, solutions[h8]), (h7, solutions[h7])])
    print(f_rep)
    
    #from sympy import simplify (we stopped simplify to be faster)
    f_simp=f_rep
    
    
    def evaluate_f(n):
        return f_simp.subs({'n': n})
    n_vals = np.arange(0, 1.01, 0.01)
    f_vals = np.array([evaluate_f(n) for n in n_vals])
    f_max_val = np.max(f_vals)
    n_max = n_vals[np.argmax(f_vals)]
    n_max_values.append(n_max)


s_values = np.array(s_values)

# Plot results
plt.plot(s_values, n_max_values)
plt.title('Network J | b∈[0,1]')
plt.xlabel('b')
plt.ylabel('γ*')
plt.show() 