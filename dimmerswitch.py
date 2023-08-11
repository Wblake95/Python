#! /usr/bin/env python

class DimmerSwitch():
    def __init__(self):
        self.TurnLightOn = True
        self.Brightness = 0

    def LightOn(self):
        self.TurnLightOn = True
        self.Bright()
        return self.TurnLightOn

    def LightOff(self):
        self.TurnLightOn = False
        self.Brightness = 0
        return self.TurnLightOn

    def Bright(self):
        if self.TurnLightOn != True:
            return
        if self.Brightness < 10:
            self.Brightness += 1
        return self.Brightness

    def Dimmer(self):
        if self.TurnLightOn != True:
            return
        if self.Brightness > 0:
            self.Brightness -= 1
        return self.Brightness

    def Show(self):
        print('Status ', self.TurnLightOn)
        print('Brightness ', self.Brightness)

switch = DimmerSwitch()

switch.LightOn()
switch.Show()
switch.LightOff()
switch.Show()
switch.LightOn()
switch.Bright()
switch.Bright()
switch.Bright()
switch.Show()
switch.Dimmer()
switch.Dimmer()
switch.Show()
