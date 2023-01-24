import glob

with open('README.md', 'w') as f:
  files = glob.glob("./*")
  for file in files:
      ex = file.split(".")[-1]
      if ((ex == "png") or (ex == "jpg")):
        print("- " + file,file=f)
        print("![](" + file + ")",file=f)
