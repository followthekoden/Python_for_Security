class myClass(object):
    def __init__(self, msg, integer):
        self.msg = msg
        self.integer = integer
        print self.msg
        print self.integer
        return

def create_file():
    f = open("demo.txt" , "w+")
    
    for i in range(10):
        f.write("this is line %d\r\n" %(i+1))
    f.write("\nk1dDarkn3ss")
    f.close()

def read_file():
    f = open("demo.txt", "r")
    f.read()
    f.close()
    
def main():
    create_file()
    read_file()
    
main()