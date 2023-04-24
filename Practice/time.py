class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        result = [self.hours, self.minutes, self.seconds]
        current_hours = f"0{self.hours}"
        current_minutes = f"0{self.minutes}"
        current_seconds = f"0{self.seconds}"
        if self.hours < 10:
            result[0] = current_hours

        if self.minutes < 10:
            result[1] = current_minutes

        if self.seconds < 10:
            result[2] = current_seconds

        return ":".join(map(str, result))

    def next_second(self):
        next_minute = False
        next_hour = False

        if self.seconds == self.max_seconds:
            self.seconds = 0
            next_minute = True
        else:
            self.seconds += 1

        if next_minute and self.minutes == self.max_minutes:
            self.minutes = 0
            next_hour = True
        elif next_minute and self.minutes != self.max_minutes:
            self.minutes += 1

        if next_hour and self.hours == self.max_hours:
            self.hours = 0
        elif next_hour and self.hours != self.max_hours:
            self.hours += 1

        return self.get_time()


time = Time(00, 00, 00)
print(time.next_second())