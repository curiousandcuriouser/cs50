from testing_my_twitter import shorten

def test_vowels ():
    assert shorten("AEIOU") == "Output: "
    assert shorten("aeiou") == "Output: "