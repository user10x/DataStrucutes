__author__ = 'nichawla'
#
# ''' meta characters . ^ $ * + ? { } [ ] \ | ( )
# For example, [abc] will match any of the characters a, b, or c
#  If you wanted to match only lowercase letters, your RE would be [a-z].
# Metacharacters are not active inside classes. For example, [akm$] will match any of the characters 'a', 'k', 'm', or '$';

import re
str = 'an example word:cat!!'

match=re.search('an example',str,flags=False)

match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
 print 'found', match.group() ## 'found word:cat'
else:
 print 'did not find'


import subprocess as sb

sb.Popen(['ls','-l'],stdout=True,shell=True)
ret=sb.call(["ls", "-l"])


