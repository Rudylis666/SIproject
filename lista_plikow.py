import os

def negatywny_zbior_opis():
    # open the output file for writing. will overwrite all existing data in there
    with open('neg2.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir('dogs'):
            print(filename)
            f.write('dogs/' + filename + '\n')

negatywny_zbior_opis()