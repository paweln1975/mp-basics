import asyncio


async def square(num):
    return num ** 2


async def parallel_execution(nums):
    tasks = []
    for num in nums:
        tasks.append(asyncio.create_task(square(num)))
    return await asyncio.gather(*tasks)


numbers = [int(i) for i in " 1 2 3 4 5".split()]
results = asyncio.run(parallel_execution(numbers))
print(*results)