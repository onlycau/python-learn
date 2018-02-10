#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import aiomysql

async def test_example(loop):
	conn=await aiomysql.connect(host='127.0.0.1',port=3306,user='root',password='020202',db='test',loop=loop)
	async with conn.cursor() as cur:
		await cur.execute("SELECT name from user2 where id=1")
		print(cur.description)
		r=await cur.fetchall()
		print(r)
	conn.close

loop=asyncio.get_event_loop()
loop.run_until_complete(test_example(loop))