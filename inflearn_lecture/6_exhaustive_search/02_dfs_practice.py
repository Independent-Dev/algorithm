graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7]
}
visited = [False] * 8

def preorder(x):
    print(x, end=" ")
    if x in graph:
        preorder(graph[x][0])
        preorder(graph[x][1])
        

def inorder(x):
    if x in graph:
        inorder(graph[x][0])

    print(x, end=" ")

    if x in graph:
        inorder(graph[x][1])

def postorder(x):
    if x in graph:
        postorder(graph[x][0])
        postorder(graph[x][1])
    print(x, end=" ")


preorder(1)
print()
inorder(1)
print()
postorder(1)