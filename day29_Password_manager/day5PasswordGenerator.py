#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)
print(nr_letters, nr_symbols, nr_symbols)

#We can shuffle a list but not a string .
# Hence we form a Lis tand Shuffle it 
#Then convert the list into a String
password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

print("Password before shuffle", password_list)
random.shuffle(password_list)
#The shuffle() method in the random module is used to shuffle a list. 
# It takes a sequence, such as a list, and reorganizes the order of the 
# items. This shuffle() method changes the original list, it does not 
# return a new list. 
# The ordering of lists is lost in this process which is the only drawback 
# of this method

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")