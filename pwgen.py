import string
import random

def gen():
	s1 = string.ascii_uppercase
	s2 = string.ascii_lowercase
	s3 = string.digits
	s4 = string.punctuation

	pwLength = int(input("Enter password length: "))

	s = []
	s.extend(s1)
	s.extend(s2)
	s.extend(s3)
	s.extend(s4)

	random.shuffle(s)
	pw = "".join(s[0:pwLength])
	print(pw)

gen()