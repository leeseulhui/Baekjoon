def _union(A, B):
    # 최대 높이를 확인해서 합해준다. -> 효과적으로 합해줄 것
    A = _find(A)
    B = _find(B)

    if A == B:
        return 
    
    if rank[A] < rank[B]:
        par[A] = B
    elif rank[B] < rank[A]:
        par[B] = A  
    else:
        par[A] = B # 반대로 해도 됨 높이는 같으니까
        rank[B] += 1

def _find(A):
    
    if par[A] == A: # 만약에 스스로를 부모로 칭하고 있다면
        return A    # 그것이 바로 루트이다.
    else:
        par[A] = _find(par[A])
        return _find(par[A])
    

N, M = map(int, input().split())

rank = [0 for _ in range(N+1)]

par = [i for i in range(N+1)]
#[0,1,2,3,4,5,6,7]

for _ in range(M):
    X, A, B = map(int, input().split())

    if X == 0:
        _union(A, B)    # A와 B를 합해줌
    else:
        if _find(A) == _find(B):    #A와 B가 조상이 같다면
            print("YES")
        else:
            print("NO")

        
