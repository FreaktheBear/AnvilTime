import anvil.pico
import machine
import time
import LocalTime
import uasyncio as asyncio
from machine import Pin
from machine import RTC
from Secrets import secrets
from dht import DHT11

# We use the LED to indicate server calls and responses.
sensor = DHT11(Pin(13))

location = LocalTime.localtime('NZ', False)  # Example: NZ with daylight saving

UPLINK_KEY = secrets['uplink']

async def anvilconnect():
    # Update time depends on the call from the Anvil ServerModule, e.g. 2s

    async def record_data():
        while True:
            sensor.measure()
            nowutc = time.time()
            local_time, local_time_str = location.get_local_time()
            print(f"Time = {local_time_str}, Temp = {sensor.temperature()}, Hum = {sensor.humidity()}")
            await anvil.pico.call("record_reading", sensor.temperature(), sensor.humidity(), nowutc)
            await asyncio.sleep(0)


    # Connect the Anvil Uplink. In MicroPython, this call will block forever.

    anvil.pico.connect(UPLINK_KEY, on_first_connect=record_data())

