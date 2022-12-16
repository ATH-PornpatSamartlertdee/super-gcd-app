from super_gcd.gcd import gcd

def test_gcd_of_3_and_6():
    result = gcd(3,6)
    assert result == 3

def test_gcd_of_6_and_3():
    result = gcd(6,3)
    assert result == 3

def test_gcd_of_4137_and_231252():
    result = gcd(4137,231252)
    assert result == 21

def test_gcd_of_4_and_6():
    result = gcd(4,6)
    assert result == 2

def test_gcd_of_6_and_4():
    result = gcd(6,4)
    assert result == 2

def test_gcd_of_str3_and_6():
    result = gcd('3',6)
    assert result == "You're shocked!"

def test_gcd_of_3_and_str6():
    result = gcd(3,'6')
    assert result == "You're shocked!"

def test_gcd_of_0_and_5():
    result = gcd(0,5)
    assert result == 5

def test_gcd_of_5_and_0():
    result = gcd(5,0)
    assert result == 5

def test_gcd_of_0_and_neg5():
    result = gcd(0,-5)
    assert result == 5

def test_gcd_of_neg5_and_0():
    result = gcd(-5,0)
    assert result == 5

def test_gcd_of_neg7_and_neg21():
    result = gcd(-7,-21)
    assert result == 7

def test_gcd_of_none_and_neg5():
    result = gcd(None,-5)
    assert result == "You're shocked!"

def test_gcd_of_3_and_neg3():
    result = gcd(3,-3)
    assert result == 3

def test_gcd_of_neg3_and_3():
    result = gcd(-3,3)
    assert result == 3

def test_gcd_of_neg3_and_neg3():
    result = gcd(-3,-3)
    assert result == 3

def test_gcd_of_neg3_and_neg3p5():
    result = gcd(-3,-3.5)
    assert result == "You're shocked!"

