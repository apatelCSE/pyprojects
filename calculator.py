while True:
	print("Options:")
	print("Enter 'add' to add two numbers")
	print("Enter 'subtract' to subtract two numbers")
	print("Enter 'multiply' to multiply two numbers")
	print("Enter 'divide' to divide two numbers")
	print("Enter 'quit' to end the program")
	user_input = input("Choose operation:")

	if user_input == "quit":
   		break
	elif user_input == "add":
		add1 = float(input("Enter a number:"))
		add2 = float(input("Enter second number:" ))
		addresult = str(add1 + add2)
		print("The answer is" + addresult)
		ans = input("Go again?")
		if ans == "no" :
			break
		else:
			continue
	elif user_input == "subtract":
		sub1 = float(input("Enter a number:" ))
		sub2 = float(input("Enter second number:" ))
		subresult = str(sub1 - sub2)
		print("The answer is" + subresult)
		ans = input("Go again?")
		if ans == "no" :
			break
		else:
			continue
	elif user_input == "multiply":
		mult1 = float(input("Enter a number:"))
		mult2 = float(input("Enter second number:"))
		multresult = str(mult1 * mult2)
		print("The answer is" + multresult)
		ans = input("Go again?")
		if ans == "no" :
			break
		else:
			continue
	elif user_input == "divide":
		div1 = float(input("Enter a number:"))
		div2 = float(input("Enter second number:"))
		divresult = str(div1 / div2)
		print("The answer is" + divresult)
		ans = input("Go again?")
		if ans == "no" :
			break
		else:
			continue
	else:
		print("Unknown input")
