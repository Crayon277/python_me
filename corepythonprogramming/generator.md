# 生成器

在python2.5中，加强了生成器的特性，除了有next（）来获得下个生成的值，用户可以将值回送给生成器【send()】，在生成器中抛出异常，以及要求生成器退出【close()】
由于双向的动作涉及叫做send的代码来向生成器发送值，以及生成器返回的值发送回来，
现在yield语句必须是一个表达是，因为当回到生成器中继续执行的时候，你或许正在接收一个进入的对象
```python
def counter(start_at=0):
  count = start_at
  while True:
    val = (yield count)
    if val is not None:
      count = val
    else:
      count +=1

```
