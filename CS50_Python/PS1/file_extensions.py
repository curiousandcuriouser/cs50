fileName = input("File name: ")

extension = fileName.split('.')[1]

match extension:
  case "gif" | "jgp" | "jpeg" | "png":
    print(f"image/{extension}")
  case "pdf" | "zip":
    print(f"application/{extension}")
  case "txt":
    print(f"txt/plain")