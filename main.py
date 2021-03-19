from machine import Pin
import utime

led = Pin(21, Pin.OUT)
led.off()
beeper = Pin(18, Pin.OUT)
beeper.off()

SIGNAL_SHORT_DURATION = 0.1
SIGNAL_LONG_DURATION = 3 * SIGNAL_SHORT_DURATION
PAUSE_LETTER = SIGNAL_SHORT_DURATION
PAUSE_WORD = 7 * SIGNAL_SHORT_DURATION #included in dictionary as ' ': '.......'

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
                    '(':'-.--.', ')':'-.--.-'}

def message_encode(message):
  encoded_message = ""
  for letter in message:
    if letter == ' ':
      encoded_message += ' '
    else:
      letter_code = MORSE_CODE_DICT[letter]
      encoded_message += str(letter_code)
    encoded_message += 'w'
  return(encoded_message)

def message_send_led(encoded_message):
  global led
  print(encoded_message)
  for character in encoded_message:
    # Debug
    # End of Debug
    if character == '.':
      print(character)
      led.on()
      utime.sleep(SIGNAL_SHORT_DURATION)
      led.off()
      utime.sleep(SIGNAL_SHORT_DURATION)
    elif character == '-':
      print(character)
      led.on()
      utime.sleep(SIGNAL_LONG_DURATION)
      led.off()
      utime.sleep(SIGNAL_SHORT_DURATION)
    elif character == 'w':
      print(character)
      led.off()
      utime.sleep(PAUSE_LETTER)
    elif character == ' ':
      print(character)
      led.off()
      utime.sleep(PAUSE_WORD)

def message_send_beeper(encoded_message):
  global beeper
  print(encoded_message)
  for character in encoded_message:
    # Debug
    # End of Debug
    if character == '.':
      print(character)
      beeper.on()
      utime.sleep(SIGNAL_SHORT_DURATION)
      beeper.off()
      utime.sleep(SIGNAL_SHORT_DURATION)
    elif character == '-':
      print(character)
      beeper.on()
      utime.sleep(SIGNAL_LONG_DURATION)
      beeper.off()
      utime.sleep(SIGNAL_SHORT_DURATION)
    elif character == 'w':
      print(character)
      beeper.off()
      utime.sleep(PAUSE_LETTER)
    elif character == ' ':
      print(character)
      beeper.off()
      utime.sleep(PAUSE_WORD)

while True:
  message = "Now we try more complex sentense"
  encoded_message = message_encode(message.upper())
  for led_pin in [ 19,20,21 ]:
    led.off()
    led = Pin(led_pin, Pin.OUT)
    message_send_led(encoded_message)
  message_send_beeper(encoded_message)