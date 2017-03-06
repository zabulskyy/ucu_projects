from document import *

request = ''
commands = [ 'help', 'new', 'save', 'add', 'del', 'show', 'back', 'forward', 'end', 'home', 'cursor pos', 'rename']
saved = False

document = Document()
document.set_name('choose name of your file: ')
print('new document created')

while True:
    command = input('?>> ')
    if command not in commands:
        print("No such command: {}".format(command))
        
    elif command.lower() == 'help':
        print("available commands:")
        for i in commands:
            print(i)
            
    elif command.lower() == 'new':
        if not saved:
            sure = input('do you want to save document before creating new? (yes, no): ')
            if sure.lower() == 'yes':
                sure = True 
            else:
                sure = False
            if sure:
                document.save()
                print('saved successfully')
                document = Document()
                document.set_name('choose name of your file: ')
                saved = False
            else:
                document = Document()
                document.set_name('choose name of your file: ')
                saved = False
        
        else:
            document = Document()
            saved = False
        print('new document created')
            
    elif command.lower() == 'save':
        try:
            document.save()
            print('saved successfully')
            saved = True
        except InvalidSave:
            print('can not save file without name')
        
    elif command.lower() == 'rename':
        document.set_name('choose name of your file: ')
        
    elif command.lower() == 'add':
        try:
            char = input("type character: ")
            
            document.insert(char)
        except InvalidCharacter:
            print('can not add more than one character per once')
            
    elif command.lower() == 'del':
        try:
            document.delete()
        except InvalidDelete:
            print('can not delete character on this position')
            
    elif command.lower() == 'show':
        print(document.string)
        
    elif command.lower() == 'back':
        try:
            document.cursor.back()
        except CursorOutOfFileBack:
            print('cursor out of file')
            
    elif command.lower() == 'forward':
        try:
            document.cursor.forward()
        except CursorOutOfFileForward:
            print('cursor out of file')
            
    elif command.lower() == 'home':
        document.cursor.home()
        
    elif command.lower() == 'end':
        document.cursor.end()
        
    elif command.lower() == 'cursor pos':
        print(document.cursor.position)
