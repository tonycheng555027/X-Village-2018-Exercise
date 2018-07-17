class Map:   
    def __init__(self,n,p):
        self.n=n
        self.p=p
        self.list = []
        for j in range(self.n):
            for i in range(self.n):
                self.list.append('*')   ## 使用 append() 添加元素
                i+=1
            j+=1
        ii=((self.n-1)/2)-1
        a=int(self.n*ii+ii)
        b=int(a+1)
        c=int(b+1)
        d=int(c+1+2*ii)
        e=int(c+2+2*ii+3+2*ii)
        if self.p==1:
           self.list[a]=0 
           self.list[b]=0 
           self.list[c]=0 
           self.list[d]=0 
           self.list[e]=0 
        #return self.list
    def display(self): 
        n=self.n
        i=1
        j=1
        k=0
        for i in range(n+1):
            for j in range(n+1):
                if k<=n*i-1:
                    print(self.list[k],end='')
                    k+=1
                j+=1
            print('')
            i+=1

x=Map(7,1)
x.display()