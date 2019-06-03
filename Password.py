# importing re library
import re

def main():
	passwd = input("Enter the Password: ")
	reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

	# compiling regex
	comp = re.compile(reg)

	# searching regex
	sear = re.search(comp, passwd)

	# validating conditions
	if sear:
		print("Password is valid.")
	else:
		print("Password invalid !!")

# Driver Code
if __name__ == '__main__':
	main()
