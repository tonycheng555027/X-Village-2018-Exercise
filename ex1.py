class Shape:
    def set_edge(self,edge):
        self.i=edge
        return self.i
    def display(self):
        i=1
        j=1
        k=self.i
        while i <=k:
            while j <=i:  
                print('*',end='')
                j+=1
            print('')
            j=1
            i+=1
x=Shape()
print(x.set_edge(5))
x.display()