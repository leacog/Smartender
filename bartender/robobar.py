import RPi.GPIO as GPIO
import time

class Drink:
    def __init__(self, name, drink_dict): 
        self.dict = drink_dict
        self.name = name
        
class Bartender:
    def __init__(self, cal_val):
        self.cal_val = cal_val
        self.GREY = 26
        self.PURPLE = 19
        self.BLUE = 13
        self.GREEN = 6
        self.YELLOW = 5
        self.chan_list = [self.GREY, self.PURPLE, self.BLUE, self.GREEN, self.YELLOW]
        GPIO.setmode(GPIO.BCM)  
        GPIO.setup(self.chan_list, GPIO.OUT)
        GPIO.output(self.chan_list, 0)
    def make(self, drink):
            drink_dict = drink.dict
            ingredients = drink_dict.keys()
            pump_times = self.convert(drink_dict.values())
            self.run_pumps(pump_times, ingredients)
    def convert(self, volumes):
                volume_list = [i * self.cal_val for i in volumes]
                return (volume_list)
    def run_pumps(self, pump_times, ingredients):
            for index,channel in enumerate(self.chan_list):
                if (pump_times[index] != 0):
                    GPIO.output(channel,1)  
                    time.sleep(pump_times[index])
                    print("Finished pouring")
                    GPIO.output(channel, 0)
#CLEAN

