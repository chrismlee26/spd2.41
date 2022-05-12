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

