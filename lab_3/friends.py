"""composition"""
class C_Door:
    def open(self):
        print("Opening...")

class C_FireproofDoor:
    def open(self):    
        door = C_Door()
        door.open()
        
    def protect(self):
        print("Door is protected")
        
        
"""inheritance"""
class I_Door:
    def open(self):
        print("Opening...")


class I_FireproofDoor(I_Door):
    def protect(self):
        print("Door is protected")

        
if __name__ == "__main__":
    print("composition:")
    c = C_FireproofDoor()
    c.open()
    c.protect()
    print("---")
    print("inheritance:")
    i = I_FireproofDoor()
    i.open()
    i.protect()