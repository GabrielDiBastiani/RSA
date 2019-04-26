#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import math


# In[2]:


def is_Prime(n):
    '''
    Teste de primalidade de Miller Rabin.
 
    Caso retorne 'False' significa que 'n' certamente não é primo. Caso retorne um valor
    'Tru'e significa que é muito provavel que 'n' seja primo.
    '''
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
 
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(1000):#número de tentativas 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False 
    return True


# In[3]:


'''
Define um valor de 512 bits para 'p' e verifica se este valor é primo,
caso não seja o processo é repetido
'''
while True:
    p = random.getrandbits(512)#Quantidade de bits da chave
    if is_Prime(p) == True:
        break
'''
Define um valor de 512 bits para 'q' e verifica se este valor é primo,
caso não seja o processo é repetido
'''
while True:
    q = random.getrandbits(512)#Quantidade de bits da chave
    if is_Prime(q) == True:
        break
        
print('q =',q) 
print('\np =',p)  


# In[4]:


'''Calcula n'''
n = p*q
'''Calcula a função totiente(phi_n)'''
phi_n = (p-1)*(q-1)

print('n =',n) 
print('\nphi_n =',phi_n) 


# In[5]:


'''Escolhe 1 < e < phi_n, tal que 'e' e 'phi_n' sejam primos entre si'''
while True:
    e = random.randrange(1, phi_n-1)
    '''
    Caso gcd(greatest common divisor(maior divisor comum)) entre 'e' e 'phi_n' for igual a 1
    significa que eles são primos entre si
    '''
    if (math.gcd(e,phi_n) == 1):
        break
        
print('e = ',e)


# In[8]:


'''Calcula xgcd(extended greatest common divisor)'''
def xgcd(a, b):
    '''retorna (gcd, x, y) tal que a*x + b*y = gcd(a, b)'''
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, y0, x0


# In[21]:


'''Descobre o valor de d tal que (e * d) % phi_n == 1'''
gcd, x, _ = xgcd(e,phi_n)
d = x % phi_n
print('d = ',d)


# In[24]:


def criptografar(txt, e, n):
    txt_dec = []
    txt_cripto = []
    
    '''
    Transforma cada letra do texto a ser criptografado 
    em um número decimal equivalente a sua posição alfabética
    '''
    for letra in txt:
        letra_dec = ord(letra)
        txt_dec.append(letra_dec)
    
    '''
    Criptografa o texto através da fórmula letra_dec ^ e % n
    '''
    for i in range(len(txt)):        
        txt_cripto.append(str(pow(txt_dec[i],e,n)))
        
    txt_cripto = ' '.join(txt_cripto)    
    return txt_cripto


# In[25]:


def decriptografar(txt, e, n):
    txt_decripto = []
    
    '''
    Verifica se a entrada txt esta em formato de lista ou formato de string
    '''
    if type(txt) == list:
        '''
        Decriptografa o texto através da fórmula txt ^ d % n
        '''
        for i in range(len(txt)):
            txt_decripto.append(chr(pow(int(txt[i]),e,n)))
        txt_decripto = ''.join(txt_decripto)
        return txt_decripto
    else:
        txt = txt.split()
        '''
        Decriptografa o texto através da fórmula txt ^ d % n
        '''
        for i in range(len(txt)):
            txt_decripto.append(chr(pow(int(txt[i]),e,n)))
        txt_decripto = ''.join(txt_decripto)
        return txt_decripto


# ### The information security is of significant importance to ensure the privacy of communications

# In[15]:


txt = input('Digite a mensagem para ser criptografada: ')


# In[16]:


txt_cripto = criptografar(txt,e,n)
print('Mensagem criptografada:',txt_cripto)


# In[17]:


txt_cripto = input('Digite a mensagem para ser decriptografada: ')


# In[19]:


txt_decripto = decriptografar(txt_cripto,d,n)
print('Mensagem decriptografada:',txt_decripto)

