import sympy as sym
import numpy as np

# Define symbols
q1a, q2a, q3a, q4a, q5b, q6c, q7d, q8e, a1, b2, c3, d4, e1, e5, e6, e7, e8, f2, f5, f6, f7, f8, g3, g5, g6, g7, g8, h4, h5, h6, h7, h8, n = sym.symbols('q1a q2a q3a q4a q5b q6c q7d q8e a1 b2 c3 d4 e1 e5 e6 e7 e8 f2 f5 f6 f7 f8 g3 g5 g6 g7 g8 h4 h5 h6 h7 h8 n')
d1, d2, e2,d3,e3, a1, a2, b1, b2, b3, c1, c2 = sym.symbols('d1 d2 e2 d3 e3 a1 a2 b1 b2 b3 c1 c2 ')
f1, f3, g1,g2,h1,h2,h3 = sym.symbols('f1 f3 g1 g2 h1 h2 h3')
q1b, q2b, q3b = sym.symbols('q1b q2b q3b')
q1c, q2c, q3c = sym.symbols('q1c q2c q3c')
q1d, q2d, q3d = sym.symbols('q1d q2d q3d')
q1e, q2e, q3e = sym.symbols('q1e q2e q3e')


# Define parameters
#alpha = sym.Symbol('alpha')
#cost = sym.Symbol('cost')
#s = sym.Symbol('s')
#each time you change network also change prices, costs, utility
alpha=10
cost=5

#add s and n max values here, then for, shift tab, add in the end
#plot, max value append, s values, take out the simplify, then run
# Define range of s values
#s_values_1 = np.arange(0, 0.51, 0.1)  # Range from 0 to 0.5 with 0.1 steps
#s_values_2 = np.arange(0.52, 1.01, 0.02)  # Range from 0.52 to 1 with 0.02 steps
#s_values = np.concatenate((s_values_1, s_values_2))
#print(s_values)
s_values = np.arange(0, 1.01, 0.02)

# Define lists to store n_max values for each s
n_max_values = []


