#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类
Base=declarative_base()
#定义user对象
class User(Base):
	__tablename__='user'

	id=Column(String(20),primary_key=True)
	name=Column(String(20))

#初始化数据链接
enginge=create_engine('mysql://root:password@localhost:3306/test')
#创DbBSession类型
DbSession=sessionmake(bind=engine)

#创建session对象
session=DbSession()
#创建新user对象
new_user=User(id='5',name='Bob')
#添加到session
session.add(new_user)
#提交即保存到数据库
session.commit()
#关闭session
session.close()
# 查询
#创建session
session=DbSession()
#创建query查询
user=session.query(User).filter(User.id=='5').one()
#打印类型和对象的name属性
print('type',type(user))
print('name:',user.name)
session.close()