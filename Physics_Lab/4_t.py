import sympy

def Tmin(a_star):
    # Define the variables and the function to be optimized
    a, T = sympy.symbols('a T')
    f = T**2 * sympy.exp(-a*T)
    
    # Take the first derivative with respect to a
    dfda = sympy.diff(f, a)
    
    # Set the derivative equal to zero and solve for T
    T_star = sympy.solve(dfda, T)[0]
    
    # Evaluate T_star at a_star to get the value of Tmin
    Tmin = T_star.subs(a, a_star)
    
    return Tmin

# Example usage: calculate Tmin for a* = 0.5
print(Tmin(0.5))