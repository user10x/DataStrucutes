# we're going to build an event counter that could be used to e.g. measure api requests against an endpoint

# # record increments the event counter called "event_name" by one at the given time
# # time is the number of seconds from the unix epoch
# record(event_name: string, time: int)

# # query aggregates events by the specified resolution, returning an array of event counts from start to end.
# # start and end are specified in same unit as the resolution (eg resolution=hour means that start is the number of hours from unix epoch)
# # start and end are inclusive, exclusive respectively
# query(event_name: string, resolution: hour | day, start: int, end: int) -> []int

# # examples
# record("/api/v1/user", 0)
# record("/api/v1/user", 1)
# record("/api/v1/user", 3600)
# record("/api/v1/user", 24 * 3600)

# # get me hourly req. to endpoint from hour 0 to hour 3
# query("/api/v1/user", "hour", 0, 3) -> [2, 1, 0]


# # get me daily req. to endpoint from day 0 to day 3
# query("/api/v1/user", "day", 0, 3) -> [3, 1, 0]

# this is how we'll store this xxx

# { ("event_name,(0, 60)" -> 123), }
# { "event_name" -> {0 -> 123, 1 -> n, 2 -> k} }

from collections import defaultdict


class EventCounter:
    def __init__(self):
        self.event_hour = defaultdict(int)
        self.event_day = defaultdict(int)

    def record(self, event_name: str, time: int) -> None:
        hour = time // 3600
        day = hour // 24

        self.event_hour[(event_name, hour)] += 1
        self.event_day[(event_name, day)] += 1

    def query(self, event_name: str, event_boundry: str, start: int, end: int) -> list:
        res = []
        if event_boundry == 'hour':
            for i in range(start, end):
                res.append(self.event_hour[(event_name,i)])
        else:
            for day in range(start, end):
                res.append(self.event_day[(event_name, day)])

        return res

    def print_event_counter(self):
        print(self.event_hour)

    def print_day_counter(self):
        print(self.event_day)

ec = EventCounter()
ec.record("/api/v1/user", 0)
ec.record("/api/v1/user", 1)
ec.record("/api/v1/user", 3600)
ec.record("/api/v1/user", 24 * 3600)
ec.record("/api/v1/user", 12 * 24 * 3600)

print(ec.print_event_counter())
print(ec.print_day_counter())


print(ec.query("/api/v1/user", "hour", 0, 3))
print(ec.query("/api/v1/user", "day", 0, 3))
print(ec.query("/api/v1/user", "day", 0, 15))



class EventCounterTrie:
    def __init__(self):
        self.event_hour = defaultdict(dict)
        self.event_day = defaultdict(int)

    def record(self, event_name: str, time: int) -> None:
        hour = time // 3600
        day = hour // 24

        self.event_hour[event_name] =
        self.event_day[(event_name, day)] += 1

    def query(self, event_name: str, event_boundry: str, start: int, end: int) -> list:
        res = []
        if event_boundry == 'hour':
            for i in range(start, end):
                res.append(self.event_hour[(event_name,i)])
        else:
            for day in range(start, end):
                res.append(self.event_day[(event_name, day)])

        return res

    def print_event_counter(self):
        print(self.event_hour)

    def print_day_counter(self):
        print(self.event_day)