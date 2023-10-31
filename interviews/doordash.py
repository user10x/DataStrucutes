"""
Given a string on inputs, return
Example:1 [("Mon 9:00 AM", "Mon 10:00 AM")]
return
["1990005,1990010,1990015, 1990020,....1100000]


Example2: [("Mon 9:00 AM", "Mon 2:30 pm")]
return ["1990005,1990010,1990015, .......1200]



"""


class StartEndTimeInterval:
    class Time:
        def __init__(self, day, hour, minute, day_time):
            self.day = day
            self.hour = hour
            self.minute = minute
            self.day_time = day_time

        def add(self, mins):
            self.hour += (mins + self.minute) // 60

            self.minute = (mins + self.minute) % 60
            print(self.hour, self.minute)
            if self.hour == 12:
                self.day_time = not self.day_time
                self.hour = 0
                if self.day_time:
                    self.day = (self.day + 1) % 7

        def get_numeric(self):
            add_hour = self.hour
            day_and_hour = self.day * 100 + add_hour# 1*100 + 11

            return day_and_hour * 100 + self.minute # 111 * 100 + 45/60


        def equals(self, t2):
            return self.day == t2.day and self.hour == t2.hour and self.minute == t2.minute and self.day_time == t2.day_time

    def __init__(self):
        self.map_days = {
            "mon": 1, "tue": 2, "wed": 3, "thu": 4, "fri": 5, "sat": 6, "sun": 7
        }
        self.format = None

    def get_intervals(self, start, end, format):
        self.format = format
        intervals = []
        start_time = self.get_time(start)
        end_time = self.get_time(end)
        while not start_time.equals(end_time):
            start_time.add(5)
            intervals.append(start_time.get_numeric())
        return intervals

    def get_time(self, time_str):
        info = time_str.split(" ")
        day = self.map_days[info[0]]
        hour, minute = map(int, info[1].split(":"))
        print(hour, minute)
        day_time = info[2] == "am"
        return self.Time(day, hour, minute, day_time)


if __name__ == "__main__":
    start_end_time_interval = StartEndTimeInterval()
    data = start_end_time_interval.get_intervals("mon 11:45 pm", "tue 2:00 am", "12 HOUR")
    print(len(data))
    print(data)

    # data2 = start_end_time_interval.get_intervals("mon 10:00 pm", "tue 11:00 pm", "24 HOUR")
    # print(len(data2))
    # print(data2)
    #
    # data3 = start_end_time_interval.get_intervals("sun 10:00 pm", "mon 11:00 pm", "24 HOUR")
    # print(len(data3))
    # print(data3)
