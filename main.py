word = input("Enter Word : ")

for i in word:
    if i=="A" or i=="a":
        print("We found the a. I am taking it to the gulag.")
        break
    else:
        print("We lost the a. we,ll get it next time.")