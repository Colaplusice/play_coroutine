# coroutine 学习

## 生成器管道

类似于Linux shell的管道

tail -f | grep python

logfile = open("access-log")
loglines = follow(logfile)
pylines = grep("python",loglines)


# 协程的激活关闭
    a=next(func)
    a.send()
    a.close()

一个生成器函数，你调用他，其实他并没有在执行代码，而是在调用next()之后才会执行代码。
而且会循环产出。结果不会保存在内存。 当然生成器转list的过程，next方法就自动调用了。

调用send()方法后，会生成一个生成器对象。或者一个coroutine函数调用send()方法
将value发送到函数内部的yield的左边。
    
    
1. Generators产生数据
2. Coroutines消费数据
3. coroutines和iteration没有联系

协程pipeline 
接收---->读取---->打印
    
    
## 解析xml

parse_xml_buses.py  通过yield来解析xml

## 结论 so far

1. coroutine is similar to generators
2. can process data through  coroutine pipeline
3. 可以通过协程来开发事件驱动系统


## 并发的几种模式

- 发送data通过 coroutine
- 发送data通过 threads
- 发送data通过 processes

可以包装coroutine在thread中或者在subprocess中


## 通过thread传递data
threading.Thread(target=func)

## 通过subprocess传递data

sendto()------>pipe/socket--->recvfrom()
pickle.dump                 pickle.load
通过pickle来打包数据

## coroutine task

feture:
- 独立的控制流  
- internal state
- 可以被调度
- 可以和其他的task进行
- 只有当协程激活时，里面的变量才会生效
- 协程可以suspend和resume yield将协程suspend send又将协程resume，close终止协程


## 多任务

## 操作系统如何处理并发以及多个进程
1. 操作系统运行多个进程同时执行，采取的方法是在多个task之间快速切换
2. 操作系统如何进行上下文切换: 通过trap和interrupt
- interrupt: 硬件相关的信号 键盘。i/o设备
- traps: 软件相关的signal

- trap是让操作系统工作的部分，系统将你的程序丢到cpu里去执行，除非遇到trap(系统调用)，
遇到trap后，程序suspend起来，然后操作系统进行执行调用的程序。repeat...
- 每次遇到trap，系统就切换到另一个task

运行

## 一些观点

yield 类似于操作系统的trap
当一个生成器遇到yield时，马上会停止执行，让步出去
控制权转交到让执行生成器的代码
如果你将yield当做trap，你能够构造一个多任务的操作系统，纯python


## coroutine 的一些坑

1. 一个coroutine上的send() method必须正确的协调
2. 如果coroutine已经运行起来了，就不能调用send方法了

# part 7 构造一个操作系统

- 纯python
- 没有线程
- 没有子进程
- 使用生成器和协程

## 动机，为什么要学concurrent呢

- 非阻塞和异步io
- 事件驱动系统
- 并发
