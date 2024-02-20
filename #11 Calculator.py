from art import logo

#calculator

#Add
def add(n1, n2):
  return n1 + n2
#Subtract
def subtract(n1,n2):
  return n1 - n2
#Multiply
def multiply(n1,n2):
  return n1 * n2
#Divide
def divide(n1,n2):
  return n1 / n2
  
def calculator(): 
  print(logo)
  num1 = float(input("What`s the first number?\n"))
  calculation_ended = False
  while not calculation_ended:
    operations = {"+":add,
                  "-":subtract,
                  "*":multiply,
                  "/":divide
                 }
    
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation\n ")
    num2 = float(input("What`s the next number?\n")) 
    answer=operations[operation_symbol](num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    num1 = answer
    
    more_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation\n")
    if more_calc == 'n':
      calculation_ended = True
      calculator()

calculator()
     


