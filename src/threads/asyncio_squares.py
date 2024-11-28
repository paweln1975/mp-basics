# Try to utilize the template given to solve the task.
import asyncio


async def square_number(number):
    return number * number


async def parallel_execution(numbers):
    t = [asyncio.create_task(square_number(n)) for n in numbers]
    res = [await task for task in t]
    return res


numbers = [int(i) for i in "1 2 3 4 5".split()]
results = asyncio.run(parallel_execution(numbers))
print(*results)
