import cmake_example as m


def test_main():
    assert m.__version__ == "0.0.1"
    assert m.add(1, 2) == 3
    assert m.subtract(1, 2) == -1

    a = m.AStruct()
    assert a is not None
    m.fun(a)
    b = m.BStruct(a)
