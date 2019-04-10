from collections import namedtuple
import pytest
import time
Task = namedtuple('task',['summary','owner','done','id'])
Task.__new__.__defaults__ = (None,None,False,None)

def test_asdit():

  t_task =  Task('do somehing','okken',True,21)
  print(type(t_task),t_task)
  #返回一个将字段类型映射到其值的新dict
  t_dict =  t_task._asdict()
  expected = {'summary':'do somehing',
              'owner':'okken',
              'done':True,
              'id':21}
  assert t_dict == expected

@pytest.mark.run_these_please
def test_replace():
    time.sleep(2)
    t_before = Task('finish book','brian',False)
    print(t_before)
    # __replace 返回一个新的命名元祖对象,用新值替换指定的字段
    t_after = t_before._replace(id =10,done = True)
    t_expected = Task('finish book','brian',True,11)
    assert t_after == t_expected


