from back_to_the_bank import value

def test_h():
  assert value("hey") == "$20"

def test_hello():
  assert value("hello") == "$0"

def test_other():
  assert value("What's up?") == "$100"
  assert value("let's DANCE!") == "$100"
  assert value("ok") == "$100"