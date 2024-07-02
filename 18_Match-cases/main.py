x = int(input())

match x:
    case 1: #Executes if the value of x is 1
        print("If we want to match with certain value")

    case 1: # To demonstrate, if any case matched it breaks
            # from match unlike other lang
        print("In Python if a case is matched it automatically\
               breaks from match after executing case block")

    case _ if (x > 2 and x < 10): # Executes if x matches the condition
        print("If we have any condition")

    case _: # If any case doesn't match then this block will execute
        print("It's Default case.")