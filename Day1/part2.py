sum = 0

# opens the input file
with open("input.txt", "r") as file:

    # iterates for every line/word in the input file
    for line in file:

        # replaces every number written in text with an actual number
        line = line.replace("one", "1")
        line = line.replace("two", "2")
        line = line.replace("three", "3")
        line = line.replace("four", "4")
        line = line.replace("five", "5")
        line = line.replace("six", "6")
        line = line.replace("seven", "7")
        line = line.replace("eight", "8")
        line = line.replace("nine", "9")

        firstNumberFound = True

        # iterates through every character in line
        for char in line:

            # checks if the character is numeric
            if char.isnumeric() == True:

                # makes sure the first number doesn't get set more than once per line
                if firstNumberFound == True:
                    firstNumber = char
                    firstNumberFound = False
                
                # cycles through every number until it finds the last one
                lastNumber = char
        # sums all the 2 digit numbers together
        sum = sum + int(firstNumber + lastNumber)
    print("the sum of all numbers is " + str(sum))
