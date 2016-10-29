
def is_Palindrome(input):
    counter_start = 0
    counter_end = len(input)-1
    for element in input:
        print counter_start, counter_end
        if counter_start == counter_end :
            return True
        if input[counter_start] != input[counter_end]:
            return False
        counter_start = counter_start + 1
        counter_end = counter_end - 1
    return True

if __name__ == '__main__':
    palin_string = "1229221"

    print is_Palindrome(palin_string)
