# Create, Encrypt, Store
Password creation and encryption algorithms

## Getting Started

These instructions will walk you through the process of running this application in order to create a password with 
customised qualities, encrypt the password and guide you through what data to keep private. We will then talk about how to 
then decrypt and use the password when it's time to log in to your chosen website or application.

### Prerequisites

I am running Python 3.7.3 for this application and using modules 'random', 'string' and 'time' which are all easily imported
within relevant scripts we will be using.

To check which version of Python you are using, open your terminal (I am using Windows Powershell), type 'py' and hit ENTER

```
C:\Users\kenan>py
Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
```

I am using the Anaconda environment but in Windows Powershell you should still see the same thing. Other versions of Python 3 are
supported with this application and the packages we will be using are included within Python's default modules. Let's begin making
some passwords!

Clone this repository in your chosen directory and run the 'create_encrypt_store.py' file by running the following command 
to get started.

```
C:\Users\kenan\mystuff\projects\create_encrypt_store\Create-Encrypt-Store\docs> py create_encrypt_store.py
```

You will then be prompted with the following message:

```
Please select an option.

1. Create, encrypt and store
2. Decrypt
>  
```

### Creating, Encrypting and Storing

We type '1' and press ENTER and enter the custom paramaters for our password. For simplicity I'll just go for a basic one:

```
Welcome to the Password Encryption programme.
Please describe what kind of password you need.
has_uppercase =
        1. True
        2. False
> 1
has_symbols =
        1. True
        2. False
> 2
has_numbers =
        1. True
        2. False
> 2
password_length =
```

We're then asked about what length password we would like. I'll choose a password of length 8, so I type '8' and press ENTER:

```
password_length = 8
Your new password is: FnaaWmIb
Please copy your password from the terminal. We will now
encrypt. Please ENTER a key between 1-26 and store it privately.
```

We are then given our password and told to copy the password from the terminal. We are then prompted to enter a key between 1-26.
This key will be used to encrypt the password before it is stored in our text file 'words.txt'. We'll say 13 and press ENTER. We
are then prompted to paste the password into the terminal and tell the terminal what website or application our password will be for.
Let's say it's for Groupon and press ENTER.

```
Please re-enter your new password by pasting it below.
> Pass: FnaaWmIb
We will now encrypt your new password.
Your encrypted password is:  SannJzVo
What will this password be for?
> Place: Groupon
```

Upon pressing ENTER, the programme will tell us:

```
Thankyou for using this programme. Your password is now encrypted and stored.
You must keep privately the key '13' along with 'Groupon' and the Id number 57366
```

So our private log (which is highly recommended to keep off of our computers on a piece of paper) will look like this:
```
13, 57366, Groupon
```

Whilst our words.txt file (which is where the encrypted passwords are stored) will keep the following data:

```
Pass: SannJzVo
Id: 57366
```

Congratulations, we have now created and stored our Groupon password! Notice how the digital component is encrypted and 
does not give away what the password is made for. So how do we retrieve our password?

### Decrypting

Let's decrypt the password we made in the above section. Run the programme again, but this time we wil select the second option.
We input our Id number and Secret Key:

```
Please select an option.

1. Create, encrypt and store
2. Decrypt
> 2
So you'd like to decrypt your password...
Please enter the Id number followed by your secret key.
Id: 57366
Secret Key: 13
```

We then find the encrypted password associated with the Id '57366' in our words.txt file and paste it into the terminal as follows.

```
Please find the associated password with '57366' and paste it below.
Pass: SannJzVo
Your password is 'FnaaWmIb',
thank you for using this programme.
```

Notice how the output password is the same as our password before we encrypted it in the last section. 

## Acknowledgements

Please see the (random password)[https://github.com/gitkenan/Random-Password] and (Caesar shift)[https://github.com/gitkenan/Caesar_shift] script documentations for more details on the components of this project. 
This project uses these two scripts to encrypt information using the Caesar cipher and uses my Random Password Generator script.

