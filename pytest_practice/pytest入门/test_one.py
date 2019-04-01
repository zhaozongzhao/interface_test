def test_passing():
    assert (1,2,3) == (1,2,3)


def test_two():
    print('重新执行')
    assert (1,2,3)==(3,2,1)
    assert 1 in (1,2,3)
    assert 2 not in (1,2,3)