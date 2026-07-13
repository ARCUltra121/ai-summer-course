counter = 0
for i in range(1,16):
    print(str(i), end=' ')

print()

for i in range(2, 31, 2):
    print(str(i), end=' ')

print()

for i in range(20, -2, -2):
    print(i, end =' ')
print()

num_start = int(input("What is the start number? "))
num_stop = int(input("What is the stop number? ")) + 1
num_step = int(input("What is the step number? "))

for i in range(num_start, num_stop, num_step):
    print(i, end=' ')
print()
