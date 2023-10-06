
#? Define Operators

#! Arithmetic Operators
#? + Addition
#? - Subtraction
#? * Multiplication
#? / Division
#? // Floor Division
#? % Modulus
#? ** Exponent

#! Assignment Operators
#? = Assign
#? += Add and Assign
#? -= Subtract and Assign
#? *= Multiply and Assign
#? /= Divide and Assign

#! Comparison Operators
#? == Equal to
#? != Not equal to
#? > Greater than
#? < Less than
#? >= Greater than or equal to
#? <= Less than or equal to

#! Logical Operators
#? and
#? or
#? not

#! Identity Operators
#? is
#? is not

#! Membership Operators
#? in
#? not in

#? Optional (Good to know)
#* Bitwise Operators
#? & AND
#? | OR
#? ^ XOR
#? ~ NOT
#? << Zero fill left shift
#? >> Signed right shift


#? Examples
#? Arithmetic Operators
print(5 + 5) # 10
print(10 - 5) # 5
print(5 * 5) # 25
print(10 / 5) # 2.0
print(10 // 5) # 2
print(10 % 5) # 0
print(5 ** 5) # 3125

#? Assignment Operators
x = 5
print(x) # 5

x += 5
print(x) # 10

x -= 5
print(x) # 5

x *= 5
print(x) # 25

x /= 5
print(x) # 5.0

#? Comparison Operators
print(5 == 5) # True
print(5 != 5) # False
print(5 > 5) # False
print(5 < 5) # False
print(5 >= 5) # True
print(5 <= 5) # True

#? Logical Operators
print(True and True) # True
print(True and False) # False
print(False and False) # False

print(True or True) # True
print(True or False) # True
print(False or False) # False

print(not True) # False
print(not False) # True

#? Identity Operators
x = 5
y = 5
z = 10

print(x is y) # True
print(x is z) # False
print(x is not y) # False

#? Membership Operators
x = [1, 2, 3, 4, 5]

print(1 in x) # True
print(6 in x) # False
print(1 not in x) # False
print(6 not in x) # True

