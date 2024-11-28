# Try to utilize the template given to solve the task.
import asyncio


async def convert_to_fahrenheit(celsius_temps):
    return (9 / 5 * temp + 32.0 for temp in celsius_temps)


async def convert_to_kelvin(celsius_temps):
    return (temp + 273.15 for temp in celsius_temps)


async def convert_temperatures(celsius_temps):
    tasks = [asyncio.create_task(convert_to_fahrenheit(celsius_temps)),
             asyncio.create_task(convert_to_kelvin(celsius_temps))
             ]
    return await asyncio.gather(*tasks)


celsius_temperatures = [float(i) for i in "0.0 100.0".split()]
results = asyncio.run(convert_temperatures(celsius_temperatures))
print("Fahrenheit: ", end=" ")
print(*results[0])
print("Kelvin: ", end=" ")
print(*results[1])
