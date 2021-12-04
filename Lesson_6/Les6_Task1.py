from time import sleep

class TrafficLight:
    colors = ('red', 'yellow', 'green')
    time = (7, 2, 5)

    def __init__(self):
        self.__color= 'red'

    def running(self):
        for i in self.colors:
            self.__color = i
            print(self.__color)
            sleep(self.time[self.colors.index(self.__color)])

traffic = TrafficLight()
traffic.running()

