#pylint: skip-file
import spidev
import time
import RPi.GPIO as io
from MCP3008 import MCP3008

mcp=MCP3008()



try:
  while True:
    x = mcp.read()
    print(x)
    temp_c = round((x* 3.3/1023)*100, 2)

    # Convert Celsius degrees to Farenheit
    temp_f = round(temp_c * 1.8 + 32, 2)

    # Print both temperatures
    print('Temp: {}ºC    {}ºF'.format(temp_c, temp_f))


    time.sleep(1)

 
except KeyboardInterrupt:
  mcp.spi.close()
  io.cleanup()
finally:
  print("Script gestopt")