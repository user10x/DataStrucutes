# import requests
# import mysql.connector
# import pandas as pd

logs = """
id=6 timestamp="Wed Jun 19 09:35:40 PDT 2019" message="test 6" field_1="test 5"
timestamp="Wed Jun 19 09:35:36 PDT 2019" message="test=10" id=10 field_1="test 10" field_6="test 1"
timestamp="Wed Jun 19 09:35:37 PDT 2019" foo=test=4 id=4 field_2="test 4"
times   tamp="Wed Jun 19 09:35:38 PDT 2019" message="test 2" id=3 field_3="test 2" field_9="test 23"
timestamp="Wed Jun 19 09:35:39 PDT 2019" message="test 3" id=2 field_4="test 3"
timestamp="Wed Jun 19 09:35:40 PDT 2019" message="test 4" id=1 field_5="test 4"
timestamp="Wed Jun 19 09:35:37 PDT 2019" message="test 5" id=5 field_3="test 10"
"""
import sys
import re
import re
str = 'an example word:cat!!'

match=re.search('an example',str,flags=False)

match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
 print ('found', match.group()) ## 'found word:cat'
else:
 print ('did not find')





# read logs get the input lines, returns a cleaner frame of datavalues
# everything before becomes a key =
# find an =
# value
# if the next char is '\"'; match the quote
# else match until it's a space

# csv_input = read_logs(logs.splitlines(), '')
# print(csv_input)
