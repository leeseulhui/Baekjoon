import sys
input = sys.stdin.readline

def preorder(start):
    if start != -18:
        print(chr(start + 64), end="")  #전위
        preorder(tree[start][0])
        preorder(tree[start][1])
def inorder(start):
    if start != -18:
        inorder(tree[start][0])
        print(chr(start+64), end="")    #중위
        inorder(tree[start][1])

def postorder(start):
    if start != -18:
        postorder(tree[start][0])
        postorder(tree[start][1])
        print(chr(start+64), end="")    #후위


n = int(input())
tree = [[] for _ in range(n+1)]

#아스키 코드로 변환
for i in range(n):
    a, b, c = input().split()
    a, b, c = ord(a)-64, ord(b)-64, ord(c)-64

    tree[a].append(b)
    tree[a].append(c)

preorder(1)
print()
inorder(1)
print()
postorder(1)
print()