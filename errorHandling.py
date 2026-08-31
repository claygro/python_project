file = open("youtube.txt", "wt")

try:
    file.write("chaii aur code")
except:
    print("Error in opening the file")
finally:
    file.close()

# this is clean and easier syntax to open, write and close the file.
with open("youtube.txt","w") as file:
    file.write("chaii aur python")