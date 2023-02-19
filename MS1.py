with open("keylog.txt", "r") as f:
    passwordChars = [] #Tracks the unique random characters of the password 
    numsList = []

    #Determine min length of password based on number of unique numbers in the textfile
    for nums in f:
        numsList.append(nums.rstrip())
        if nums[0] not in passwordChars:
            passwordChars.append(nums[0])
        if nums[1] not in passwordChars:
            passwordChars.append(nums[1])
        if nums[2] not in passwordChars:
            passwordChars.append(nums[2])
    minLength = len(passwordChars)
    print(f"Minimum password length is {minLength}")

    # Find all the numbers that occur before each number, assuming all characters are unique
    numbersBefore = { n : [] for n in passwordChars }
    for n in numsList:
        if n[0] not in numbersBefore[str(n[2])]:
            numbersBefore[str(n[2])].append(n[0])
        if n[1] not in numbersBefore[str(n[2])]:
            numbersBefore[str(n[2])].append(n[1])
        if n[0] not in numbersBefore[str(n[1])]:
            numbersBefore[str(n[1])].append(n[0])
    # print(numbersBefore)
    print(''.join(sorted(numbersBefore, key=lambda k: len(numbersBefore[k]))))
    f.close()