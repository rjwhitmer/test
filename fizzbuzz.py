def fizzbuzz(x):
	if is_divisible(x, 3) and is_divisible(x, 5):
		return("fizzbuzz")
	elif is_divisible(x, 3):
		return("fizz")
	elif is_divisible(x, 5):
		return("buzz")
	else:
		return (x)
	return ''

def is_divisible(x, y):
	if x%y==0:
		return True
	else:
		return False

def main():
	x=1
	while x<101:
		print(fizzbuzz(x))
		x+=1

if __name__ == '__main__':
    main()