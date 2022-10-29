class Time(object):
    def __init__(self, time):
        apm, hour, minute = self.break_time(time)
        self.hour = int(hour)
        if apm.lower() == "pm" and self.hour != 12:
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
        self.days = days.split()
        self.start = Time(time.split("-")[0])
        self.end = Time(time.split("-")[1])
        self.crn = crn

    def collide_time(self, time_slot):

        collision = False
        a_start = self.start.hour + self.start.minute
        a_end = self.end.hour + self.end.minute
        b_start = time_slot.start.hour + time_slot.start.minute
        b_end = time_slot.end.hour + time_slot.end.minute

        if (a_start == b_start) or (a_end == b_end):
            collision = True
        if (a_start < b_start < a_end) or (b_start < a_start < b_end):
            collision = True

        return collision

    def collision_day(self, slot):
        all_days = set(self.days + slot.days)
        print(all_days)

    def __repr__(self) -> str:
        return f"<{self.crn} on {self.days},{self.start}-{self.end}>"


class Schedule(object):
    def __init__(self, course):
        self.course = course
        self.slots = []
        self.indices = 0

    def add_slots(self, days, time, crn):
        if time != "TBA":
            self.slots.append(Slot(days, time, crn))

    def __repr__(self):
        return f"<{self.course}, {len(self.slots)}>"
