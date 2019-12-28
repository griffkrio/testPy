
import random as r
import time
n = 20
while True:
    print(n*' '+'/\\')
    for i in range(1,n):
        s = ''.join(r.choice(['*','~',r.choice(['☣','•','☃','~'])]) for i in range(i*2))
        sl = r.choice(['/','☣'])
        sr = r.choice(['\\','•'])
        print((n-i)*' '+sl+s+sr)
    print((n-1)*' ' + '\'||\'')
    print(' '+n*2*'-')
    print('        ✐   Merry Christmas!')
    print('        ✐  SV@Camo.Kiev.Ua')
    time.sleep(1)