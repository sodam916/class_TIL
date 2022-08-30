

def printhello(i):
    if i < 3:
        print('hello')
        printhello(i - 1)
        
printhello(3)