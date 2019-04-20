# This small program gets rid of national characters from a file

import unidecode

textfile = input("Enter the text file name \n")

with open(textfile, "rt") as fin:
    with open(textfile.split(".")[0] + "normalized.txt", "wt") as fout:
        for line in fin:
            fout.write(unidecode.unidecode(line))
