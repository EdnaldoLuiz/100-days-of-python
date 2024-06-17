import asyncio

async def cumprimentar():
    print('Olá!')
    await asyncio.sleep(1)
    print('Como vai você?')

async def main():
    await cumprimentar()

asyncio.run(main())