
inp = input("Enter expression to be calculated: \n")

try:
    result = eval(inp)
    print(result)
except Exception as e:
    print("Error in input expression: ", e)