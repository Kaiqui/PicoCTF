import random
flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽'

pico = []
for i in range(len(flag)):
        pico.append(str(chr(ord(flag[i])>>8)))
        pico.append(str(chr((ord(flag[i]))-((ord(flag[i])>>8)<<8))))
        #pico.append(str(i))

print(''.join(pico))