from machine import Pin
import utime

led = Pin(20, Pin.OUT)

s_short = 0.05
s_long = 3 * s_short
letter_pause = s_short
word_pause = 7 * s_short #included in dictionary as ' ': '.......'

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-',' ': '.......'}

def message_send(message):
  global led
  for letter in message:
    try:
      letter_code = MORSE_CODE_DICT[letter]
      print(letter)
      print(letter_code)
      for character in letter_code:
        led.off()
        utime.sleep(letter_pause)
        if character == ".":
          led.on()
          utime.sleep(s_short)
        elif character == "-":
          led.on()
          utime.sleep(s_long)
    except:
      break
while True:
  for led_pin in [ 19,20,21 ]:
    led.off()
    led = Pin(led_pin, Pin.OUT)
    message = "This message will repeat all the time"
    message_send(message.upper())