for s in s_values:
    # Define profit functions for good 1 for the 3 firms + follower q4
    P1a = alpha - s*q2a - s*q3a - s*q4a - q1a
    P2a = alpha - s*q1a - s*q3a - s*q4a - q2a
    P3a = alpha - s*q1a - s*q2a - s*q4a - q3a
    P4a = alpha - s*q1a - s*q2a - s*q3a - q4a
    
    
    C1a = cost - a1 - a2 - n*b1 - n*b2 - n*c1 -n*d1 - n*d2
    C2a = cost - b1 - b2 - b3 - n*a1 - n*a2 - n*c1 - n*d1 - n*d2 - n*d3
    C3a = cost - c1 - c2 - n*a1 - n*b1 - n*d1
    C4a = cost - d1 - d2 - d3 - n*a1 - n*a2 - n*b1 - n*b2 - n*b3 - n*c1
    
    
    prof1a = (P1a-C1a)*q1a - 4*a1**2 - 4*a2**2
    prof2a = (P2a-C2a)*q2a - 6*b1**2 - 6*b2**2 - 6*b3**2
    prof3a = (P3a-C3a)*q3a - 4*c1**2 - 4*c2**2
    prof4a = (P4a-C4a)*q4a - 6*d1**2 - 6*d2**2 - 6*d3**2
    
    
    
    # Define profit functions for good 2 for the 3 firms + follower q5
    P1b = alpha - s*q2b - s*q5b - q1b
    P2b = alpha - s*q1b - s*q3b - s*q5b - q2b
    P3b = alpha - s*q2b - s*q5b - q3b
    P5b = alpha - s*q1b - s*q3b - s*q2b - q5b
    
    
    C1b = cost - a1 - a2 - n*b1 - n*b2 - n*e1 - n*e2
    C2b = cost - b1 - b2 - b3 - n*a1 - n*a2 - n*c1 - n*e1 - n*e2 - n*e3
    C3b = cost - c1 - c2 - n*b1 - n*e1
    C5b = cost - e1 - e2 - e3 - n*a1 - n*a2 - n*b1 - n*b2 - n*b3 - n*c1
    
    
    
    prof1b = (P1b-C1b)*q1b - 4*a1**2 - 4*a2**2
    prof2b = (P2b-C2b)*q2b - 6*b1**2 - 6*b2**2 - 6*b3**2
    prof3b = (P3b-C3b)*q3b - 4*c1**2 - 4*c2**2
    prof5b = (P5b-C5b)*q5b - 6*e1**2 - 6*e2**2 - 6*e3**2
    
    
    
    # Define profit functions for good 3 for the 3 firms + follower q6
    P1c = alpha - s*q2c - s*q3c - s*q6c - q1c
    P2c = alpha - s*q1c - s*q3c - s*q6c - q2c
    P3c = alpha - s*q1c - s*q2c - s*q6c - q3c
    P6c = alpha - s*q1c - s*q3c - s*q2c - q6c
    
    
    C1c = cost - a1 - a2 - n*b1 - n*b2 - n*f1 - n*f2
    C2c = cost - b1 - b2 - b3 - n*a1 - n*a2 - n*c1 - n*f1 - n*f2 - n*f3
    C3c = cost - c1 - c2 - n*b1 - n*f1
    C6c = cost - f1 - f2 - f3 - n*a1 - n*a2 - n*b1 - n*b2 - n*b3 - n*c1
    
    
    
    prof1c = (P1c-C1c)*q1c - 4*a1**2 - 4*a2**2
    prof2c = (P2c-C2c)*q2c - 6*b1**2 - 6*b2**2 - 6*b3**2
    prof3c = (P3c-C3c)*q3c - 4*c1**2 - 4*c2**2
    prof6c = (P6c-C6c)*q6c - 6*f1**2 - 6*f2**2 - 6*f3**2
    
    
    
    
    # Define profit functions for good 4 for the 3 firms + follower q7
    P1d = alpha - s*q2d - s*q7d - q1d
    P2d = alpha - s*q1d - s*q3d - s*q7d - q2d
    P3d = alpha - s*q2d - s*q7d - q3d
    P7d = alpha - s*q1d - s*q3d - s*q2d - q7d
    
    
    C1d = cost - a1 - a2 - n*b1 - n*b2 - n*c1 -n*g1 - n*g2
    C2d = cost - b1 - b2 - b3 - n*a1 - n*a2 - n*c1 - n*g1 - n*g2 - n*g3
    C3d = cost - c1 - c2 - n*a1 - n*b1 - n*g1
    C7d = cost - g1 - g2 - g3 - n*a1 - n*a2 - n*b1 - n*b2 - n*b3 - n*c1
    
    
    prof1d = (P1d-C1d)*q1d - 4*a1**2 - 4*a2**2
    prof2d = (P2d-C2d)*q2d - 6*b1**2 - 6*b2**2 - 6*b3**2
    prof3d = (P3d-C3d)*q3d - 4*c1**2 - 4*c2**2
    prof7d = (P7d-C7d)*q7d - 6*g1**2 - 6*g2**2 - 6*g3**2
    
    
    
    
    # Define profit functions for good 5 for the 3 firms + follower q8
    P1e = alpha - s*q2e - s*q3e - s*q8e - q1e
    P2e = alpha - s*q1e - s*q8e - q2e
    P3e = alpha - s*q1e - s*q8e - q3e
    P8e = alpha - s*q2e - s*q3e - s*q1e - q8e
    
    
    C1e = cost - a1 - a2 - n*b1 - n*b2 - n*h1 - n*h2
    C2e = cost - b1 - b2 - b3 - n*a1 - n*a2 - n*c1 - n*h1 - n*h2 - n*h3
    C3e = cost - c1 - c2 - n*b1 - n*h1
    C8e = cost - h1 - h2 - h3 - n*a1 - n*a2 - n*b1 - n*b2 - n*b3 - n*c1
    
    
    prof1e = (P1e-C1e)*q1e - 4*a1**2 - 4*a2**2
    prof2e = (P2e-C2e)*q2e - 6*b1**2 - 6*b2**2 - 6*b3**2
    prof3e = (P3e-C3e)*q3e - 4*c1**2 - 4*c2**2
    prof8e = (P8e-C8e)*q8e - 6*h1**2 - 6*h2**2 - 6*h3**2
    
    
    
    #sum of profits now to maximize prof1=prof1a+prof1b etc
    prof1 = prof1a + prof1b + prof1c + prof1d + prof1e
    prof2 = prof2a + prof2b + prof2c + prof2d + prof2e
    prof3 = prof3a + prof3b + prof3c + prof3d + prof3e
    prof4 = prof4a
    prof5 = prof5b
    prof6 = prof6c
    prof7 = prof7d
    prof8 = prof8e
    
    
    
    
    # Take derivatives
    dq1a = sym.diff(prof1, q1a)
    dq2a = sym.diff(prof2, q2a)
    dq3a = sym.diff(prof3, q3a)
    dq4a = sym.diff(prof4, q4a)
    dq5b = sym.diff(prof5, q5b)
    dq6c = sym.diff(prof6, q6c)
    dq7d = sym.diff(prof7, q7d)
    dq8e = sym.diff(prof8, q8e)
    dq1b = sym.diff(prof1, q1b)
    dq2b = sym.diff(prof2, q2b)
    dq3b = sym.diff(prof3, q3b)
    dq1c = sym.diff(prof1, q1c)
    dq2c = sym.diff(prof2, q2c)
    dq3c = sym.diff(prof3, q3c)
    dq1d = sym.diff(prof1, q1d)
    dq2d = sym.diff(prof2, q2d)
    dq3d = sym.diff(prof3, q3d)
    dq1e = sym.diff(prof1, q1e)
    dq2e = sym.diff(prof2, q2e)
    dq3e = sym.diff(prof3, q3e)
    
    
    
    
    
    
    # Set derivatives to 0 and solve for q1, q2, q3
    soln = sym.solve((dq1a, dq2a, dq3a, dq4a, dq5b, dq6c, dq7d, dq8e, dq1b, dq2b, dq3b, dq1c, dq2c, dq3c,dq1d, dq2d, dq3d,dq1e, dq2e, dq3e), (q1a, q2a, q3a, q4a, q5b, q6c, q7d, q8e,q1b, q2b, q3b,q1c, q2c, q3c,q1d, q2d, q3d,q1e, q2e, q3e,))
    
    
    # Print optimal values of q1, q2, q3
    print("Optimal value of q1a:", soln[q1a])
    print("Optimal value of q2a:", soln[q2a])
    print("Optimal value of q3a:", soln[q3a])
    print("Optimal value of q4a:", soln[q4a])
    print("Optimal value of q5b:", soln[q5b])
    print("Optimal value of q6c:", soln[q6c])
    print("Optimal value of q7d:", soln[q7d])
    print("Optimal value of q8e:", soln[q8e])
    print("Optimal value of q1b:", soln[q1b])
    print("Optimal value of q2b:", soln[q2b])
    print("Optimal value of q3b:", soln[q3b])
    print("Optimal value of q1c:", soln[q1c])
    print("Optimal value of q2c:", soln[q2c])
    print("Optimal value of q3c:", soln[q3c])
    print("Optimal value of q1d:", soln[q1d])
    print("Optimal value of q2d:", soln[q2d])
    print("Optimal value of q3d:", soln[q3d])
    print("Optimal value of q1e:", soln[q1e])
    print("Optimal value of q2e:", soln[q2e])
    print("Optimal value of q3e:", soln[q3e])
    
    
    
    p1a = P1a.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p2a = P2a.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p3a = P3a.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p4a = P4a.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p5b = P5b.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p6c = P6c.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p7d = P7d.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p8e = P8e.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p1b = P1b.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p2b = P2b.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p3b = P3b.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p1c = P1c.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p2c = P2c.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p3c = P3c.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p1d = P1d.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p2d = P2d.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p3d = P3d.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p1e = P1e.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p2e = P2e.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    p3e = P3e.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    
    
    
    co1a = C1a.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co2a = C2a.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co3a = C3a.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co4a = C4a.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co5b = C5b.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co6c = C6c.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co7d = C7d.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co8e = C8e.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co1b = C1b.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co2b = C2b.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co3b = C3b.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co1c = C1c.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co2c = C2c.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co3c = C3c.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co1d = C1d.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co2d = C2d.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co3d = C3d.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co1e = C1e.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co2e = C2e.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    co3e = C3e.subs({q1a: soln[q1a], q2a: soln[q2a], q3a: soln[q3a], q4a: soln[q4a], q5b: soln[q5b], q6c: soln[q6c], q7d: soln[q7d], q8e: soln[q8e], q1b: soln[q1b], q2b: soln[q2b], q3b: soln[q3b],q1c: soln[q1c], q2c: soln[q2c], q3c: soln[q3c],q1d: soln[q1d], q2d: soln[q2d], q3d: soln[q3d],q1e: soln[q1e], q2e: soln[q2e], q3e: soln[q3e],})
    
    
    
    
    Prof1a = (p1a - co1a)*soln[q1a] - 4*a1**2 - 4*a2**2
    Prof2a = (p2a - co2a)*soln[q2a] - 6*b1**2 - 6*b2**2 - 6*b3**2
    Prof3a = (p3a - co3a)*soln[q3a] - 4*c1**2 - 4*c2**2
    Prof4a = (p4a - co4a)*soln[q4a] - 6*d1**2 - 6*d2**2 - 6*d3**2 
    Prof5b = (p5b - co5b)*soln[q5b] - 6*e1**2 - 6*e2**2 - 6*e3**2
    Prof6c = (p6c - co6c)*soln[q6c] - 6*f1**2 - 6*f2**2 - 6*f3**2 
    Prof7d = (p7d - co7d)*soln[q7d] - 6*g1**2 - 6*g2**2 - 6*g3**2
    Prof8e = (p8e - co8e)*soln[q8e] - 6*h1**2 - 6*h2**2 - 6*h3**2
    Prof1b = (p1b - co1b)*soln[q1b] - 4*a1**2 - 4*a2**2
    Prof2b = (p2b - co2b)*soln[q2b] - 6*b1**2 - 6*b2**2 - 6*b3**2
    Prof3b = (p3b - co3b)*soln[q3b] - 4*c1**2 - 4*c2**2
    Prof1c = (p1c - co1c)*soln[q1c] - 4*a1**2 - 4*a2**2
    Prof2c = (p2c - co2c)*soln[q2c] - 6*b1**2 - 6*b2**2 - 6*b3**2
    Prof3c = (p3c - co3c)*soln[q3c] - 4*c1**2 - 4*c2**2
    Prof1d = (p1d - co1d)*soln[q1d] - 4*a1**2 - 4*a2**2
    Prof2d = (p2d - co2d)*soln[q2d] - 6*b1**2 - 6*b2**2 - 6*b3**2
    Prof3d = (p3d - co3d)*soln[q3d] - 4*c1**2 - 4*c2**2
    Prof1e = (p1e - co1e)*soln[q1e] - 4*a1**2 - 4*a2**2
    Prof2e = (p2e - co2e)*soln[q2e] - 6*b1**2 - 6*b2**2 - 6*b3**2
    Prof3e = (p3e - co3e)*soln[q3e] - 4*c1**2 - 4*c2**2
    
    
    
    Prof1 = Prof1a + Prof1b + Prof1c + Prof1d + Prof1e
    Prof2 = Prof2a + Prof2b + Prof2c + Prof2d + Prof2e
    Prof3 = Prof3a + Prof3b + Prof3c + Prof3d + Prof3e
    Prof4 = Prof4a
    Prof5 = Prof5b
    Prof6 = Prof6c
    Prof7 = Prof7d
    Prof8 = Prof8e
    
    
    
    
    Utility= alpha*(soln[q1a]) - ((soln[q1a])**2)/2 - s*((soln[q1a])*(soln[q2a])) - s*((soln[q1a])*(soln[q3a])) - s*((soln[q1a])*(soln[q4a])) - ((p1a)*(soln[q1a])) +  alpha*(soln[q2a]) - ((soln[q2a])**2)/2 - s*((soln[q2a])*(soln[q1a])) - s*((soln[q2a])*(soln[q3a])) - s*((soln[q2a])*(soln[q4a])) - ((p2a)*(soln[q2a])) +  alpha*(soln[q3a]) - ((soln[q3a])**2)/2 - s*((soln[q3a])*(soln[q1a])) - s*((soln[q3a])*(soln[q2a])) - s*((soln[q3a])*(soln[q4a]))  - ((p3a)*(soln[q3a])) + alpha*(soln[q4a]) - ((soln[q4a])**2)/2 - s*((soln[q4a])*(soln[q1a])) - s*((soln[q4a])*(soln[q2a])) - s*((soln[q4a])*(soln[q3a])) - ((p4a)*(soln[q4a])) + alpha*(soln[q1b]) - ((soln[q1b])**2)/2 - s*((soln[q1b])*(soln[q2b])) - s*((soln[q1b])*(soln[q5b]))  - ((p1b)*(soln[q1b])) + \
    alpha*(soln[q2b]) - ((soln[q2b])**2)/2 - s*((soln[q2b])*(soln[q1b])) - s*((soln[q2b])*(soln[q3b])) - s*((soln[q2b])*(soln[q5b]))  - ((p2b)*(soln[q2b])) + alpha*(soln[q3b]) - ((soln[q3b])**2)/2 - s*((soln[q3b])*(soln[q2b])) - s*((soln[q3b])*(soln[q5b])) - ((p3b)*(soln[q3b])) + alpha*(soln[q5b]) - ((soln[q5b])**2)/2 - s*((soln[q5b])*(soln[q1b])) - s*((soln[q5b])*(soln[q2b])) - s*((soln[q5b])*(soln[q3b])) - ((p5b)*(soln[q5b])) + alpha*(soln[q1c]) - ((soln[q1c])**2)/2 - s*((soln[q1c])*(soln[q2c])) - s*((soln[q1c])*(soln[q3c])) - s*((soln[q1c])*(soln[q6c])) - ((p1c)*(soln[q1c])) + alpha*(soln[q2c]) - ((soln[q2c])**2)/2 - s*((soln[q2c])*(soln[q1c])) - s*((soln[q2c])*(soln[q3c])) - s*((soln[q2c])*(soln[q6c])) - ((p2c)*(soln[q2c])) + alpha*(soln[q3c]) - ((soln[q3c])**2)/2 -  s*((soln[q3c])*(soln[q1c])) - s*((soln[q3c])*(soln[q2c])) - s*((soln[q3c])*(soln[q6c])) - ((p3c)*(soln[q3c])) + alpha*(soln[q6c]) - ((soln[q6c])**2)/2 -  s*((soln[q6c])*(soln[q1c])) - s*((soln[q6c])*(soln[q2c]))- s*((soln[q6c])*(soln[q3c]))  - ((p6c)*(soln[q6c])) + alpha*(soln[q1d]) - ((soln[q1d])**2)/2 -  s*((soln[q1d])*(soln[q2d])) - s*((soln[q1d])*(soln[q7d]))  - ((p1d)*(soln[q1d])) + alpha*(soln[q2d]) - ((soln[q2d])**2)/2 -  s*((soln[q2d])*(soln[q1d])) - s*((soln[q2d])*(soln[q3d])) - s*((soln[q2d])*(soln[q7d])) - ((p2d)*(soln[q2d])) + \
    alpha*(soln[q3d]) - ((soln[q3d])**2)/2 - s*((soln[q3d])*(soln[q2d])) - s*((soln[q3d])*(soln[q7d])) - ((p3d)*(soln[q3d])) + alpha*(soln[q7d]) - ((soln[q7d])**2)/2 - s*((soln[q7d])*(soln[q1d])) - s*((soln[q7d])*(soln[q2d])) - s*((soln[q7d])*(soln[q3d])) - ((p7d)*(soln[q7d])) + alpha*(soln[q1e]) - ((soln[q1e])**2)/2 - s*((soln[q1e])*(soln[q2e])) - s*((soln[q1e])*(soln[q3e])) - s*((soln[q1e])*(soln[q8e]))  - ((p1e)*(soln[q1e])) + alpha*(soln[q2e]) - ((soln[q2e])**2)/2 -  s*((soln[q2e])*(soln[q1e]))  - s*((soln[q2e])*(soln[q8e])) - ((p2e)*(soln[q2e])) +  alpha*(soln[q3e]) - ((soln[q3e])**2)/2 -  s*((soln[q3e])*(soln[q1e])) - s*((soln[q3e])*(soln[q8e])) - ((p3e)*(soln[q3e])) + alpha*(soln[q8e]) - ((soln[q8e])**2)/2 -  s*((soln[q8e])*(soln[q1e])) - s*((soln[q8e])*(soln[q2e])) - s*((soln[q8e])*(soln[q3e])) - ((p8e)*(soln[q8e])) 
    
    
    
    
    
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
    f_double_prime_Prof1_a2 = Prof1.diff(a2, 2)
    f_double_prime_Prof2_b1 = Prof2.diff(b1, 2)
    f_double_prime_Prof2_b2 = Prof2.diff(b2, 2)
    f_double_prime_Prof2_b3 = Prof2.diff(b3, 2)
    f_double_prime_Prof3_c1 = Prof3.diff(c1, 2)
    f_double_prime_Prof3_c2 = Prof3.diff(c2, 2)
    f_double_prime_Prof4_d1 = Prof4.diff(d1, 2)
    f_double_prime_Prof4_d2 = Prof4.diff(d2, 2)
    f_double_prime_Prof4_d3 = Prof4.diff(d3, 2)
    f_double_prime_Prof5_e1 = Prof5.diff(e1, 2)
    f_double_prime_Prof5_e2 = Prof5.diff(e2, 2)
    f_double_prime_Prof5_e3 = Prof5.diff(e3, 2)
    f_double_prime_Prof6_f1 = Prof6.diff(f1, 2)
    f_double_prime_Prof6_f2 = Prof6.diff(f2, 2)
    f_double_prime_Prof6_f3 = Prof6.diff(f3, 2)
    f_double_prime_Prof7_g1 = Prof7.diff(g1, 2)
    f_double_prime_Prof7_g2 = Prof7.diff(g2, 2)
    f_double_prime_Prof7_g3 = Prof7.diff(g3, 2)
    f_double_prime_Prof8_h1 = Prof8.diff(h1, 2)
    f_double_prime_Prof8_h2 = Prof8.diff(h2, 2)
    f_double_prime_Prof8_h3 = Prof8.diff(h3, 2)
    
    
    
    
    # Compute the second derivative of the function with respect to a1, a2
    f_double_prime_Prof1_a1 = Prof1.diff(a1, 2)
    f_double_prime_Prof1_a2 = Prof1.diff(a2, 2)
    f_double_prime_Prof2_b1 = Prof2.diff(b1, 2)
    f_double_prime_Prof2_b2 = Prof2.diff(b2, 2)
    f_double_prime_Prof2_b3 = Prof2.diff(b3, 2)
    f_double_prime_Prof3_c1 = Prof3.diff(c1, 2)
    f_double_prime_Prof3_c2 = Prof3.diff(c2, 2)
    f_double_prime_Prof4_d1 = Prof4.diff(d1, 2)
    f_double_prime_Prof4_d2 = Prof4.diff(d2, 2)
    f_double_prime_Prof4_d3 = Prof4.diff(d3, 2)
    f_double_prime_Prof5_e1 = Prof5.diff(e1, 2)
    f_double_prime_Prof5_e2 = Prof5.diff(e2, 2)
    f_double_prime_Prof5_e3 = Prof5.diff(e3, 2)
    f_double_prime_Prof6_f1 = Prof6.diff(f1, 2)
    f_double_prime_Prof6_f2 = Prof6.diff(f2, 2)
    f_double_prime_Prof6_f3 = Prof6.diff(f3, 2)
    f_double_prime_Prof7_g1 = Prof7.diff(g1, 2)
    f_double_prime_Prof7_g2 = Prof7.diff(g2, 2)
    f_double_prime_Prof7_g3 = Prof7.diff(g3, 2)
    f_double_prime_Prof8_h1 = Prof8.diff(h1, 2)
    f_double_prime_Prof8_h2 = Prof8.diff(h2, 2)
    f_double_prime_Prof8_h3 = Prof8.diff(h3, 2)
    
    
    # Compute the second derivative of the function with respect to a1, a2
    # Values of n to check for concavity
    n_values = np.arange(0, 1.01, 0.01)
    
    # Check concavity for each value of n
    for n_val in n_values:
        # Substitute n with the current value .subs(n, n_val)
        f_double_prime_Prof1_a1_n = f_double_prime_Prof1_a1.subs({n: n_val})
        f_double_prime_Prof1_a2_n = f_double_prime_Prof1_a2.subs({n: n_val})
        f_double_prime_Prof2_b1_n = f_double_prime_Prof2_b1.subs({n: n_val})
        f_double_prime_Prof2_b2_n = f_double_prime_Prof2_b2.subs({n: n_val})
        f_double_prime_Prof2_b3_n = f_double_prime_Prof2_b3.subs({n: n_val})
        f_double_prime_Prof3_c1_n = f_double_prime_Prof3_c1.subs({n: n_val})
        f_double_prime_Prof3_c2_n = f_double_prime_Prof3_c2.subs({n: n_val})
        f_double_prime_Prof4_d1_n = f_double_prime_Prof4_d1.subs({n: n_val})
        f_double_prime_Prof4_d2_n = f_double_prime_Prof4_d2.subs({n: n_val})
        f_double_prime_Prof4_d3_n = f_double_prime_Prof4_d3.subs({n: n_val})
        f_double_prime_Prof5_e1_n = f_double_prime_Prof5_e1.subs({n: n_val})
        f_double_prime_Prof5_e2_n = f_double_prime_Prof5_e2.subs({n: n_val})
        f_double_prime_Prof5_e3_n = f_double_prime_Prof5_e3.subs({n: n_val})
        f_double_prime_Prof6_f1_n = f_double_prime_Prof6_f1.subs({n: n_val})
        f_double_prime_Prof6_f2_n = f_double_prime_Prof6_f2.subs({n: n_val})
        f_double_prime_Prof6_f3_n = f_double_prime_Prof6_f3.subs({n: n_val})
        f_double_prime_Prof7_g1_n = f_double_prime_Prof7_g1.subs({n: n_val})
        f_double_prime_Prof7_g2_n = f_double_prime_Prof7_g2.subs({n: n_val})
        f_double_prime_Prof7_g3_n = f_double_prime_Prof7_g3.subs({n: n_val})
        f_double_prime_Prof8_h1_n = f_double_prime_Prof8_h1.subs({n: n_val})
        f_double_prime_Prof8_h2_n = f_double_prime_Prof8_h2.subs({n: n_val})
        f_double_prime_Prof8_h3_n = f_double_prime_Prof8_h3.subs({n: n_val})
    
        # Check if the second derivatives are non-positive
        if (f_double_prime_Prof1_a1_n.is_nonpositive and f_double_prime_Prof1_a2_n.is_nonpositive
                and f_double_prime_Prof2_b1_n.is_nonpositive and f_double_prime_Prof2_b2_n.is_nonpositive
                and f_double_prime_Prof2_b3_n.is_nonpositive and f_double_prime_Prof3_c1_n.is_nonpositive
                and f_double_prime_Prof3_c2_n.is_nonpositive and f_double_prime_Prof4_d1_n.is_nonpositive
                and f_double_prime_Prof4_d2_n.is_nonpositive and f_double_prime_Prof4_d3_n.is_nonpositive
                and f_double_prime_Prof5_e1_n.is_nonpositive and f_double_prime_Prof5_e2_n.is_nonpositive
                and f_double_prime_Prof5_e3_n.is_nonpositive and f_double_prime_Prof6_f1_n.is_nonpositive
                and f_double_prime_Prof6_f2_n.is_nonpositive and f_double_prime_Prof6_f3_n.is_nonpositive
                and f_double_prime_Prof7_g1_n.is_nonpositive and f_double_prime_Prof7_g2_n.is_nonpositive
                and f_double_prime_Prof7_g3_n.is_nonpositive and f_double_prime_Prof8_h1_n.is_nonpositive
                and f_double_prime_Prof8_h2_n.is_nonpositive and f_double_prime_Prof8_h3_n.is_nonpositive):
    
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
    f_Prof4_d1 = Prof4.diff(d1)
    f_Prof4_d2 = Prof4.diff(d2)
    f_Prof4_d3 = Prof4.diff(d3)
    f_Prof5_e1 = Prof5.diff(e1)
    f_Prof5_e2 = Prof5.diff(e2)
    f_Prof5_e3 = Prof5.diff(e3)
    f_Prof6_f1 = Prof6.diff(f1)
    f_Prof6_f2 = Prof6.diff(f2)
    f_Prof6_f3 = Prof6.diff(f3)
    f_Prof7_g1 = Prof7.diff(g1)
    f_Prof7_g2 = Prof7.diff(g2)
    f_Prof7_g3 = Prof7.diff(g3)
    f_Prof8_h1 = Prof8.diff(h1)
    f_Prof8_h2 = Prof8.diff(h2)
    f_Prof8_h3 = Prof8.diff(h3)
    
    
    
    # Set first derivatives to zero and solve for a1, a2, b1, b2, b3, c1, and c2
    eq1 = f_Prof1_a1
    eq2 = f_Prof1_a2
    eq3 = f_Prof2_b1
    eq4 = f_Prof2_b2
    eq5 = f_Prof2_b3
    eq6 = f_Prof3_c1
    eq7 = f_Prof3_c2
    eq8 = f_Prof4_d1
    eq9 = f_Prof4_d2
    eq10 = f_Prof4_d3
    eq11 = f_Prof5_e1
    eq12 = f_Prof5_e2
    eq13 = f_Prof5_e3
    eq14 = f_Prof6_f1
    eq15 = f_Prof6_f2
    eq16 = f_Prof6_f3
    eq17 = f_Prof7_g1
    eq18 = f_Prof7_g2
    eq19 = f_Prof7_g3
    eq20 = f_Prof8_h1
    eq21 = f_Prof8_h2
    eq22 = f_Prof8_h3
    
    
    
    # Solve equations and store results
    solutions = sym.solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, eq11, eq12, eq13, eq14, eq15, eq16, eq17, eq18, eq19, eq20, eq21, eq22), (a1, a2, b1, b2, b3, c1, c2, d1, d2, d3, e1, e2, e3, f1, f2, f3, g1, g2, g3, h1, h2, h3))
    
    
    A1 = solutions[a1]
    A2 = solutions[a2]
    B1 = solutions[b1]
    B2 = solutions[b2]
    B3 = solutions[b3]
    C1 = solutions[c1]
    C2 = solutions[c2]
    D1 = solutions[d1]
    D2 = solutions[d2]
    D3 = solutions[d3]
    E1 = solutions[e1]
    E2 = solutions[e2]
    E3 = solutions[e3]
    F1 = solutions[f1]
    F2 = solutions[f2]
    F3 = solutions[f3]
    G1 = solutions[g1]
    G2 = solutions[g2]
    G3 = solutions[g3]
    H1 = solutions[h1]
    H2 = solutions[h2]
    H3 = solutions[h3]
    
    
    print("Solutions for a1, b2, c3, d4, e1, e5, e6, e7, e8, f2, f5, f6, f7, f8, g3, g5, g6, g7, g8, h4, h5, h6, h7, h8:")
    print("A1:", A1)
    print("A2:", A2)
    print("B1:", B1)
    print("B2:", B2)
    print("B3:", B3)
    print("C1:", C1)
    print("C2:", C2)
    print("D1:", D1)
    print("D2:", D2)
    print("D3:", D3)
    print("E1:", E1)
    print("E2:", E2)
    print("E3:", E3)
    print("F1:", F1)
    print("F2:", F2)
    print("F3:", F3)
    print("G1:", G1)
    print("G2:", G2)
    print("G3:", G3)
    print("H1:", H1)
    print("H2:", H2)
    print("H3:", H3)
    
    
    
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
        print("D1 =", D1.subs(n, n_val))
        print("D2 =", D2.subs(n, n_val))
        print("D3 =", D3.subs(n, n_val))
        print("E1 =", E1.subs(n, n_val))
        print("E2 =", E2.subs(n, n_val))
        print("E3 =", E3.subs(n, n_val))
        print("F1 =", F1.subs(n, n_val))
        print("F2 =", F2.subs(n, n_val))
        print("F3 =", F3.subs(n, n_val))
        print("G1 =", G1.subs(n, n_val))
        print("G2 =", G2.subs(n, n_val))
        print("G3 =", G3.subs(n, n_val))
        print("H1 =", H1.subs(n, n_val))
        print("H2 =", H2.subs(n, n_val))
        print("H3 =", H3.subs(n, n_val))
    
    
    
    ##########################################################
    
    

    
    
    # Define your function as the sum of 4 symbolic expressions
    Prof1_rep = Prof1.subs(a1, solutions[a1]).subs(a2, solutions[a2]).subs(b1, solutions[b1]).subs(b2, solutions[b2]).subs(b3, solutions[b3]).subs(c1, solutions[c1]).subs(c2, solutions[c2]).subs(d1, solutions[d1]).subs(d2, solutions[d2]).subs(d3, solutions[d3]).subs(e1, solutions[e1]).subs(e2, solutions[e2]).subs(e3, solutions[e3]).subs(f1, solutions[f1]).subs(f2, solutions[f2]).subs(f3, solutions[f3]).subs(g1, solutions[g1]).subs(g2, solutions[g2]).subs(g3, solutions[g3]).subs(h1, solutions[h1]).subs(h2, solutions[h2]).subs(h3, solutions[h3])
    Prof2_rep = Prof2.subs(a1, solutions[a1]).subs(a2, solutions[a2]).subs(b1, solutions[b1]).subs(b2, solutions[b2]).subs(b3, solutions[b3]).subs(c1, solutions[c1]).subs(c2, solutions[c2]).subs(d1, solutions[d1]).subs(d2, solutions[d2]).subs(d3, solutions[d3]).subs(e1, solutions[e1]).subs(e2, solutions[e2]).subs(e3, solutions[e3]).subs(f1, solutions[f1]).subs(f2, solutions[f2]).subs(f3, solutions[f3]).subs(g1, solutions[g1]).subs(g2, solutions[g2]).subs(g3, solutions[g3]).subs(h1, solutions[h1]).subs(h2, solutions[h2]).subs(h3, solutions[h3])
    Prof3_rep = Prof3.subs(a1, solutions[a1]).subs(a2, solutions[a2]).subs(b1, solutions[b1]).subs(b2, solutions[b2]).subs(b3, solutions[b3]).subs(c1, solutions[c1]).subs(c2, solutions[c2]).subs(d1, solutions[d1]).subs(d2, solutions[d2]).subs(d3, solutions[d3]).subs(e1, solutions[e1]).subs(e2, solutions[e2]).subs(e3, solutions[e3]).subs(f1, solutions[f1]).subs(f2, solutions[f2]).subs(f3, solutions[f3]).subs(g1, solutions[g1]).subs(g2, solutions[g2]).subs(g3, solutions[g3]).subs(h1, solutions[h1]).subs(h2, solutions[h2]).subs(h3, solutions[h3])
    Prof4_rep = Prof4.subs(a1, solutions[a1]).subs(a2, solutions[a2]).subs(b1, solutions[b1]).subs(b2, solutions[b2]).subs(b3, solutions[b3]).subs(c1, solutions[c1]).subs(c2, solutions[c2]).subs(d1, solutions[d1]).subs(d2, solutions[d2]).subs(d3, solutions[d3]).subs(e1, solutions[e1]).subs(e2, solutions[e2]).subs(e3, solutions[e3]).subs(f1, solutions[f1]).subs(f2, solutions[f2]).subs(f3, solutions[f3]).subs(g1, solutions[g1]).subs(g2, solutions[g2]).subs(g3, solutions[g3]).subs(h1, solutions[h1]).subs(h2, solutions[h2]).subs(h3, solutions[h3])
    Prof5_rep = Prof5.subs(a1, solutions[a1]).subs(a2, solutions[a2]).subs(b1, solutions[b1]).subs(b2, solutions[b2]).subs(b3, solutions[b3]).subs(c1, solutions[c1]).subs(c2, solutions[c2]).subs(d1, solutions[d1]).subs(d2, solutions[d2]).subs(d3, solutions[d3]).subs(e1, solutions[e1]).subs(e2, solutions[e2]).subs(e3, solutions[e3]).subs(f1, solutions[f1]).subs(f2, solutions[f2]).subs(f3, solutions[f3]).subs(g1, solutions[g1]).subs(g2, solutions[g2]).subs(g3, solutions[g3]).subs(h1, solutions[h1]).subs(h2, solutions[h2]).subs(h3, solutions[h3])
    Prof6_rep = Prof6.subs(a1, solutions[a1]).subs(a2, solutions[a2]).subs(b1, solutions[b1]).subs(b2, solutions[b2]).subs(b3, solutions[b3]).subs(c1, solutions[c1]).subs(c2, solutions[c2]).subs(d1, solutions[d1]).subs(d2, solutions[d2]).subs(d3, solutions[d3]).subs(e1, solutions[e1]).subs(e2, solutions[e2]).subs(e3, solutions[e3]).subs(f1, solutions[f1]).subs(f2, solutions[f2]).subs(f3, solutions[f3]).subs(g1, solutions[g1]).subs(g2, solutions[g2]).subs(g3, solutions[g3]).subs(h1, solutions[h1]).subs(h2, solutions[h2]).subs(h3, solutions[h3])
    Prof7_rep = Prof7.subs(a1, solutions[a1]).subs(a2, solutions[a2]).subs(b1, solutions[b1]).subs(b2, solutions[b2]).subs(b3, solutions[b3]).subs(c1, solutions[c1]).subs(c2, solutions[c2]).subs(d1, solutions[d1]).subs(d2, solutions[d2]).subs(d3, solutions[d3]).subs(e1, solutions[e1]).subs(e2, solutions[e2]).subs(e3, solutions[e3]).subs(f1, solutions[f1]).subs(f2, solutions[f2]).subs(f3, solutions[f3]).subs(g1, solutions[g1]).subs(g2, solutions[g2]).subs(g3, solutions[g3]).subs(h1, solutions[h1]).subs(h2, solutions[h2]).subs(h3, solutions[h3])
    Prof8_rep = Prof8.subs(a1, solutions[a1]).subs(a2, solutions[a2]).subs(b1, solutions[b1]).subs(b2, solutions[b2]).subs(b3, solutions[b3]).subs(c1, solutions[c1]).subs(c2, solutions[c2]).subs(d1, solutions[d1]).subs(d2, solutions[d2]).subs(d3, solutions[d3]).subs(e1, solutions[e1]).subs(e2, solutions[e2]).subs(e3, solutions[e3]).subs(f1, solutions[f1]).subs(f2, solutions[f2]).subs(f3, solutions[f3]).subs(g1, solutions[g1]).subs(g2, solutions[g2]).subs(g3, solutions[g3]).subs(h1, solutions[h1]).subs(h2, solutions[h2]).subs(h3, solutions[h3])
    
    
    #change utility depending on s
    Utility_rep = Utility.subs(a1, solutions[a1]).subs(a2, solutions[a2]).subs(b1, solutions[b1]).subs(b2, solutions[b2]).subs(b3, solutions[b3]).subs(c1, solutions[c1]).subs(c2, solutions[c2]).subs(d1, solutions[d1]).subs(d2, solutions[d2]).subs(d3, solutions[d3]).subs(e1, solutions[e1]).subs(e2, solutions[e2]).subs(e3, solutions[e3]).subs(f1, solutions[f1]).subs(f2, solutions[f2]).subs(f3, solutions[f3]).subs(g1, solutions[g1]).subs(g2, solutions[g2]).subs(g3, solutions[g3]).subs(h1, solutions[h1]).subs(h2, solutions[h2]).subs(h3, solutions[h3])
    
    
    
    f = Prof1_rep + Prof2_rep + Prof3_rep + Prof4_rep + Prof5_rep + Prof6_rep + Prof7_rep + Prof8_rep + Utility_rep
    f_rep = f.subs(a1, solutions[a1]).subs(a2, solutions[a2]).subs(b1, solutions[b1]).subs(b2, solutions[b2]).subs(b3, solutions[b3]).subs(c1, solutions[c1]).subs(c2, solutions[c2]).subs(d1, solutions[d1]).subs(d2, solutions[d2]).subs(d3, solutions[d3]).subs(e1, solutions[e1]).subs(e2, solutions[e2]).subs(e3, solutions[e3]).subs(f1, solutions[f1]).subs(f2, solutions[f2]).subs(f3, solutions[f3]).subs(g1, solutions[g1]).subs(g2, solutions[g2]).subs(g3, solutions[g3]).subs(h1, solutions[h1]).subs(h2, solutions[h2]).subs(h3, solutions[h3])
    print(f_rep)
    
    #from sympy import simplify (we stopped simplify to be faster)
    f_simp=f_rep
    
    import matplotlib.pyplot as plt
    
    
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
plt.title('Multiple Products Network | b∈[0,1]')
plt.xlabel('b')
plt.ylabel('γ*')
plt.show() 