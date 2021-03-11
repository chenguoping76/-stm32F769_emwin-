

import asyncio


async def first():
    print('first函数调用开始,下面将会等待3秒模拟函数运行完毕')
    await asyncio.sleep(3)
    print('first函数执行完毕')


async def last():
    print('last函数调用开始')
    await asyncio.sleep(2)
    print('last函数执行完毕')


async def func(delay):
    print('开始异步同时执行的函数+延迟: ' + str(delay))
    await asyncio.sleep(delay)
    print('--异步函数执行完毕+延迟: ' + str(delay))


async def main():
    await first()  # 这里先调用first()函数,并且等它执行完了才会开始
    await asyncio.gather(
        func(1),
        func(2),
        func(3)
    )
    await last()


asyncio.run(main())
