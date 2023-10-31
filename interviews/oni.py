# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
"""
# Given the list of strings in the Sample Input below, display the Sample Output in the console.

# Sample Input
# create file /home/jack/diary/2023-04-01.txt
# create file /home/jack/diary/2023-04-02.txt
# create file /home/jack/photos/1.jpg


# create file /home/jack/diary/2023-04-01.txt
# create file /home/jack/photos/1.jpg
# create file /home/jack/diary/2023-04-02.txt


key:  /home/jack/diary/ [file1, file2, (key2)]
key2:  /home/jack/diary/abc/ [file1, file2]
/home/jack/diary/1.jpg
/home/jack/diary/photos/1.jpg
/home/jack/diary/ -> [(1.jpg,f),  (/home/jack/diary/photos/, d)]
# Sample Output
# - home
#   - jack
#     - diary
#       - 2023-04-01.txt
#       - 2023-04-02.txt
#     - photos
#       - 1.jpg

"""

from collections import defaultdict


def process_tree(files):
    object_map = defaultdict(list)

    level = 0
    for file in files:
        # /home/jack/diary/2023-04-01.txt  /home/jack/diary/ [2023-04-01.txt
        # /home/jack/diary/texts/1/log.txt

        prefix = '/'.join(file.split('/')[:-1])

        for name in files.split('/'):
            if name not in object_map:
                object_na

        if prefix in object_map:
            file_name = file[len(prefix)+1:]
            object_map[prefix].append((file_name, 'd', level))
        else:
            level = level + 1
            fileName = file.split('/')[-1]
            object_map[prefix].append((fileName, 'f', level))


    print(object_map)

    # output
    # eg: /home/jack/diary/ -> [(1.jpg,f),  (photos/, office/xyz.jpg, ''  d)]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # process_tree(['/home/jack/diary/2023-04-01.txt', '/home/jack/diary/2023-04-02.txt'])
    process_tree(
        ['/home/jack/diary/2023-04-01.txt', '/home/jack/diary/2023-04-02.txt', '/home/jack/diary/files/newfile.txt'])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
