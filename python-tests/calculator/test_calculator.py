import calculator

def test_add():
    assert calculator.add(2,4)==6

def test_sub():
    assert calculator.sub(4,3)==1

def test_mul():
    assert calculator.mul(4,3)==12

def test_div():
    assert calculator.div(12,3)==4

def test_rem():
    assert calculator.rem(12,10)==2