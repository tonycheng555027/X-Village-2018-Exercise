import re


class AuthSystem:

    
    def __init__(self):
        """Define regex"""
        self.username_regex = re.compile(r'[A-Z][a-z][a-z]')
        self.password_regex = re.compile(r'[a-z][a-z][a-z][0][0-9][0-9][0-9][0-9][0-9]')
    
    def _check_username(self, username):
        """Check username is valid or not"""
        if self.username_regex.search(username) is not None:
            print("Correct username")
            return True
        else: 
            print("Username format error! Your username is"+' '+username)
            return False
        
    def _check_password(self, password):
        """Check password is valid or not"""
        if self.password_regex.search(password) is not None:
            print("Correct password")
            return True
        else:
            print("Password format error! Your password is"+' '+password)
            return False
        
    def authenticate(self, username, password):
        """authenticate the user"""
        if not self._check_username(username):
            return
        
        if not self._check_password(password):
            return
        
        print("Welcome, "+username+"!")

a=input('輸入帳號:')
b=input('輸入密碼:')
auth = AuthSystem()
if len(a)>3 or len(a)<3:
    print('Username legnth error! Your username length is'+' '+ str(len(a))+'.')
elif len(b)>9 or len(b)<9:
        print('Password legnth error! Your password length is'+' '+ str(len(b))+'.')
else:
    auth.authenticate(a, b)    
# Construct a object of type AuthSystem


# authenticate the user's credentials

