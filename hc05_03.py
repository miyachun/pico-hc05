from machine import Pin,UART
uart = UART(0, 9600)
led = Pin(25, Pin.OUT)

codeon=b'\x4c\x45\x44\x44\x20\x6f\x6e'
codeoff=b'\x4c\x45\x44\x44\x20\x6f\x66\x66'

while True:
    if uart.any():
        data = uart.read()
        print(data)
        if data== b'on\r\n':
            led.high()            
            uart.write(bytes(codeon))
            print("LED is ON")
        elif data==b'off\r\n':
            led.low()            
            uart.write(bytes(codeoff))
            print("LED is OFF")