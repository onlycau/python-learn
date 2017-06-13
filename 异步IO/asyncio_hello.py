#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#asyncio Hello wordl

import threading
import asyncio

async def hello():
	print("Hello world!(%s)" %threading.currentThread())
	#异步调用asyncio.sleep(1):
	r=await asyncio.sleep(1)
	print("Hello again!(%s)" %threading.currentThread())

#获取Eventloop:
loop=asyncio.get_event_loop()
#执行coroutine
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()