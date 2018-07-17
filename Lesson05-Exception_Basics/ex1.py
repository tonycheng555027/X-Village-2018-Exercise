codr='''
def div(dividend, divisor):
    print("The answer is {}".format(dividend/divisor))

for i in range(5, -1, -1):
    for j in range(5, -1, -1):
        div(i, j)
        '''
error_message='''
Traceback (most recent call last):
  File "ex1.py", line 7, in <module>
    div(i, j)
  File "ex1.py", line 3, in div
    print("The answer is {}".format(dividend/divisor))
ZeroDivisionError: division by zero'
'''
answer="從下面找，一開始在div(i,j)發生錯誤，而div是一個函式，往上找到即會發現是因為除數不能為0，故發生錯誤，\n錯誤訊息除了原因還說明了錯誤在哪個檔案、哪一行發生錯誤"
print(answer)