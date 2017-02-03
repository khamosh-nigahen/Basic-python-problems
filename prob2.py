
num = int(raw_input("Enter the number for which you want to find a factorial"))

def fact(x):
    if x == 0:
	return 1;
    return x * fact(x-1)

print fact(num)

