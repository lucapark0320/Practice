import math

def factorial(n):
    if n < 0:
        return "Error: Negative factorial"
    return math.factorial(n)

def log_base(x, base):
    if x <= 0 or base <= 0:
        return "Error: Invalid input for log"
    return math.log(x, base)

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        return -b / (2*a)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2

def solve_cubic(a, b, c, d):
    # Using Cardano's method
    f = ((3*c/a) - ((b**2)/(a**2))) / 3
    g = ((2*(b**3)/(a**3)) - (9*b*c/(a**2)) + (27*d/a)) / 27
    h = (g**2)/4 + (f**3)/27

    if h > 0:
        R = -(g/2) + math.sqrt(h)
        S = math.copysign(abs(R)**(1/3), R)
        T = -(g/2) - math.sqrt(h)
        U = math.copysign(abs(T)**(1/3), T)
        root1 = (S + U) - (b/(3*a))
        return (root1,)
    else:
        i = math.sqrt(((g**2)/4) - h)
        j = i**(1/3)
        k = math.acos(-(g/(2*i)))
        L = -j
        M = math.cos(k/3)
        N = math.sqrt(3) * math.sin(k/3)
        P = -(b/(3*a))
        root1 = 2*j*math.cos(k/3) - (b/(3*a))
        root2 = L*(M+N) + P
        root3 = L*(M-N) + P
        return root1, root2, root3

# 테스트
print("5! =", factorial(5))
print("log2(8) =", log_base(8, 2))
print("Quadratic 1x^2 + 0x - 4 =", solve_quadratic(1, 0, -4))