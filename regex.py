import sys
import re
import re


logs = """
id=6 timestamp="Wed Jun 19 09:35:40 PDT 2019" message="test 6" field_1="test 5"
"""


def regex_practice():
    mylist = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo", "id=6 test2"]
    r = re.compile(".*cat")
    newlist = list(filter(r.match, mylist))  # Read Note
    print(newlist)

    r = re.compile('[a-zA-Z]+=[0-9]\s{1}t')
    newlist = list(filter(r.match, mylist))  # Read Note
    print(newlist)
    re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):', r'static PyObject*\npy_\1(void)\n{', 'def myfunc():')
    m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds someone")
    print(m.groupdict())
    print(m.group('first_name'))
    print(m.group('last_name'))

    m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
    print(m.group(0))  # The entire match
    print(m.group(1))  # The first parenthesized subgroup.
    print(m.group(2))  # The second parenthesized subgroup.
    print(m.group(1, 2))

    print(re.split(r'\W+', 'Words, words, words.'))

    # match logs
    log_lines_list = ["id=6 test2=10", "msg=debugging an application"]

    m = re.match(r"([a-zA-Z]+=[a-zA-z0-9]+)", "id=6 msg=10  ts=2019 info=debugging an application")
    print(m.groups())

    string = '"Foo Bar" "Another Value"'
    print(re.findall(r'"(.*?)"', string))

    print(re.split(r"((.+)(={1})(.+)(\s+))", "id=6 msg=10 ts=2019 info=debugging an application"))
    re.match(r'^(?P<n>[0-9]+)(?P<op>[-+\*/])(?P<rest>.+)$', '1+2+3').groupdict()
    print(re.match(r'(?P<lhs>[a-z]+)(?P<op>[=])(?P<rhs>[0-9]+)', 'id=3  field=6 msg=info level logs').groupdict())
    p1 = re.compile(r'(?P<lhs>[a-zA-z0-9]+)(?P<op>[=])(?P<rhs>[a-zA-z0-9]+)')
    print(
        re.findall(p1, 'id=3  field2=6 1 msg=info level logs foo=test=4 key1= key2=value2 timestamp="2019 Wednesday" '))

    p2 = re.compile(r'\"(.*)?\"')
    print(
        re.findall(p2, 'id=3  field=6 1 msg=info level logs foo=test=4 key1= key2=value2 timestamp="2019 Wednesday" '))



regex_practice()
