from PS7.watch_on_youtube import parse

def test_parse_short():
  assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"

def test_parse_long():
  assert parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == "https://youtu.be/xvFZjo5PgG0"

def test_parse_invalid():
  assert parse('<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>') == "None"