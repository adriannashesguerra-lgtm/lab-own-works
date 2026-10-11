def relational_operations_evaluator ():
    print ("Welcome to the relational operations evaluator!")
    #get the input of the two numbers from the user
    num1 = float(input("Enter the value of the first num: "))
    num2 = float(input("Enter the value of the second num: ")) 
    result = ""
    
    #evaluate the relational operations
    print (f"{num1} > {num2} = {num1 > num2}")
    print (f"{num1} < {num2} = {num1 < num2}")
    print (f"{num1} >= {num2} = {num1 >= num2}")
    print (f"{num1} <= {num2} = {num1 <= num2}")
    print (f"{num1} == {num2} = {num1 == num2}")
    print (f"{num1} != {num2} = {num1 != num2}")
relational_operations_evaluator()
    