from sympy import symbols

a1, a2, b1, b2, b3, c1, c2, q1, q2, q3, n, a, b, c = symbols('a1 a2 b1 b2 b3 c1 c2 q1 q2 q3 n a b c')

# Define the first derivative of the function (expr=profits)
expr=(-0.676470588235294*a1*n + 0.11764705882353*a1 - 0.294117647058823*a2*n + 0.11764705882353*a2 - 0.264705882352941*b1*n - 0.294117647058823*b1 + 0.11764705882353*b2*n - 0.294117647058823*b2 - 0.294117647058823*b3 - 0.176470588235294*c1*n - 0.38235294117647*c1 - 0.38235294117647*c2 + 7.20588235294117)*(0.323529411764706*a1*n + 0.117647058823529*a1 - 0.294117647058824*a2*n + 0.117647058823529*a2 + 0.735294117647059*b1*n - 0.294117647058824*b1 + 0.117647058823529*b2*n - 0.294117647058824*b2 - 0.294117647058824*b3 - 0.176470588235294*c1*n + 0.617647058823529*c1 + 0.617647058823529*c2 + 2.20588235294118) - (5 - (c1) - (c2) - ((n)*(b1)) - ((n)*(a1)))*(0.323529411764706*a1*n + 0.117647058823529*a1 - 0.294117647058824*a2*n + 0.117647058823529*a2 + 0.735294117647059*b1*n - 0.294117647058824*b1 + 0.117647058823529*b2*n - 0.294117647058824*b2 - 0.294117647058824*b3 - 0.176470588235294*c1*n + 0.617647058823529*c1 + 0.617647058823529*c2 + 2.20588235294118) - 4*c1**2 - 4*c2**2



f_prime = expr

# Compute the second derivative of the function with respect to a,b,c
f_double_prime = f_prime.diff(c2, 2)

# Values of n to check for concavity
n_values = [0, 1, 0.2, 0.5, 0.8]

print("Second derivative of the function with respect to c2")
print(f_double_prime)

# Check concavity for each value of n
for n_val in n_values:
    # Substitute n with the current value
    f_double_prime_n = f_double_prime.subs(n, n_val)
    
    # Check if the second derivative is non-positive
    if f_double_prime_n.is_nonpositive:
        print(f"The function is concave with respect to c2 for n = {n_val}")
    else:
        print(f"The function is not concave with respect to c2 for n = {n_val}")
