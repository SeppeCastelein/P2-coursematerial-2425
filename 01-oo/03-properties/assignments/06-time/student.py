class Time: 
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        if 0 <= value < 24:
            self.__hours = value
        else:
            raise ValueError("Invalid hours: must be between 0 and 23")

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        if 0 <= value < 60:
            self.__minutes = value
        else:
            raise ValueError("Invalid minutes: must be between 0 and 59")

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value):
        if 0 <= value < 60:
            self.__seconds = value
        else:
            raise ValueError("Invalid seconds: must be between 0 and 59")

# Example usage:
time = Time(0, 0, 0)
time.hours = 8
try:
    time.hours = -1
except ValueError as e:
    print(e)  # Output: Invalid hours: must be between 0 and 23

try:
    time.hours = 24
except ValueError as e:
    print(e)  # Output: Invalid hours: must be between 0 and 23


