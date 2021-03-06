#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
from http://aiomysql.readthedocs.io/en/latest/examples.html#low-level-api
"""
import asyncio 
import aiomysql

async def test_example_executemany(loop):
	#connect mysql
	conn=await aiomysql.connect(host='127.0.0.1',user='root',password='020202',db='test',loop=loop)

	cur=await conn.cursor()
	async with conn.cursor() as cur:

		#create table music_style	
		await cur.execute("DROP TABLES IF EXISTS music_style;")
		await cur.execute("""CREATE TABLE music_style (id int,name VARCHAR(255),PRIMARY KEY (id));""")
		
		#commit
		await conn.commit()
		
		#insert 3 rows and commit 
		await cur.execute("INSERT INTO music_style VALUES(1,'heavy metal')")
		await cur.execute("INSERT INTO music_style VALUES(2,'death metal')")
		await cur.execute("INSERT INTO music_style VALUES(3,'power metal')")
		await conn.commit()

		#insert 3 row by one long query using *executemane* method
		data=[(4,'gothic metal'),(5,'doom metal'),(6,'post metal')]
		await cur.executemany(
			"INSERT INTO music_style (id,name)"
			"values (%s,%s)",data)
		await conn.commit()

		#fetch all insert row from table music_style
		await cur.execute("SELECT * FROM music_style;")
		result=await cur.fetchall()
		print(result)

	#close connection	
	conn.close()

#run

loop=asyncio.get_event_loop()
loop.run_until_complete(test_example_executemany(loop))
