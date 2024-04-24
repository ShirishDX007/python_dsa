import asyncio
import time

class Breakfast:
    async def make_coffee(self, name):
        self.name = name
        return f" your {self.name} Coffee is getting prepared.."

    async def make_sandwhich(self, seconds):
        await asyncio.sleep(seconds)
        return f"finished async sandwich in {seconds} seconds."

async def main():
    breakfast = Breakfast()
    coffee_task = breakfast.make_coffee('cappacino')
    sandwich = breakfast.make_sandwhich(3)
    coffee_result = await coffee_task
    sandwich_result = await sandwich

    print(coffee_result)
    print(sandwich_result)

asyncio.run(main())

