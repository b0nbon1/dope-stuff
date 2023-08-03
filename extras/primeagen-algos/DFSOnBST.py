def search(curr, needle):
    if not curr:
        return False
    if curr.value == needle:
        return True
    if curr.value < needle:
        return search(curr.right, needle)
    return search(curr.left, needle)

def dfs(head, needle):
    return search(head, needle)