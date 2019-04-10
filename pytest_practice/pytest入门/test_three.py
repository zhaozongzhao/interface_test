from collections import namedtuple


import  pytest

#clooections  是Python内建的一个集合模块,提供了许多有用的集合类
Task = namedtuple('task',['summary','owner','done','id'])
# 使用__new__.default__创建默认的Task对象,不需要指定所有的属性
Task.__new__.__defaults__ = (None,None,False,None)

def test_defalults():
    # 不适用任何参数调用默认值
    t1 = Task()
    t2 = Task(None,None,False,None)
    assert t1==t2

@pytest.mark.run_these_please
def test_member_access():
    # 检查字段功能应该调用namedtuple
    t = Task('buy milk','brian')
    print(t)
    assert t.summary == 'buy milk'''
    assert t.owner == 'brian'
    assert (t.done,t.id) == (False,None)
