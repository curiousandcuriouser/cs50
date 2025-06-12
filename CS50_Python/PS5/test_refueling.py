from refueling import convert, gauge

def test_gauge():
  assert gauge("75") == "75%"
  assert gauge("1") == "E"
  assert gauge("99") == "F"
