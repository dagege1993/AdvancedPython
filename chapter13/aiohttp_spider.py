# asyncio爬虫.去重.入库
import asyncio
import re

import aiohttp
import aiomysql
from pyquery import PyQuery

start_url = "http://www.jobbole.com"
waitting_urls = []
seen_urls = set()


async def fetch(url, session):
    async with session.get(url) as resp:
        try:
            print("resp.status :{}".format(resp.status))
            if resp.status in [200, 201]:
                data = await resp.text()
                return data
        except Exception as e:
            print(e)


def extract_urls(html):
    urls = []
    pq = PyQuery(html)
    for link in pq.items('a'):
        url = link.attr("href")
        if url and url.startwith("http") and url not in seen_urls:
            urls.append(url)
            waitting_urls.append(url)
    return urls


async def init_urls():
    html = await fetch(start_url)
    extract_urls(html)


async def article_handler(url, session):
    # 获取文章详情并且解析入库
    html = await fetch(url, session)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq("title").text()


async def consumer():
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waitting_urls) == 0:
                await asyncio.sleep(0.5)
                continue
            url = waitting_urls.pop()
            print("start get url: {}".format(url))
            if re.match('http://.*?jobbole.com/\d+/', url):
                if url not in seen_urls:
                    asyncio.ensure_future(
                        article_handler(url, session))  # ensure_future()函数可以把一个协程封装成一个任务，然后这个任务就可以传送给别的代码


async def main(loop):
    # 等待mysql建立连接
    pool = await aiomysql.create_pool(host="127.0.0.1", port=3306,
                                      user="root", password="",
                                      db="mysql", loop=loop,
                                      charset="utf8", autocommit=True
                                      )
    asyncio.ensure_future(init_urls())
