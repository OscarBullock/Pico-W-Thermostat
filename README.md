 # IT Thermostat assignment 
 ----------
 This the IoT project

 # BME280
    Measures the following:
     - Air pressure
     - Temperature
     - Humidity
 
 # SD1306

Displays the following on the **screen**:

# Important!:
1. Open the **Terminal** application
2. Input the following code into the Terminal: 
 -  python3 -m pip install machine
  
# Link:
   Here is the link to our document: 
   <https://cgsacteduau-my.sharepoint.com/:w:/r/personal42432_cgs_act_edu_au/_layouts/15/Doc.aspx?sourcedoc=%7B406351A4-1C10-4902-99F5-99845B5873A8%7D&file=IoT%20rasberry%20pico%20project%20documentation.docx&action=default&mobileredirect=true>

# The program
To load an image use **![The alt text]**

# The code
`print("hello world")`

Here is the input:
```python
#Rasperry Pi Pico with BME280 and SSD1306

from PiicoDev_BME280 import PiicoDev_BME280
from PiicoDev_SSD1306 import create_PiicoDev_SSD1306
from PiicoDev_Unified import sleep_ms # cross-platform compatible sleep function

sensor = PiicoDev_BME280() # initialise the sensor
display = create_PiicoDev_SSD1306() # initialise the display
#zeroAlt = sensor.altitude() # take an initial altitude reading

tempC, presPa, humRH = sensor.values() # read all data from the sensor
pres_hPa = presPa / 100 # convert air pressurr Pascals -> hPa (or mbar, if you prefer)

display.fill(0)
display.text("Temp: "+str(tempC)+" C", 0, 0, 1)
display.text("Pres: "+str(pres_hPa)+" hPa", 0, 10, 1)
display.text("Hum: "+str(humRH)+" %", 0, 20, 1)
display.show()

while True:
    # Print data
    tempC, presPa, humRH = sensor.values() # read all data from the sensor
    pres_hPa = presPa / 100 # convert air pressurr Pascals -> hPa (or mbar, if you prefer)

    display.fill(0)
    display.text("Temp: "+str(tempC)+" C", 0, 0, 1)

    display.text("Pres: "+str(pres_hPa)+" hPa", 0, 10, 1)
    display.text("Hum: "+str(humRH)+" %", 0, 20, 1)
    display.text("Oscar and Ben", 0, 30, 1)
    display.show()

    sleep_ms(1000) # wait 1 second

```
 
Here is the output:
![The output of the code](outputImage.jpeg)

# Purpose
To display temperature, pressure, and humidity data on an OLED screen (SSD1306) using a BME280 sensor. The Raspberry Pi Pico WH will collect the data from the sensor and display it on the screen.


# Set up
 -------
Here are all the required parts
1.	Components:
    -	Raspberry Pi Pico WH
	-	BME280 sensor
	-	SSD1306 OLED display
	-	Breadboard
	-	PiicoDev cable (for connections)
	-	Jumper wires
2. 	Connections:
	◦	BME280 and SSD1306 are connected to the Raspberry Pi Pico WH via the I2C interface (pins GPIO 3 for SDA and GPIO 5 for SCL).
	◦	Both the sensor and the display will share the same I2C lines (SDA and SCL).
	◦	Connect 3.3V from the Pico to the breadboard to power the SSD1306 display (since it's powered separately).
	◦	Connect the GND to the ground rail on the breadboard.
3.	Pin connections:
	◦	Pico GPIO 3 (SDA) -> PiicoDev cable SDA
	◦	Pico GPIO 5 (SCL) -> PiicoDev cable SCL
	◦	3.3V (Pico) -> 3.3V power rail (for SSD1306)
	◦	GND (Pico) -> GND power rail (for SSD1306)
4.	Programming Environment:
	◦	Use MicroPython on the Pico WH.
	◦	Libraries needed: ssd1306.py for the OLED and bme280.py for the sensor.
	◦	These libraries handle communication and data reading from the sensor and displaying it on the screen.



# Usage

Purpose:

Setup:

Usage:
	1	Reading sensor data: The BME280 will measure temperature, pressure, and humidity. The Pico will communicate with it via I2C to read this data.
	2	Displaying data on OLED: Once the data is collected, it will be displayed on the SSD1306 OLED screen. The temperature, pressure, and humidity will refresh periodically, showing live updates.
Code Outline (MicroPython):
python
Copy code
from machine import I2C, Pin
import ssd1306
import bme280

# I2C setup for Pico
i2c = I2C(1, scl=Pin(5), sda=Pin(3))

# OLED setup
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# BME280 setup
sensor = bme280.BME280(i2c=i2c)

while True:
    # Read temperature, pressure, humidity
    temp, pressure, humidity = sensor.values
    
    # Clear the OLED display
    oled.fill(0)
    
    # Display the readings
    oled.text("Temp: " + temp, 0, 0)
    oled.text("Pressure: " + pressure, 0, 10)
    oled.text("Humidity: " + humidity, 0, 20)
    
    # Update the display
    oled.show()
    
    # Sleep for a second
    time.sleep(1)
This code will continuously read the temperature, pressure, and humidity from the BME280 and display it on the SSD1306 screen.
Let me know if you need more details or help with specific parts of the setup!

	

 Hardware
---------

**Core Electronics hardware is released under [Creative Commons Share-alike 4.0 International](http://creativecommons.org/licenses/by-sa/4.0/).**
 
 # Image references
 <https://iotprojectsideas.com/interface-bme280-with-raspberry-pi-pico-using-micropython/>

 <https://peppe8o.com/ssd1306-i2c-oled-raspberry-pi-pico-micropython/>
 
 
 # PiicoDev® BME280 MicroPython Module

This is the firmware repo for the Core Electronics [PiicoDev® Atmospheric Sensor BME280](https://core-electronics.com.au/catalog/product/view/sku/CE07503).

This module depends on the [PiicoDev Unified Library](https://github.com/CoreElectronics/CE-PiicoDev-Unified).

See the Quickstart Guides:
- [Micro:bit v2](https://core-electronics.com.au/tutorials/piicodev-atmospheric-sensor-bme280-quickstart-guide-for-microbit.html)
- [Raspberry Pi Pico](https://core-electronics.com.au/tutorials/piicodev-atmospheric-sensor-bme280-quickstart-guide-for-rpi-pico.html)

 
 
 
 # PiicoDev® OLED Module SSD1306 -  MicroPython Module

This is the firmware repo for the [Core Electronics PiicoDev® OLED Module](https://core-electronics.com.au/catalog/product/view/sku/CE07911)

This module depends on the [PiicoDev Unified Library](https://github.com/CoreElectronics/CE-PiicoDev-Unified), include `PiicoDev_Unified.py` in the project directory on your MicroPython device.
