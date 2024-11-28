import asyncio


async def greet(name):
    print(f"Starting ... hello {name} ")
    await asyncio.sleep(1)
    print(f"Finished ... bye {name}")


async def main():
    await asyncio.gather(
        greet("Alice"),
        greet("Bob"),
        greet("Euro Papa")
    )

    await asyncio.sleep(5)
    future = asyncio.Future()

    # Schedule the setting of the future result
    asyncio.create_task(set_after(future, 2, '...world'))

    print('Hello...', end='')

    # Wait until the future is done
    print(await future)


async def set_after(future, delay, value):
    # Simulate a delay with asyncio.sleep
    await asyncio.sleep(delay)

    # Set the result of the future
    future.set_result(value)

asyncio.run((main()))
