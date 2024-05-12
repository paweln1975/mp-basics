# Try to utilize the template given to solve the task.
import asyncio


async def convert_to_fahrenheit(temperature, future):
    future.set_result(9 / 5 * temp + 32 for temp in temperature)


async def convert_to_kelvin(temperature, future):
    future.set_result(temp + 273.15 for temp in temperature)


async def convert_temperatures(temperatures):
    f = asyncio.Future()
    k = asyncio.Future()

    await asyncio.gather(
        convert_to_fahrenheit(temperatures, f),
        convert_to_kelvin(temperatures, k),
    )
    return f.result(), k.result()


celsius_temperatures = [float(i) for i in "0.0 100.0".split()]
results = asyncio.run(convert_temperatures(celsius_temperatures))
print("Fahrenheit: ", end=" ")
print(*results[0])
print("Kelvin: ", end=" ")
print(*results[1])