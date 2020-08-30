import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation 
%matplotlib notebook

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)


def func(curr):
    if curr == 901:
        a.event_source.stop()
    
    ax1=plt.subplot(221)
    plt.cla()
    plt.hist(x1[100:100+curr],facecolor = 'b',normed =True,alpha =0.5,bins =20)
    plt.title('Normal Distribution',fontsize='medium')
    
    
    ax2=plt.subplot(222,sharey=ax1)
    ax2.yaxis.tick_right()
    plt.cla()
    plt.hist(x2[100:100+curr],facecolor = 'y',bins = 20,normed =True)
    plt.title('Gamma Distribution',fontsize='medium')

    ax3=plt.subplot(223,sharey=ax1)
    plt.cla()
    plt.hist(x3[100:100+curr],facecolor ='g',alpha =0.5,bins = 20,normed =True,)
    plt.xlabel('Exponential Distribution')

    ax4=plt.subplot(224,sharey=ax1)
    ax4.yaxis.tick_right()
    plt.cla()
    plt.hist(x4[100:100+curr],facecolor = 'r',alpha = 0.5, bins = 20,normed =True)
    plt.xlabel('Uniform Distribution')


fig=plt.figure()
a=animation.FuncAnimation(fig, func, interval = 5)
    