from machine import Pin,ADC
import utime

adc = ADC(26)
TEMPERATURE_SENSOR = ADC(4)
CONVERSION_FACTOR = 3.3 / (65535)
RED_LED = Pin(21, Pin.OUT)
GREEN_LED = Pin(20, Pin.OUT)
BLUE_LED = Pin(19, Pin.OUT)
LEDS = [RED_LED, GREEN_LED, BLUE_LED]
for led in LEDS:
  led.off()
while True:
  val = adc.read_u16() * CONVERSION_FACTOR
  reading = TEMPERATURE_SENSOR.read_u16() * CONVERSION_FACTOR
  temperature = 27 - (reading - 0.706)/0.001721
  print(val)
  RED_LED.toggle()
  utime.sleep(2)