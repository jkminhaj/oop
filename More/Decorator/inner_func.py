def hi() :
    print("Hi")
    
    def inner_fun () :
        print("I am from inner_fun")
    
    return inner_fun

hi()() #calling both functions . must have to return the inner function to use it outside

#  we can pass a function inside a function

def doSomething(func) :
    func()


def coding() :
    print("I am coding")
    

doSomething(coding)
