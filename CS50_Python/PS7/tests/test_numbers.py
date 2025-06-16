from PS7.numb3rs import validate

def test_validate_0_9():
  assert validate("0.0.0.0") == True

def test_validate_correct():
  assert validate("127.0.0.1") == True
  assert validate("255.255.255.255") == True

def test_validate_high():
  assert validate("512.512.512.512") == False
  assert validate("1.2.3.1000") == False

def test_validate_words():
  assert validate("cat") == False