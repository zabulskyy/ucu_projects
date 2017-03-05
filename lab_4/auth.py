import hashlib

class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user

class UsernameAlreadyExists(AuthException):
    pass
   
class PasswordTooShort(AuthException):
    pass
    
class InvalidUsername(AuthException):
    pass
    
class InvalidPassword(AuthException):
    pass

    
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self.encrypt_pw(password)
        self.is_logged_in = False
        
    def encrypt_pw(self, password):
        hash_string = (self.username + password)
        hash_string = hash_string.encode("utf-8")
        return hashlib.sha256(hash_string).hexdigest()
        
    def check_password(self, password):
        encrypted = self.encrypt_pw(password)
        return encrypted == self.password

        
class Authenticator:
    def __init__(self):
        self.users = {}
        
    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)
        return True
        
    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)
        if not user.check_password(password):
            raise InvalidPassword(username, user)
            
        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        if type(username) != str:
            return False
        if username in self.users:
            return self.users[username].is_logged_in
        return False
        
authenticator = Authenticator()
        
        
class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}
        
    def add_permission(self, perm_name):
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission exists")
        
    def permit_user(self, perm_name, username):
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername("username")
            perm_set.add(username)
            
    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True


class NotLoggedInError(AuthException):
    pass
    
class NotPermittedError(AuthException):
    pass
            
class PermissionError(Exception):
    pass
    
authorizor = Authorizor(authenticator)        


            