#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#协程尝试

def consumer():
	r=''
	while True:
		n=yield r#yield接收外部value 不保存内部value
		if not n:
			return
		print('[CONSUMER] Consuming %s...'%n)
		r='200 OK'

def produce(c):
	c.send(None)#启动生成器
	n=0
	while n<5:
		n=n+1
		print('[PRODUCER] Producing %s...' %n)
		r=c.send(n)
		print('[PRODUCER] Consumer return: %s' %r)
	c.close()#关闭协程 过程结束

c=consumer()
produce(c)