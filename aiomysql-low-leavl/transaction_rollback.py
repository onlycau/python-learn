#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
from http://aiomysql.readthedocs.io/en/latest/examples.html#low-level-api
"""

import asyncio
import aiomysql

async def test_example_transaction(loop):
	conn=await aiomysql.connect(host='127.0.0.1',user='root',password='020202',db='test',autocommit=False,loop=loop)

	async with conn.cursor() as cursor:

		#check table if in else drop
		stmt_drop="DROP TABLE IF EXISTS names"
		await cursor.execute(stmt_drop)  #cursor.execute(can_be_a_variable)
	
	#create table names and commit
		await cursor.execute("""
			CREATE TABLE names (
			id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
			name VARCHAR(30) DEFAULT '' NOT NULL,
			CNT TINYINT UNSIGNED DEFAULT 0,
			PRIMARY KEY (id))""")
		await conn.commit()

		#Insert 3 records
		names=(('ZhangZhe',),('Jingqi',),('WangWu',))
		stmt_insert="INSERT INTO names (name) VALUES (%s)"
		await cursor.executemany(stmt_insert,names)

		#Roll back
		await conn.rollback()

		#There should be no data
		strmt_select="SELECT id,name FROM names ORDER BY id"
		await cursor.execute(strmt_select)
		resp=await cursor.fetchall()
		
		#check there is no data
		assert not resp
		"""if  resp:
			print(resp)
			raise Exception('there may be some data.')"""

		#do the insert again
		await cursor.executemany(stmt_insert,names)
		await cursor.execute(strmt_select)
		resp=await cursor.fetchall()
		print(resp)

		#Cleaning up,dropping the table again
		await cursor.execute(stmt_drop)
		await cursor.close()
		conn.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(test_example_transaction(loop))
