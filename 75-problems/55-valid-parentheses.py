def isValid(self, s: str) -> bool:
  brackets = []
  for i in s:
      if i == "(" or i == "[" or i == "{":
          brackets.append(i)
      elif len(brackets) == 0:
          return False
      elif i == ")" and brackets[-1] == "(":
          brackets.pop()
      elif i == "}" and brackets[-1] == "{":
          brackets.pop()
      elif i  == "]" and brackets[-1] == "[":
          brackets.pop()
      else:
          return False
  return len(brackets) == 0