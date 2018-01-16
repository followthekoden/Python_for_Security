import operator

#compare 2 numbers to determine the larger
def num_compare():
    num1 = float(input("enter number 1: "))
    num2 = float(input("enter number 2: "))
    largestNumber = 0
    if (num1 == num2):
        print ("numbers are equal")
    elif (num1 > num2):
        largestNumber = num1
        print("number 1 is larger")
    else:
        largestNumber = num2
        print("number 2 is larger")
    print ("k1dDarkn3ss... Exiting")
    return largestNumber

#remove a selected letter from a string
def remove_letter():
    text = str(input("enter the text: "))
    text2 = text
    letterRM = str(input("enter the letter to remove: "))
    
    for i in letterRM:
        text = text.replace(i, "")
    print (text)
    print ("Removal 100%... Exiting")
    return text

#Print the previously stored string
def print_string():
    print ("what?!?!?!?")
    
#Basic calculaator (additon, subtraction, muliplication, division)
def calculator():
    num1 = float(input("enter number 1: "))
    sign = str(input("action: "))
    num2 = float(input("enter number 2: "))
    outcome = 0
    ops = {"+" : operator.add, "-" : operator.sub, "/" : operator.truediv, "*" : operator.mul}
    for key, value in ops.items():
        if sign == key:
            outcome = value(num1, num2)
            print (str(outcome))
            return outcome
    print ("calculations complete k1dDarkn3ss... exiting")
    return outcome

#accept and store a string
def accept_and_store():
    global k1dDarkn3ss 
    k1dDarkn3ss = str(input("Enter a string value: "))
    print ("accepted and stored")
    return k1dDarkn3ss
    
#menu goes here
def main():
    opt_list = [
        "1 number compare",
        "2 print string",
        "3 remove letter",
        "4 calculator",
        "5 accept and store"]
    opt_methods = [
        num_compare,
        print_string,
        remove_letter,
        calculator,
        accept_and_store]
        
    for opt in opt_list:
        print (opt)
        
    opt_choice = int(input("Select an option: "))
    opt_choice -= 1
    opt_methods[opt_choice]()
    
main()