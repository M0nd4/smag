import random 
import matplotlib.pyplot as plt
import numpy as np

def direct_disks_box(N, sigma):
    overlap = True
    while overlap == True:
        L = [(random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))]
        for k in range(1, N):
            a = (random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))
            min_dist_sq = min(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) for b in L) 
            if min_dist_sq < 4.0 * sigma ** 2: 
                overlap = True
                break
            else:
                overlap = False
                L.append(a)
    return L

def markov_disks_box(N, sigma,delta, n_steps):
    overlap = True 
    un = np.random.uniform
    L = np.zeros([N,2])
    L+= [1.0,1.0]
    while overlap == True:

        L = np.zeros([N,2])
        L+= np.array([un(sigma, 1.0 - sigma), un(sigma, 1.0 - sigma)])

        for k in range(1, N):
            newitem = L[k-1]+np.array([un(-delta, delta), un(-delta, delta)])
            #print("lets try",newitem)
            border = not((newitem>sigma).all() and (newitem<1.0-sigma).all())
            min_dist= np.min(np.sum((L[0:k,:]-newitem)**2,1))
            if (min_dist < 4.0 * sigma ** 2) or border : 
                overlap = True
                #print("fail")
                break
            else:
                L[k,:] = newitem
                overlap = False
                #print("success")
    return L
def markov_disks_box2(N, sigma,delta, n_steps):
    overlap = True 
    un = np.random.uniform
    ch = lambda:np.random.randint(0,4)
    choices = np.random.randint(0,4,n_steps)
    L = np.array([[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]])
    for step in range(n_steps): 
        a = L[choices[step]]
        b = a + [un(-delta,delta),un(-delta,delta)] 
        border = ((b>sigma).all() and (b<1.0-sigma).all())
        min_dist= np.min(np.sum((L-b)**2,1))
        if (min_dist > 4.0 * sigma ** 2) or border : 
            L[choices[step]] = b 
        # time
     
    return L



N = 4
sigma = 0.1197
n_runs = 1000000
n_steps = 0 
delta = 0.1
histo_data = np.zeros([n_runs,N,2]) 
for run in range(n_runs):
    histo_data[run,:,:] = direct_disks_box(N, sigma)
    #print(histo_data[run,:,:])
    if run%10000==0:
        print("%.3f%%"%(run/n_runs*100))
def hist_data():
    plt.figure()
    plt.hist((histo_data[:,:,0].flatten()), bins=100, normed=True)
    plt.xlabel(r'Position $x$')
    plt.ylabel(r'frequency')
    plt.title("Histogram of the x-Position with direct sampling")
    plt.grid()
    plt.show()
hist_data()
