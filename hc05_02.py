#Diyprojectslab.com
 
from machine import Pin, UART
 
uart = UART(0, 9600)
led = Pin(25, Pin.OUT)
 
while True:
    
  #uart.write('LED on \n')
  if uart.any() > 0:
    data = uart.read()
    print(data)
    if "on" in data:
      led.value(1)
      print('LED on \n')
      uart.write('LED on \n')
    elif "off" in data:
      led.value(0)
      print('LED off \n')
      uart.write('LED off \n')