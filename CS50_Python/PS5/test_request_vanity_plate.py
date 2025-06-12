from requesting_vanity_plate import is_valid

def test_length():
  assert is_valid("A") == "Invalid"
  assert is_valid("AB34567") == "Invalid"
  assert is_valid("AB") == "Valid"
  assert is_valid("AB1234") == "Valid"

def test_first_letters():
  assert is_valid("123456") == "Invalid"
  assert is_valid("1ABSH67") == "Invalid"
  assert is_valid("AB3456") == "Valid"

def test_0():
  assert is_valid("ABC012") == "Invalid"
  assert is_valid("ABCD10") == "Valid"

def text_letter_after_number():
    assert is_valid("ABC0A1") == "Invalid"
    assert is_valid("ABCD10") == "Valid"