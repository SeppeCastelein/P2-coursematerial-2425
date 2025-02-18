class Duration:
    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    @staticmethod
    def from_seconds(seconds):
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return Duration(hours, minutes, seconds)

    @staticmethod
    def from_minutes(minutes):
        hours = minutes // 60
        minutes %= 60
        return Duration(hours, minutes, 0)

    @staticmethod
    def from_hours(hours):
        return Duration(hours, 0, 0)

    @property
    def hours(self):
        return self._hours

    @property
    def minutes(self):
        return self._hours * 60 + self._minutes

    @property
    def seconds(self):
        return self._hours * 3600 + self._minutes * 60 + self._seconds

# Example usage:
duration = Duration.from_seconds(60)
print(duration.seconds)  # Output: 60
print(duration.minutes)  # Output: 1

duration = Duration.from_hours(1)
print(duration.minutes)  # Output: 60
print(duration.seconds)  # Output: 3600