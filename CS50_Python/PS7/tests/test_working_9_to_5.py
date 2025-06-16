from PS7.working_9_to_5 import convert

def test_conversion():
  assert "9 AM to 5 PM" == "09:00 to 17:00"
  assert "9:00 AM to 5:00 PM" == "09:00 to 17:00"
  assert "10 AM to 8:50 PM" == "10:00 to 20:50"
  assert "10:30 PM to 8 AM" == "22:30 to 08:00"

def test_error():
  assert "9:60 AM to 5:60 PM" == ValueError
  assert "9 AM - 5 PM" == ValueError
  assert "09:00 AM - 17:00 PM" == ValueError