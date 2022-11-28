# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
import math


t = np.linspace(0,200,400);
plt.subplot(3,1,1)
plt.plot(t,0.005*(math.sin(math.sin(0.2*t))-0.2*math.sin(t)),'k-')
plt.xlabel('t (s)','fontsize',14)
plt.ylabel('x (t)','fontsize',14)
set(gca,'fontsize',14)
plt.subplot(3,1,2)
t = np.linspace(0,200,400);
plt.plot(t,0.0025*math.sin(t)-t*math.cos(t),'k-')
plt.xlabel('t (s)','fontsize',14)
plt.ylabel('x (t)','fontsize',14)
set(gca,'fontsize',14)
plt.subplot(3,1,3)
t = np.linspace(0,50,400);
plt.plot(t,-0.0017*math.sin(math.sin(2*t)-2*math.sin(t)),'k-')
plt.xlabel('t (s)','fontsize',14)
plt.ylabel('x (t)','fontsize',14)
set(gca,'fontsize',14)
