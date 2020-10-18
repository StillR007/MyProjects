from time import sleep


class TrafficLight:
    def __init__(self):
        TrafficLight.__color = 'red'

    def running(self):
        print('Светофор красный (7 сек)')
        sleep(7)
        print('Светофор желтый (2 сек)')
        sleep(2)
        print('Светофор зееный (5 сек)')
        sleep(5)


a = TrafficLight()
a.running()
