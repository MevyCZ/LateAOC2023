sum = 0

textNumbers = "one two three four five six seven eight nine".split()

# opens the input file
with open("C:\\Users\\manny\\Scripts\\AdventOfCode2023\\Day1\\input.txt", "r") as file:

    # iterates for every line/word in the input file
    for line in file:

        firstNumberFound = True

        # iterates through every character in line
        for char in line:

            # checks if the character is numeric
            if char.isnumeric() == True or textNumbers in line:

                # makes sure the first number doesn't get set more than once per line
                if firstNumberFound == True:
                    firstNumber = char
                    firstNumberFound = False
                
                # cycles through every number until it finds the last one
                lastNumber = char
        # sums all the 2 digit numbers together
        print(int(firstNumber + lastNumber))
        sum = sum + int(firstNumber + lastNumber)
    print(sum)
