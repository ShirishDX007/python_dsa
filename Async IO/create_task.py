import asyncio
import time

async def call_api(message, result=1000, delay=3):
    #print(message)
    await asyncio.sleep(delay)
    return result

async def show_message():
    for _ in range(3):
        await asyncio.sleep(1)
        print("API call is in the process..")

async def main():
    start = time.perf_counter()
    message_task = asyncio.create_task(
        show_message()
    )
    task_1 = asyncio.create_task(
        call_api("Call API for stock price of Reliance", 3000)
    )
    task_2 = asyncio.create_task(
        call_api("Call API for stock price of Maruti", 12500)
    )
    price = await task_1
    print(price)

    price = await task_2
    print(price)

    await message_task

    end_time = time.perf_counter()
    print(f" {round(end_time-start),0} seconds to complete.")

asyncio.run(main())