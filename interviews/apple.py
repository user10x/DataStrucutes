"""
Find and replace
cat /usr/share/dict/words | head
A
a
aa
aal
aalii
aam
Aani
aardvark
aardwolf
Aaron

Find all occurrences and replace with a given word

"""


def process_file(filePAth, word="cat", replace="dog"):

    validWords = set()


    with open(filePAth, 'r') as f:
        for line in f:
            if word in line:
                line = line.replace(word, replace)
            print(line, end='')




