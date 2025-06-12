from PIL import Image, ImageOps
import sys

try:
  if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit()
  elif len(sys.argv) > 4:
    print("Too many command-line arguments")
    sys.exit()
  elif not sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".jpeg") or sys.argv[1].endswith(".png"):
    print("Invalid input")
    sys.exit()
  elif not sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".jpeg") or sys.argv[2].endswith(".png"):
    print("Invalid output")
    sys.exit()
  elif sys.argv[1].endswith() != sys.argv[2].endswith():
    print("Input and output have different extensions")
    sys.exit()

  images = []

  for sys.argv[1] in sys.argv:
      input = Image.open(sys.argv[1])
      ImageOps.fit(shirt.png, size: [], centering: (0.5, 0.5))
      Image.paste(im: shirt.png)
      Image.save(sys.argv[2])

except FileNotFoundError:
    print("File does not exist")
    sys.exit()