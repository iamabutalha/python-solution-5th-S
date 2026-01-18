
def strong_password(password):
    if(len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password)):
        print("Strong pass")
    else:
        print("Weak Password")


strong_password("Helloworkdkaddkakd222")