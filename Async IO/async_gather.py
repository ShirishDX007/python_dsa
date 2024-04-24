import asyncio
from datetime import datetime
import click


async def task_one():
    await asyncio.sleep(3)
    return "task one completed."
async def task_two():
    await asyncio.sleep(2)
    return "task two completed."
async def main():
    task1, task2 = await asyncio.gather(task_one(), task_two())
    print(task1)
    print(task2)
start = datetime.now()
asyncio.run(main())

click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
