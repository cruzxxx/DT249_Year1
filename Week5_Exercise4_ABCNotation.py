"""Write a program to read the attached file and print the Id,
title (one only), time and key signatures line by line.

print:
id:
T: - if T has more than 1 line, print only first one, ignore the rest
M:
K:
ignore notation

problem 1: print only the lines selected above > DONE
problem 2: print the id X > DONE
problem 3: renaming X: == nothing /  K: == Key sig:  /  M: == Time sig: /  T: == nothing > DONE
problem 4: print every round of the loop in 1 line > DONE
problem 5: for T, print only the first T for each X (tune) and ignore the rest > DONE

"""

try:
    with open("hnr1.abc", mode="r") as file_music: #reading the file, no need for closing file at the end
        number_songs = 0 #empty variable for int is 0, not ""
        title = ""

        for line in file_music:
            if "X:" in line: #new song
                id = line.strip().replace("X:", "")
                number_title = 0 #wipes out the variable T at the beginning of a new song
                number_songs += 1

            elif "T:" in line:
                if number_title == 0:
                    title = line.strip().replace("T:", "")
                number_title += 1

            elif "M:" in line:
                time = line.strip().replace("M:", "Time sig: ")

            elif "K:" in line:
                key = line.strip().replace("K:", "Key sig: ") #strip removes extra line in the output

                print(f"{id} ... {title} ... {time} ... {key}")

    print(f"The file has {number_songs} tunes")

except Exception as e:
    print(f"{e}")