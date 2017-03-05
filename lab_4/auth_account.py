import auth

auth.authenticator.add_user("admin", "adminadmin")
auth.authenticator.add_user("moder1", "123456")
auth.authorizor.add_permission("test")
auth.authorizor.add_permission("change")

auth.authorizor.permit_user("test", "admin")
auth.authorizor.permit_user("change", "admin")
auth.authorizor.permit_user("test", "moder1")

class Editor:
    def __init__(self):
        self.username = None
        self.menu_map ={
            "login": self.login,
            "change": self.change,
            "test": self.test,
            "quit": self.quit,
        }
    
    def login(self): 
        if self.username is not None:
            print("logging out...")
            print("succesfuly logged out!")
        logged_in = False
        print("leave line empty to cancel")
        while not logged_in:
            username = input("username: ")
            password = input("password: ") 
            if not username or not password:
                break
            try:
                logged_in = auth.authenticator.login(username, password)
            except (auth.InvalidUsername, auth.InvalidPassword):
                print("sorry, invalid data")
            else:
                self.username = username
                print("login successful, {}!".format(username))
    
    def is_permitted(self, permission):
        try:
            auth.authorizor.check_permission(permission, self.username)
        except auth.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except auth.PermissionError as e:
            print("{} permission does not exist".format(permission))
            return False
        except auth.NotPermittedError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True
            
            
    def test(self):
        if self.is_permitted("test"):
            print("testing program...")
            
    def change(self):
        if self.is_permitted("change"):
            print("changing program...")
            
    def register(self):
        register = False
        while not register:
            username = input("username: ")
            if username == "exit":
                print("you are not register!")
                return
            password = input("password: ")
            try:
                register = auth.authenticator.add_user(username, password)
            except auth.UsernameAlreadyExists:
                print("sorry, username already exists")
            except auth.PasswordTooShort:
                print("sorry, password too short")
            else:
                print("register successful, {}!".format(username))
                      
    def quit(self):
        Editor().menu()     
        
    def menu(self):
        try:
            ans = ""
            while True:
                print("available commands:\n login, change, test, quit")
                ans = input(">>? ")
                try:
                    func = self.menu_map[ans]
                except KeyError:
                    print("command not found")
                else:
                    func()
        
        finally:
            print("thanks for using my login service")
            
Editor().menu()       
                