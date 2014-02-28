import matplotlib.pyplot as plt

def show_conf(L, sigma, title, fname):
    plt.figure()
    plt.axes()
    for [x, y] in L:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                cir = plt.Circle((x + ix, y + iy), radius = sigma,  fc = 'r')
                plt.gca().add_patch(cir)
    plt.axis('scaled')
    plt.title(title)
    plt.axis([0.0, 1.0, 0.0, 1.0])
    #plt.savefig(fname)
    plt.show()

L = [[0.95, 0.95]]
sigma = 0.1
show_conf(L, sigma, 'test graph', 'one_disk.png')
