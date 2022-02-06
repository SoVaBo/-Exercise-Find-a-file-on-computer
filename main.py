from pathlib import Path


root = Path('.')
fpaths = root.rglob("**/*") 
sitem = input("what is your item to search?: ")
for path in fpaths:
  if path.is_file():
    if sitem in path.stem:
      print(path.absolute())
    