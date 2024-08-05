import anvil.pico
import uasyncio as asyncio
from Anvilfn import anvilconnect


# Asynchronous main function
async def main():
    asyncio.create_task(anvilconnect())
    
    while True:
        try:
            if True:
                await asyncio.sleep_ms(1000)   # Sleep for 1 seconds
        except OSError as e:
            print('Main error')
        await asyncio.sleep_ms(0)   # Sleep for 0.1 seconds

try:
    asyncio.run(main())  # Run the main asynchronous function
except OSError as e:
    print('Runtime error')
finally:
    asyncio.new_event_loop() #Create a new event loop


