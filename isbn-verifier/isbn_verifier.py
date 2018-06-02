def calculate(isbn_list):
  val = 0
  for i, j in zip(range(0, len(isbn_list)), range(len(isbn_list), 0, -1)):
    val += isbn_list[i] * j
  return val % 11 == 0     

def verify(isbn):
  isbn_list = list(map(int, list(filter(str.isdigit, isbn))))
  if len(isbn_list) == 10:
    return calculate(isbn_list) 
  else:
    if(len(list(filter(str.isalnum, isbn))) == 10 and isbn.endswith('X')):
      isbn_list.append(10)
      return calculate(isbn_list)
    return False