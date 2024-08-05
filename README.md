# Pi Pico LocalTime Class #
This Anvil.Works project contains a Micropython LocalTime.py class which returns the local time for any Timezone (including DST offset when applicable).
This software is tested on a Raspberry Pi Pico W and works together with the AnvilDashboardTempHum repository.
The Pico is flashed with the following Anvil firmware: https://github.com/anvil-works/anvil-pico/releases/tag/v0.2.0

## Used third party info ##
The timezone information and DST formulas are based on the information from the following websites:
http://www.webexhibits.org/daylightsaving/i.html (EU formulas valid from 1996 till 2099)
https://www.worlddata.info/timezones/
All timezones, DST, and shift times have been accounted for, which obviously presents some doubles in the actual timezone entries.
A separate (more compact) class will be created which only has the absolute Standard Time offsets and only codes for the timezones which use DST.
To keep it as lean as possible you can also just create an entry for your specific timezone.

Use this class at your own risk!

### AnvilTime Example ###
In this AnvilTime example the LocalTime.py class is called from from the Anvilfn.py function via the following instructions:

_import LocalTime_

_location = LocalTime.localtime('NZ', False)  # Example: NZ with daylight saving_

_local_time, local_time_str = location.get_local_time()_

Local time will be returned in a tuple format and a string which is more useable for timestamp recording lets say on a SDcard.
The time string returns resolution back in microseconds. However caution needs to be taken as I don't know how accurate the onboard Pico RTC is.
Still, the fact that resolution is in microseconds should make it possible to use this class for a device which is used for example to capture sequence of events.
The I2C DS3231 module can be used if a more accuracy RTC is needed (have not experimented with this device).

The AnvilTime example program is a simple example which takes the current temperature and humidity from a DHT11 sensor.
The "main.py" routine is created as an asynchronous main function and the "Anvilfn.py" function is called from main.
The program/project can be expanded with your own asyncio concurrent "subroutine" calls.
