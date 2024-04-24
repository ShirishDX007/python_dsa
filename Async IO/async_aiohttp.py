import aiohttp
import asyncio

async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()
async def main():
    """ fetch data from urls"""
    urls = [
        'https://gorest.co.in/public/v2/users',
        'https://gorest.co.in/public/v2/todos'
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]

        result = await asyncio.gather(*tasks)
        print(result)
if __name__ == '__main__':
    asyncio.run(main())