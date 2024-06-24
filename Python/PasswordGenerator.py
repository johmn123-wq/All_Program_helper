'''Password Generator
Given the password length as input, program  will generate a random password (length 8-32 char)
Example:
Input: 8
Output: bY62+oP_
'''
pw_length = int(input('Please enter your desired password length (between 8 and 32 characters).\n'))
def pw_gen(pw_length):
    if pw_length > 32 or pw_length < 8:
        print ("Password length must be between 8 and 32 characters")
    else:
        import secrets #instead of just using random for a pw https://docs.python.org/3/library/secrets.html
        import string
        pw = ''.join(secrets.choice(string.hexdigits + string.punctuation) for _ in range(pw_length))
    #Seems very heavy on special characters when using this. Can narrow character field using string module constants, such as only upper (string.ascii_uppercase) or lower string.ascii_lowercase or string.digits
        print ("Your randomly generated password is: %s" % pw)
pw_gen(pw_length)
