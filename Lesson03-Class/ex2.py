class Map:   
    def set_map(self,n):
        self.n=n
        self.list = []
        for j in range(n):
            for i in range(n):
                self.list.append('*')   ## 使用 append() 添加元素
                i+=1
            j+=1
        return self.list
    def set_pattern(self,p):
        self.p=p
        i=((self.n-1)/2)-1
        n=self.n
        a=int(n*i+i)
        b=int(a+1)
        c=int(b+1)
        d=int(c+1+2*i)
        e=int(c+2+2*i+3+2*i)
        if self.p==1:
           self.list[a]=0 
           self.list[b]=0 
           self.list[c]=0 
           self.list[d]=0 
           self.list[e]=0 
        return self.list
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

x=Map()
print(x.set_map(3))
x.set_pattern(1)
x.display()