# Try to utilize the template given to solve the task.
import asyncio


async def calculate_sum(numbers, future):
    suma = 0
    for s in numbers:
        suma += s
    future.set_result(suma)


async def calculate_product(numbers, future):
    pr = 1
    for s in numbers:
        pr *= s
    future.set_result(pr)


async def calculate_results(numbers):
    future_sum = asyncio.Future()
    await asyncio.create_task(calculate_sum(numbers, future_sum))

    future_product = asyncio.Future()
    await asyncio.create_task(calculate_product(numbers, future_product))

    return await future_sum, await future_product


numbers = [int(i) for i in "1 2 3 4 5".split()]
results = asyncio.run(calculate_results(numbers))
print(", ".join([str(i) for i in results]))
