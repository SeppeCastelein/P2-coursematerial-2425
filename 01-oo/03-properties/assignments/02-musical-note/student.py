class MusicalNote:
    def __init__(self, name, pitch):
        self.name = name
        self.pitch = pitch

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def pitch(self):
        return self.__pitch
    

    @pitch.setter
    def pitch(self, value):
        self.__pitch = value