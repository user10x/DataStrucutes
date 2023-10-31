

"""
Generally speaking, the longer the password is, the better.
For the purpose of this problem, here are the conditions for
what we consider a "strong" password:

1. At least 20 characters long
2. 12 unique characters
3. A single character cannot appear more than 2 times consecutively

Implement a function that validates if the password satisfies these conditions.

*Input: string*
*Output: bool*

### Good Examples
correct horse battery staple
laptop on standing desk
hello, my name is inigo montoya

### Bad Examples
Password123!@#
apple apple apple apple
this is suuuch a long password

"""

def check_consescutive(input, times=2)->bool:
    last_seen = 1
    for i in range(1, len(input)):
        if input[i-1] == input[i]:
            last_seen +=1
            if last_seen > times:
                return False
        else:
            last_seen = 1
    return True


def unique_check(input):
     return len(set(input)) >= 12

def validate_password(input)->bool:
    #case 1
    if len(input) < 20:
        return False

    if not unique_check(input):
        print('debug', 'unique_check')
        return False

    if not check_consescutive(input, 2):
        print('debug', 'check_consescutive')
        return False

    return True





print(validate_password('correct horse battery stapleebbccdd'))
print(validate_password('laptop on standing desk'))
print(validate_password('hello, my name is inigo montoya'))

print(validate_password('Password123!@#'))
print(validate_password('apple apple apple apple'))
print(validate_password('this is suuuch a long password'))