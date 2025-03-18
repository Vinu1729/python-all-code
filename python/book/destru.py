class taste:
    def __init__(self):
        print("this is constructor")
    def __del__(self):
        print("this is destructor")
def function ():
    s1=taste()
def function2 ():
    s2 = taste()
    print("calling function")
    function()
    print("calling destrucotor")


function2()