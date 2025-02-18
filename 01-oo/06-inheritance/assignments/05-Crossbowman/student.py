class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        pass
    def use_arrows(self,num):
        if num <= self.__num_arrows:
            self.__num_arrows -= num
            return True
        raise ValueError("Not enough arrows")


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)
        

    def triple_shot(self, target):
        pass