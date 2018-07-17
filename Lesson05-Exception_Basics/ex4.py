class RelationException(Exception):
    def __init__(self, err_msg):
        self.msg = err_msg
    def __str__(self):
        return  self.msg

relation = {'Jason':'Mary', 'Mary':'Jason', 'Jennifer':'Ken', 'Ken':'Jennifer', 'Tina':'Kim', 'Kim':'Tina'}
def check(pa, pb):
    if relation[pa] != pb:
        raise RelationException("No relation found \n Are you sure that"+' '+ pa +' '+"and" +' '+pb +' '+"are in love with each other?")

try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    check(p1, p2)
    print("{} and {} are in love with each other!".format(p1, p2))
    
except RelationException as e:
    print(e)