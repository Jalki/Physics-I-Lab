#!/usr/bin/env python
# coding: utf-8

# In[50]:


#Physics Lab 1
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')
#Credit to rundergradengineers.com for the code!

#Tester One Mean and Sigma
T_1mu = 250 
T_1sigma = 32.2773
#Tester Two Mean and Sigma
T_2mu = 212
T_2sigma = 30.2738
#Upperbounds
x1 = 190
x2 = 300
#Calculate the z-transform
T_1z1 = ( x1 - T_1mu) / T_1sigma
T_1z2 = ( x2 - T_1mu) / T_1sigma
T_2z1 = ( x1 - T_2mu) / T_2sigma
T_2z2 = ( x2 - T_2mu) / T_2sigma
#Ha
x = np.arange(x1, x2, 0.001)
x_all = np.arange(T_1z1,T_2z2,0.001)
y= norm.pdf(x,0,1)
y2 = norm.pdf(x_all,0,1)
#Build the plot
fig, ax = plt.subplots(figsize=(9,6))
plt.style.use('fivethirtyeight')
ax.plot(x_all, y2)

ax.fill_between(T_1z1,y2,0, alpha=.5, color='b')
ax.fill_between(x_all, y2, 0, alpha =.5, color="g")
ax.set_xlim([-1.5,1.5])
ax.set_xlabel('# of Standard Deviation Outside the Mean')
ax.set_yticklabels([0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1])
ax.set_title('Normal Gaussian Curve')
plt.savefig('normal_curve.png', dpi=72, bbox_inches="tight")
plt.show()


# In[ ]:




