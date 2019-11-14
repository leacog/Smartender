import RPi.GPIO as GPIO
import robobar

smartender = robobar.Bartender(cal_val=1)

techilla_recipe = {"vodka": 1, "tequilla": 2, "cola": 3, "soda": 0, "snaps": 0}  
techilla = robobar.Drink("techilla", techilla_recipe)
smartender.make(techilla)

GPIO.cleanup()

