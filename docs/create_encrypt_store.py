import caesar_shift as cs
import password_gen
import time
import random



def main():
    print("""Please select an option.

1. Create, encrypt and store
2. Decrypt""")
    
    initial_action = str(input("> "))

    if initial_action == "1":
        password_file = open("words.txt", 'a+')

        print("""Welcome to the Password Encryption programme.
Please describe what kind of password you need.""")
        password_ = ' '
        a, b, c = 0, 0, 0
        password_gen.main()

        print("""Please copy your password from the terminal. We will now 
encrypt. Please ENTER a key between 1-26 and store it privately.""") 

        time.sleep(3)

        key = input("> ")

        print("""Please re-enter your new password by pasting it below.""")

        pasted_pass = input('> Pass: ')

        print("""We will now encrypt your new password.""")

        pasted_pass = cs.Caesar_shift(pasted_pass, key)
        print('Your encrypted password is: ', pasted_pass)
        
        print("""What will this password be for?""")

        purpose = input('> Place: ')
        identifier = random.randint(10000, 99999)

        while str(identifier) in password_file:
            identifier = random.randint(1000, 9999)

        print("""Please keep the following information secret:
%r, %r, %r""" % (key, identifier, purpose))

        password_file = open("words.txt", 'a')

        password_file.write('Pass: ' + str(pasted_pass) + '\n')
        password_file.write('Id: ' + str(identifier) + '\n \n')
        password_file.close()

        print("""Thankyou for using this programme. Your password is now encrypted and stored.
You must keep privately the key %r along with %r and the Id number""" % (key, purpose), identifier)

    elif initial_action == "2":
        print("""So you'd like to decrypt your password...
Please enter the Id number followed by your secret key.""")

        id_number = input('Id: ')
        secret_key = input('Secret key: ')
        
        # this needs editing
        print("""Please find the associated password with %r and paste it below.""" % id_number)
        password2 = input("Pass: ")

        # decrypt password
        password2 = cs.Caesar_shift(str(password2), - int(secret_key))

        print("""Your password is %r, 
thank you for using this programme.""" % password2)
    else:
        print("""This is not an option. Please type '1' or '2' to proceed.""")
        main()


if __name__ == '__main__':
    main()
else:
    pass