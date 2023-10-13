# For Loop with Else

# Else is executed only when the loop is successfully executed, not when the loop is terminated by a break statement.

for i in range(4):
    print(i)
else:
    print("Loop Ended...")  # will get executed

# Using a break statement in the loop will prevent the else statement from being executed.

print("\nwith break keyword")
for i in range(4):
    print(i)
    if i == 3:
        break
else:
    print("Loop Ended...")  # will not get executed
print("\n")

# using `while` loop

i = 1

while i <= 4:
    print(i)
    i += 1
else:
    print("WHILE LOOP ENDED SUCCESSFULLY...")  # will get executed

# using `while` loop with `break` keyword

i = 5

print("\nwith break keyword")
while i > 0:
    print(i)
    if i == 2:
        break
    i -= 1
else:
    print("WHILE LOOP ENDED SUCCESSFULLY...")  # will not get executed
