#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
from http://aiomysql.readthedocs.io/en/latest/examples.html#low-level-api
"""

import asyncio
import aiomysql

async def test_example(loop):
	pool=await aiomysql.create_pool(host='127.0.0.1',user='root',
		password='020202',db='mysql',loop=loop)
	
	async with pool.acquire() as conn:
		async with conn.cursor() as cur:
			await cur.execute("SELECT 42;")
			print(cur.description)
			(r,)=await cur.fetchone()
			assert r==42
	pool.close()
	await pool.wait_closed()


loop=asyncio.get_event_loop()
loop.run_until_complete(test_example(loop))