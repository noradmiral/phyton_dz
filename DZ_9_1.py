import time
class TrafficLight:
    _color = None
    _colors = ['red', 'yellow', 'green']

    def __init__(self):
        self._color = self._colors[0]

    def running(self):
        i=0
        while i<5:
            for el in TrafficLight._colors :
                print(el)
                i+=1
                time.sleep(3)

traffic = TrafficLight()
traffic.running()
