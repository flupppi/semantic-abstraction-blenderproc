'''
Created on 11.01.2021

@author: Felix Kalchschmid
'''

# Sie mit der Eingabe x= ((4,2,7,1),(3,1,2,3),9,5)und verschiedenen Lösungen

def V_ks(s,v,S,k,t):   
    size = 0
    value = 0
   
    for i in range(0,len(s)):
        if t[i] ==1:
            size += s[i]
            value += v[i]
    if(size <= S and value >= k):
        return True
    else:
        return False
   
s = [4,2,7,1]
v = [3,1,2,3]
S = 9
k = 5
t = [0,1,1,0]

print(V_ks(s,v,S,k,t))


a = [8,2,2,1,5]
k = 9

t = [1,0,0,1,0]
V_ks(a,k,t)

t = [0,1,1,1,0]
V_ks(a,k,t)

