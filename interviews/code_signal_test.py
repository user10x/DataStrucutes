def solution(queries):
    from collections import defaultdict
    hash_map = defaultdict(int)
    result = []
    elements = []
    for op, num in queries:
        num = int(num)
        if op == "ADD":
            hash_map[num] += 1
            result.append("")
            elements.append(num)
        elif op == "EXISTS":
            if hash_map[num] > 0:
                result.append("true")
            else:
                result.append("false")

        elif op == "REMOVE":
            if hash_map[num] > 0:
                hash_map[num] = hash_map[num] - 1
                result.append("true")

            else:
                result.append("false")

        elif op == "GET_NEXT":
            next = find_next(num, elements)
            result.append(next)

    return result


def find_next(num, elements):
    elements = sorted(elements)
    res = ""
    for i in range(num, len(elements)):
        if elements[i] == num:
            for j in range(i, len(elements) - 1):
                if elements[j] != elements[j + 1]:
                    res = f'{elements[i + 1]}'

                    print("breaking", elements[i], elements[i + 1])
                    break

    return res

#todo add input and output
var = ["", "", "", "", "2", "4", "4", "", "true", "2", "4", "4", ""]
