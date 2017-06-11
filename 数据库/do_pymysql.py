#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql

connection=pymysql.connect(
	user='root',
	password='password',
	db='test')
cursor=connection.cursor()
cursor.execute('insert into user (id,name)values (%s,%s)',['3','Huixihan'])
cursor.rowcount
connection.commit()
cursor.close()

cursor=connection.cursor()
cursor.execute('select * from user where id =%s',('2',))
values=cursor.fetchall()
print(values)