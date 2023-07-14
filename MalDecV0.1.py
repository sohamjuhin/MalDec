import os
import yara

def detect_malware(file_path):
  """Returns True if the file is malware, False otherwise."""
  rules = yara.compile(open("rules.yar", "r").read())
  match = rules.match(file_path)
  return match

def main():
  file_path = "/path/to/file"
  if detect_malware(file_path):
    print("File is malware")
  else:
    print("File is not malware")

if __name__ == "__main__":
  main()
