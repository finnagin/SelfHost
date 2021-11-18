def test_pass():
  assert True

def test_fail():
  assert False

def test_secret():
  with open("secret.txt", "r") as fid:
    test_string = fid.readline().rstrip()
  assert test_string == "asdf"
