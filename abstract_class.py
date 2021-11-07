"""
Creadit to https://github.com/ArjanCodes/betterpython/blob/main/2%20-%20dependency%20inversion/dependency-inversion-after.py

This code uses an abstract class and abstract method to reduce coupling, making parts of code less dependent on each other

Lightbulb and Fan are inherited from the abstract class that specifies turn_on and turn_off methods,
so the power switch function is not dependent on what to swtich, it just have a 'client' which all implement the turn on
and off methods.


"""

from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")


class ElectricPowerSwitch:

    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


l = LightBulb()
f = Fan()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()