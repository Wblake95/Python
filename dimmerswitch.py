#! /usr/bin/env python

class DimmerSwitch():
    def __init__(self):
        self.TurnLightOn = True
        self.Brightness = 0

    def LightOn(self):
        self.TurnLightOn = True
        return self.TurnLightOn

    def LightOff(self):
        self.TurnLightOn = False
        return self.TurnLightOn

    def Bright(self):
        if self.Brightness < 10:
            self.Brightness += 1
        return self.Brightness

    def Dimmer(self):
        if self.Brightness > 0:
            self.Brightness -= 1
        return self.Brightness
    def Show(self):
        print('Status ', self.TurnLightOn)
        print('Brightness ', self.Brightness)

LightSwitch = DimmerSwitch()
LightSwitch.Show()
LightSwitch.LightOff()
LightSwitch.Show()
LightSwitch.Bright()
LightSwitch.Bright()
LightSwitch.Bright()
LightSwitch.Show()
LightSwitch.Dimmer()
LightSwitch.Show()
