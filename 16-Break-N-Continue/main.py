
#? What is `continue` and `break` in Python?
#* `continue` is used to skip the current iteration of a loop and continue with the next iteration.
#* `break` is used to exit a loop.

#? `break` example
for index in range(11):
    if index == 10:
        break; #? This will break the loop when the index is 10.
    print("5 X", (index + 1), "=", (index + 1) * 5); #? Here, I'm adding one to the index because the index starts from 0. So, 0 + 1 = 1, 1 + 1 = 2, 2 + 1 = 3, and so on.

print("\n\n");

#? `continue` example
for index in range(11):
    if index == 9:
        print("Skipping the iteration when the index is", index, "...");
        continue; #? This will skip the iteration when the index is 10.
    print("5 X", (index + 1), "=", (index + 1) * 5);

print("\n==========================================");
print("Table of 1 to 10".center(40));
print("==========================================\n")

for i in range(1, 11):
    for j in range(1, 11):
        print(i, "X", j, "=", (i * j)); 
    print("\n");