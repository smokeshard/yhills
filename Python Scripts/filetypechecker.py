import os
import mimetypes

# First, get the file's MIME type.
def getMIME(filePath):
  return mimetypes.guess_type(filePath)[0]

# Next, check the file's provided extension.
def checkExtension(filePath):
  if not os.path.isfile(filePath):
    return f"[ERR.] '{filePath}' does not exist."
  fileExtension, _ = mimetypes.guess_type(filePath)
  if fileExtension is None:
    return f"[ERR.] '{filePath}' MIME type could not be determined."
  with open(filePath, 'rb') as f:
    fileHexcode = f.read(4).hex().upper()
  knownMIME = {"89504E47": "image/png", "FFD8FFDB": "image/jpeg", "FFD8FFE0": "image/jpeg", "FFD8FFE1": "image/jpeg", "504B0304": "application/zip",}
  fileMIME = knownMIME.get(fileHexcode, "Unknown")
  if fileMIME == fileExtension:
    return f"[SUCC] '{filePath}' is of type ({fileMIME}) and has a matching extension."
  else:
    return f"[FAIL] '{filePath}' is of type ({fileMIME}), but has an extension claiming ({fileExtension})."

if __name__ == "__main__":
  filePath = input("\nInput an absolute file path: ")
  print(checkExtension)
