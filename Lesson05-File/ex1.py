f = open('note.txt', 'w+')
date = input('輸入日期:')
event = input('輸入事件:')
description = input('輸入心得:')
f.write('date:'+date+'\n')
f.write('event:'+event+'\n')
f.write('description:'+description+'\n')
print(f.read())
f.close()