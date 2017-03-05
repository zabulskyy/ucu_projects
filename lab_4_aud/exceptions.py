class MyException(Exception):
	pass


def raise_func():
	raise KeyError 
	raise IndexError 
	
	
def except_func(func):
	try:
		func()
	except KeyError:
		print('KeyError')
	except IndexError:
		print('IndexError')
	except MyException:
		print('MyException')
	except:
		print('unknown error')
		
		
def myexcept_raise_func():
	raise MyException('it works')
	
	

