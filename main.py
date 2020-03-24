# ---------------------------------
# OPERATORS
# ---------------------------------

num_1 = 10
num_2 = 4

sum_result = num_1 + num_2
subs_result = num_1 - num_2
mult_result = num_1 * num_2

# We have 3 types of division operators

# Full division
full_div_result = num_1 / num_2  # we would get 2.5
integer_div_result = num_1 // num_2  # we would get 2
mod_div_result = num_1 % num_2  # we would get 2 which is the reminder

# Lets check an example of how we can use the modulus (Get the reminder of a division)
# How do I check if a number is even or odd

is_even_result = 13 % 2


# There are derived operators for example:

# Power x^n
x = 2
n = 3
power_result = x ** n


# ---------------------------------
# SIMPLE FUNCTIONS
# ---------------------------------
def power(px, pn):
    return float(px) ** pn


def sqr_root(px):
    return power(px=px, pn=(1/2))


def discriminant(a, b, c):
    return power(b, 2) - (4 * a * c)


def compute_x1(a, b, c):
    return ((-1 * b) - sqr_root(discriminant(a, b, c))) / 2 * a


def compute_x2(a, b, c):
    return ((-1 * b) + sqr_root(discriminant(a, b, c))) / 2 * a


print('x1 = {}'.format(compute_x1(1, -1, -2)))
print('x2 = {}'.format(compute_x2(1, -1, -2)))
# x = -1
# x = 2





