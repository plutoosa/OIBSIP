import random
import string

password_length = int(input("Enter your desired password length: "))

#print menu
print (''' Choose characters you want in your password:
       1. Letters
       2. Digits
       3. Special characters
       4. Exit
       ''')

#initialise character list
character_list = ""
#takes menu answers
while(True):
    choice = int(input("Pick your choice: "))
    if(choice == 1):
        #adds letters to the characters possible for the password
        character_list += string.ascii_letters
    elif(choice == 2):
        character_list += string.digits
    elif(choice == 3):
        character_list += string.punctuation
    elif(choice == 4):
        break
    
genPassword = []

for i in range(password_length):
    
    #randomises the password generation
    randomChar = random.choice(character_list)
    
    #appends
    genPassword.append(randomChar)
    
print("The generated password is "  + "".join(genPassword))
    
    
    