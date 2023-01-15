import glob

files = glob.glob("./*")
for file in files:
    ex = file.split(".")[-1]
    if ((ex == "png") or (ex == "jpg")):
      print(file)

