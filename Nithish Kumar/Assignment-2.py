import random
while(True):
    x = random.randint(10, 99)
    y = random.randint(10, 99)
    if (x > 35 and y > 60):
        print("The Temperature is: ",x,"`C")
        print("The Humidity is: ", y,"%")
        print("Alarm is ON")
    else:
        print("The Temperature is: ",x,"`C")
        print("The Humidity is: ", y,"%")
        print("Alarm is OFF")
        break