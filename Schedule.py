class Time(object):
    def __init__(self, time):
        apm, hour, minute = self.break_time(time)
        self.hour = int(hour)
        if apm.lower() == "pm":
            self.hour += 12
            self.hour = str(self.hour)

        self.minute = minute

    def break_time(self, time):
        hour = time.split(":")[0]
        minute = time.split(":")[1][:2]
        apm = time[-2:]
        return apm, hour, minute

    def __repr__(self):
        return f"{self.hour}:{self.minute}"


class Slot(object):
    def __init__(self, days, time, crn) -> None:
        self.days = days
        self.start = Time(time.split("-")[0])
        self.end = Time(time.split("-")[1])
        self.crn = crn

    def __repr__(self) -> str:
        return f"<{self.crn} on {self.days},{self.start}-{self.end}>"


class Schedule(object):
    def __init__(self, course):
        self.course = course
        self.slots = []

    def add_slots(self, days, time, crn):
        self.slots.append(Slot(days, time, crn))

    def __repr__(self):
        return f"<{self.course}, {len(self.slots)}>"
