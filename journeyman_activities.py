import socket

'''1.1) Take two arguments, a list and an integer. The list is a series 
of strings; one of those strings will be the filename, the others will 
be the file contents. The integer is the location in the list of the file 
name. (Write each string to a separate line)

list:
a 0 <-contents
b 1 <-contents
c 2 <-contents
d 3 <-contents
e 4 <- filename
f 5 <-contents

item:
4

'''
def journeyman1(str_list , item):
    file_name = str(str_list(item))
    f = open(file_name, 'w+')
    for i in str_list:
        if i != file_name:
            f.write(i)
    f.close()


'''1.2) Write a function which takes a single integer as an argument and 
returns the sum of every integer up to and including that number, use a 
generator.'''

def sum_number():
    number = journeyman1(sum_generator())
    print (str(number))

def sum_generator(final_num):
    current_num = 0
    
    while(current_num <= final_num):
        yield current_num
        current_num += 0

def journeyman2(final_num):
    range_sum = sum(range(final_num+1))
    return range_sum
    

'''1.3) Write a python script which connects to the included server 
on port 50001 and returns the message it receives.'''
def journeyman3():
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 80)) #connect
    receive_string = s.recv(1024) #get what server sends
    s.close() #close the socket
    return receive_string


'''1.4) Create a class called person, with height, weight, hair color, 
and eye color fields, then implement it to describe yourself.'''
def journeyman4():
    class Person:
        def __init__(self, height = 0, weight = 0, hair = '', eye = ''):
            self.height = height
            self.weight = weight
            self.hair = hair
            self.eye = eye
        def print_info(self):
            print "Height:\t%d\nWeight:\t%d\nHair:\t%s\nEye:\t%s\n" % (self.height , self.weight , self.hair , self.eye)
            
    Bill = Person(6, 180, "Brown", "Blue")
    Bill.print_info()
        
    return
    

journeyman4()
