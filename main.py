word = input("Enter Word : ")

for i in word:
    if i=="A" or i=="a":
        print("We found a.")
        break
    else:
        print("We lost the a.")