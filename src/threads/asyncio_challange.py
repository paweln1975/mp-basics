# what will be printed ?
import asyncio


async def task_one():
    print("Starting task one")
    await asyncio.sleep(2)
    print("Task one completed")

async def task_two():
    print("Starting task two")
    await asyncio.sleep(1)
    print("Task two completed")


async def print_numbers():
    for i in range(5):
        await asyncio.sleep(0.5)
        print(i, end=' ')


async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_numbers())

    await task1
    await task2
    print("Await sync")
    await asyncio.gather(task_one(), task_two())
    print("Main function completed")

asyncio.run(main())
