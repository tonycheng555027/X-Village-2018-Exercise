def eight_queens(cor):
    a=0
    aa=0
    for i in range(0,2,1):
        for  j in range(0,7,1):
            for  k in range(j+1,8,1):
                if cor[j][i]==cor[k][i]:
                    a+=1
                else:
                    pass
    if a != 0:
        print('False')
    else:
        for  jj in range(0,7,1):
            for  kk in range(jj+1,8,1):
                if (cor[jj][0]-cor[kk][0])==(cor[jj][1]-cor[kk][1]) or (cor[jj][0]-cor[kk][0])==-1*(cor[jj][1]-cor[kk][1]):
                    aa+=1
                else:
                    pass
        if aa!=0:
            print('False')
        else:
            print('True')

eight_queens([[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]])