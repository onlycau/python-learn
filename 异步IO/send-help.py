def h():
	print('start')
	d=yield 5# 1)yield将5生成出去,流程阻塞
                # 2)yield返回被新设置的表达式的值
	print(d)
	m=yield(6)
	print(m) #一般不执行，生成器直接退出
	yield 7
	
c=h()
t=c.send(None)# send用来设置生成器的输入与输出： 参数输入，返回值输出
print(t)
print("........")

t=c.send('Lux')
print(t)

t=c.send('ACE')
print(t)