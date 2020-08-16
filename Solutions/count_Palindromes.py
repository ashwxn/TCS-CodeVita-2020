a_String =input()
def subPgm(a_String):
  for a in range(1,len(a_String)-2):
    if three_palindromic_substrings(a_String[:a]):
      for b in range(a+1,len(a_String)):
        if three_palindromic_substrings(a_String[a:b]) and three_palindromic_substrings(a_String[b:]):
          print(a_String[:a],end="\n")
          print(a_String[a:b],end="\n")
          print(a_String[b:])
          return
  print("Impossible",end='')
def three_palindromic_substrings(a_String):
  aN = len(a_String)
  if aN == 1:
    return True
  for b in range(aN//2):
    if a_String[b] != a_String[-b-1]:
      return False
  return True
subPgm(a_String)
