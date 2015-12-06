def RunLength(a):
  count = 0
  letter = ''
  enc = ''
  a = str(a)
  for c in a:
    if c == letter:
      count += 1
    if c != letter:
      if count == 0:
        count = 1
        letter = c
      else:
        enc += '%d%s' % (count, letter)
        count = 1
        letter = c
  enc += '%d%s' % (count, letter)
  return enc


def getRows(a):
    b = "1"
    for x in range(a):
        print(b)
        b = RunLength(b)

getRows(int(input("Enter a number of iterations: ")))




