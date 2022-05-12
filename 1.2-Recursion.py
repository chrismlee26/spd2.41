# 1 Given a sorted array of strings, write a recursive function to find the index of the first and last occurrence of a target string. If the target string is not found in the array, report that.
# Example input:  instructors = [Adriana, Adriana, Alan, Alan, Alan, Alan, Alan, Braus, Braus, Braus, Braus, Dan, Dan, Dan, Dan, Dan, Dani, Dani, Jess, Meredith, Milad, Milad, Mitchell, Mitchell, Mitchell, Mitchell]
# Example execution:  find_indexes(instructors, 'Braus')  ⇒  (7, 10)

# --------------------
# Question 1
# --------------------
# Example execution:  find_indexes(instructors, 'Braus')  ⇒  (7, 10)
instructors = ["Adriana", "Adriana", "Alan", "Alan", "Alan", "Alan", "Alan", "Braus", "Braus", "Braus", "Braus", "Dan", "Dan", "Dan", "Dan", "Dan", "Dani", "Dani", "Jess", "Meredith", "Milad", "Milad", "Mitchell", "Mitchell", "Mitchell", "Mitchell"]

def find_indexes(instructors, target):
    if len(instructors) == 0:
        return -1
    if instructors[0] == target:
        return 0
    # Find all instances of target
    indexes = []
    for i in range(len(instructors)):
        if instructors[i] == target:
            indexes.append(i)
    # Return first and last instance of target
    if len(indexes) == 0:
        return -1
    return (indexes[0], indexes[-1])

print(find_indexes(instructors, 'Braus'))

# 2 Given a string of digits 2 to 9 a user has pressed on a T9 “old school” telephone keypad, return a list of all letter combinations they could have been trying to type on the keypad.
# Example execution 1:  t9_letters("23")  ⇒  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
# Example execution 2:  t9_letters("4663")  ⇒  ["gmmd", …, "gone", …, "good", …, "home", …, "hood", …, "ioof"]

# --------------------
# Question 2
# --------------------

def t9_letters(digits):
    # create a dictionary of all possible combinations
    t9_dict = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    # create a list to store all possible combinations
    combinations = []

    while len(digits) > 0:
        # get the first digit
        digit = digits[0]
        # get the list of possible combinations for that digit
        letters = t9_dict[digit]
        # remove the first digit from the string
        digits = digits[1:]
        # if there are no more digits, add the letters to the list
        if len(digits) == 0:
            combinations.extend(letters)
        # if there are more digits, add the letters to the list and then add the combinations of the remaining digits
        else:
            for letter in letters:
                combinations.append(letter)
    return combinations

print(t9_letters("23"))
print(t9_letters("4663"))