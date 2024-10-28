#Rasperry Pi Pico with BME280 and SSD1306
from PiicoDev_BME280 import PiicoDev_BME280
from PiicoDev_SSD1306 import create_PiicoDev_SSD1306
from PiicoDev_Unified import sleep_ms # cross-platform compatible sleep function

sensor = PiicoDev_BME280() # initialise the sensor
display = create_PiicoDev_SSD1306() # initialise the display
#zeroAlt = sensor.altitude() # take an initial altitude reading

tempC, presPa, humRH = sensor.values() # read all data from the sensor
pres_hPa = presPa / 100 # convert air pressurr Pascals -> hPa (or mbar, if you prefer)

display.fill(0) # Clears the display
display.text("Temp: "+str(tempC)+" C", 0, 0, 1) # Writes the temperature to the display
display.text("Pres: "+str(pres_hPa)+" hPa", 0, 10, 1) # Writes the pressure to the display
display.text("Hum: "+str(humRH)+" %", 0, 20, 1) # Writes the humidity to the display
display.show() # Shows the display

while True:
    # Print data
    tempC, presPa, humRH = sensor.values() # read all data from the sensor
    pres_hPa = presPa / 100 # convert air pressurr Pascals -> hPa (or mbar, if you prefer)

    display.fill(0) # Clears the display
    display.text("Temp: "+str(tempC)+" C", 0, 0, 1) # Writes the temperature to the display

    display.text("Pres: "+str(pres_hPa)+" hPa", 0, 10, 1) # Writes the pressure to the display
    display.text("Hum: "+str(humRH)+" %", 0, 20, 1) # Writes the humidity to the display
    display.text("By: Oscar and Ben", 0, 30, 1) # Writes the humidity to the display
    display.show() # Shows the display

    sleep_ms(1000) # wait 1 second