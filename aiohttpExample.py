import aiohttp
import asyncio
from datetime import datetime

async def main():
    """
    超时属性有(单位为秒)
    total：整个操作时间包括连接建立，请求发送和响应读取。
    connect：该时间包括建立新连接或在超过池连接限制时等待池中的空闲连接的连接。
    sock_connect：连接到对等点以进行新连接的超时，不是从池中给出的。
    sock_read：从对等体读取新数据部分之间的时间段内允许的最大超时
    """
    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout = timeout) as client:
        html = await client.get('https://www.baidu.com/', timeout = timeout)
        print(i)

loop = asyncio.get_event_loop()

tasks = []
for i in range(100):
    task = loop.create_task(main())
    tasks.append(task)

start = datetime.now()

loop.run_until_complete(main())

end = datetime.now()

print('花费时间为：', end - start)
