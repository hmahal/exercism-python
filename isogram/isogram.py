def is_isogram(string):
  string = ''.join(filter(str.isalnum, string.lower()))
  return len(set(string)) == len(string)
