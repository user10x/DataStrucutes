royals = [
    {'name': 'Richard', 'birthdate': '1940-2-12', 'parent': 'Edwlye'},
    {'name': 'Nedd', 'birthdate': '1974-09-09', 'parent': 'Richard'},
    {'name': 'Benjen', 'birthdate': '1967-2-12', 'parent': 'Richard'},
    {'name': 'Lyanna', 'birthdate': '1968-02-12', 'parent': 'Richard'},
    {'name': 'Rob', 'birthdate': '1979-02-12', 'parent': 'Nedd'},
    {'name': 'Sansa', 'birthdate': '1981-02-12', 'parent': 'Nedd'},
    {'name': 'Arya', 'birthdate': '1984-02-12', 'parent': 'Nedd'},
    {'name': 'Bran', 'birthdate': '1986-02-12', 'parent': 'Nedd'}
]

"""
 # Edwlye -> [Richard]
 # Richard -> [Nedd, Benjen, Lyanna]
 # Nedd -> [Rob, Sansa, Arya, Bran]
    
"""


def nth_successor(royals, n):
    def calculate_ts(date_str):
        import datetime

        date = date_str.split('-')
        return datetime.datetime(int(date[0]), int(date[1]), int(date[2]))

    import heapq

    min_heap = []

    for element in royals:
        ts = calculate_ts(element['birthdate'])
        min_heap.append((ts, element))


    from collections import defaultdict

    parent_to_children = defaultdict(list)



    for element in royals:
        parent_to_children[element['parent']].append((calculate_ts(element['birthdate']),element['name']))

    for k, v in parent_to_children.items():
        print(k, v)
        print("")


    heapq.heapify(min_heap)



    count = -1

    while count <= n:
        ts, element = heapq.heappop(min_heap)
        print("popped", element)
        count += 1

        # print(element)
        # print(parent_to_children)

        if element['name'] in parent_to_children:
            children = parent_to_children[element['name']]
            children_left = n - len(children)
            if children_left > 0:
               count += len(children)
               while children_left>0:
                  heapq.heappop(min_heap)
                  children_left -= 1
            else:
               print(children)
               return children[n-1][1]




print(nth_successor(royals, 0))