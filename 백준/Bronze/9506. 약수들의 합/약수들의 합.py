import math as M

while True:
    n = int(input())
    if n == -1:
        break
    st = []

    for i in range(1, int(M.sqrt(n)) + 1):  
        if n % i == 0:
            st.append(i)
            if i != n // i and i != 1: 
                st.append(n // i)
    
    st.sort()  

    if n in st:
        st.remove(n)  

    # 완전수 여부 확인
    if n == sum(st) and n != 1:
        print(f"{n} = {' + '.join(map(str, st))}") 
    else:
        print(f"{n} is NOT perfect.")  
