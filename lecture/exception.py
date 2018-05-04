#try throws the exception and except handles it
try:
    number = int(input("Enter a number: "))
except:
    print("its ded LOL")

#except is very generic so we need to figure out how to catch specific errors

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("your input was not a number")

#multiple and finally (which is optional to include, always happens)

try:
    number = int(input("Enter a number: "))
    result = number/0
except ValueError:
    print("your input was not a number!")
except ZeroDivisionError:
    print("you are dividing by 0!")
except:
    print("somethings wrong but I dont know!")
finally:
    print("I am always executed no matter what!")

#asks for an int, valueError is handled by recursion, otherwise it shrugs
#apparently this should be avoided as you can end in an infinite loop
def askAgainIfNeeded():
    try:
        better_be_an_int = int(input("Enter an int of I will ask again: "))
    except ValueError:
        print("recursion is stupid")
        askAgainIfNeeded()
    except:
        print{"Something broke IDK"}

askAgainIfNeeded()
print("was that so hard?")
