#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd
from pandas import DataFrame


# In[ ]:


#set initial conditions

k_initial = 100
n = 0
k_elong = 6000
k_deg = 2
L = 5300


tend = 10


three_prime_end = [0]
five_prime_end = [0]
rna_count = []
z = []
t = [0]
mature_rna = 0
mature_rna_count = []


# In[ ]:


get_ipython().run_line_magic('time', '')
#model

while t[-1] < tend:
    
    rates = [k_initial, n*k_elong, n*k_deg]
    rate_sum = sum(rates)
    
    tau = np.random.exponential(scale = 1/rate_sum)
    
    t.append(t[-1] + tau)
    rna_count.append(n)
    
    rand = random.uniform(0,1)
    
    l = n
    res = True in (ele >= l for ele in three_prime_end)
    
    #initiation rate
    if rand * rate_sum > 0 and rand * rate_sum < rates[0]:
        if res == True:
            n += 1
            z.append(1) #new mRNA entry
        else:
            pass
    
    #elongation
    elif rand * rate_sum > rates[0] and rand * rate_sum < rates[0] + rates[1]:
        
        z_index = np.random.randint(0, len(z)) #select mRNA
        
        index = len(three_prime_end)
        for i in range(index, len(z)):
            three_prime_end.append(0)#add initial 3' ends in accordance with z
            five_prime_end.append(0) #add initial corresponding 5' ends
            i +=1
            
        if three_prime_end[z_index] < L:
            three_prime_end[z_index] += 1 #grow selected mRNA by 1
        else:
            mature_rna += 1
            mature_rna_count.append(mature_rna)
            three_prime_end[z_index] = max(three_prime_end)
        
        
        
        
        
    else:
        z_index = np.random.randint(0, len(z)) #select mRNA
        
        index = len(three_prime_end)
        for i in range(index,len(z)):
            three_prime_end.append(0)#add initial 3' ends in accordance with z
            five_prime_end.append(0) #add initial corresponding 5' ends
            i +=1
            
        if three_prime_end[-1] >= five_prime_end[-1]:
            
            five_prime_end[z_index] += 1 #degrade selected mRNA by 1 
            n -= 1

            
            
        else:
            pass
        

