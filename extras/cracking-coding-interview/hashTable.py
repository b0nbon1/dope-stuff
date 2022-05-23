def hashStringToInt(s, tableSize):
  hash = 17
  for i in range(len(s)):
    hash = (13*hash* ord(s[i])) % tableSize
  
  return hash


class HashTable:
  def __init__(self) -> None:
      self.table = [None]*1
      self.numItems = 0
  
  def resize(self):
    newTable = [None]*len(self.table)*2
    for item in self.table:
      if item:
        for key,value in item:
          idx = hashStringToInt(key, len(newTable))
          if newTable[idx]:
            newTable[idx].append([key, value])
          else:
            newTable[idx] = [[key, value]]
    self.table = newTable
      

  def setItem(self, key, value):
    self.numItems+=1
    loadFactor = self.numItems/len(self.table)
    if loadFactor > .8:
      self.resize()
    idx = hashStringToInt(key, len(self.table))
    if self.table[idx]:
      self.table[idx].append([key, value])
    else:
      self.table[idx] = [[key, value]]
  
  def getItem(self, key):
    idx = hashStringToInt(key, len(self.table))
    if not self.table[idx]:
      return None
    return next((x for x in self.table[idx] if x[0] == key), [None,None])[1]


myTable = HashTable()
myTable.setItem("firstName", "Bonvic")
myTable.setItem("lastName", "Bundi")

print(myTable.getItem("firstName"))
print(myTable.getItem("lastName"))
print(len(myTable.table))
