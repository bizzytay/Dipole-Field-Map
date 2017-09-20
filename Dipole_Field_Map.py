from Dipole_Field_Point import *

xnum = 128
ynum = 128
znum = 2#3

xpixel = x_length/(xnum -1)
ypixel = y_length/(ynum -1)
zpixel = z_length/(znum -1)

# position of the dipole
xdipole = x_length/2
ydipole = y_length/2
zdipole = d + z_length/2

xrel = []
yrel = []
zrel = []
xspace = []
yspace = []
zspace = []

#calculates the space and reletive positions
def space_rel(num,dipole,space,rel,pixel):
    for i in range(num):
        space.append(pixel * i)
        rel.append(space[i] - dipole)

space_rel(xnum,xdipole,xspace,xrel,xpixel)
space_rel(ynum,ydipole,yspace,yrel,ypixel)
space_rel(znum,zdipole,zspace,zrel,zpixel)

#Instance of B field
BF = B_Field()


xstart = xrel[0]
ystart = yrel[0]
xend = xrel[xnum - 1]
yend = yrel[ynum - 1]
dx = xrel[1] - xrel[0]
dy = yrel[1] - yrel[0]
yrelmat, xrelmat = np.mgrid[slice(ystart, yend + dy, dy),slice(xstart, xend + dx, dx)]
xrelmat = xrelmat[:, :]
xrelmat = xrelmat/1.0e-4
yrelmat = yrelmat[:, :]
yrelmat = yrelmat/1.0e-4
#print "dx=",dx, "yx=", dy, "yrelmat" , yrelmat, "xrelmat", xrelmat


Bxmap, Bymap, Bzmap = BF.Map(xnum,ynum,znum,xrel,yrel,zrel)
#pprint.pprint(Bxmap)


BxImage = [[0 for j in xrange(ynum)] for i in xrange(xnum)]
ByImage = [[0 for j in xrange(ynum)] for i in xrange(xnum)]
BzImage = [[0 for j in xrange(ynum)] for i in xrange(xnum)]

for i in range(xnum):
    for j in range(ynum):
        for k in range(znum):
            BxImage[i][j] = Bxmap[i][j][k]
            ByImage[i][j] = Bymap[i][j][k]
            BzImage[i][j] = Bzmap[i][j][k]


BxImage = np.array(BxImage)
BxImage.resize(ynum,xnum)

ByImage = np.array(ByImage)
ByImage.resize(ynum,xnum)

BzImage = np.array(BzImage)
BzImage.resize(ynum,xnum)


print "Length", BxImage.shape

Xz_min,Xz_max= -np.abs(BxImage).max(), np.abs(BxImage).max()
Yz_min,Yz_max= -np.abs(ByImage).max(), np.abs(ByImage).max()
Zz_min,Zz_max= -np.abs(BzImage).max(), np.abs(BzImage).max()

#Xz_min,Xz_max= -1240.55, 1240.55
#Yz_min,Yz_max= -1240.55, 1240.55
#Zz_min,Zz_max= -2881.59, 2881.59

print Xz_min, Xz_max, Yz_min, Yz_max, Zz_min, Zz_max
'''
def fmt(x, pos):
    a, b = '{:.2e}'.format(x).split('e')
    b = int(b)
    return r'${} \times 10^{{{}}}$'.format(a, b)
'''
#Create the images of Bx,By, and Bz
def pic(Image,Min,Max):
    plt.pcolor(xrelmat, yrelmat, Image, cmap=cm.coolwarm, vmin=Min, vmax=Max)
    #plt.title(Title,fontsize=15)
    #plt.xlabel("X(um)",fontsize=10)
    #plt.ylabel("Y(um)",fontsize=10)
    plt.axis([xrelmat.min(), xrelmat.max(), yrelmat.min(), yrelmat.max()])
    plt.xticks([])
    plt.yticks([])

    #plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
    #cbar = plt.colorbar(format=ticker.FuncFormatter(fmt))
    #cbar.ax.set_ylabel("Gaus(G)",rotation=270)

def quiver(Image,Min,Max):
    plt.title('Quiver')
    Q = plt.quiver(xrelmat, yrelmat, Image, cmap=cm.coolwarm)
#    plt.axis([xrelmat.min(), xrelmat.max(), yrelmat.min(), yrelmat.max()])

'''
#For display purposes and layout
plt.subplot(3,2,1)
imq = quiver(BxImage,Xz_min,Xz_max)
plt.subplot(3,2,2)
imq = quiver(ByImage,Xz_min,Xz_max)
plt.subplot(3,2,3)
imq = quiver(BzImage,Xz_min,Xz_max)
plt.show()

'''

plt.subplot(2, 3, 1)
im1 = pic(BxImage,Xz_min,Xz_max)
plt.subplot(2, 3, 2)
im2 = pic(ByImage,Yz_min,Yz_max)
#Zz_max = 2000
#Zz_min = -2000
plt.subplot(2, 3, 3)
im3 = pic(BzImage,Zz_min,Zz_max)

#cbaxes = fig.add_axes([0.8, 0.1, 0.03, 0.8])

#cbar = plt.colorbar(orientation="horizontal")
#plt.tight_layout()
plt.show()

#    y, x = np.mgrid[slice(-3, 3 + dy, dy),slice(-3, 3 + dx, dx)]]
#    BxImage = Bxmap[:][:][k]
#    z_min, z_max = -np.abs(BxImage).max(), np.abs(BxImage).max()
#    plt.pcolor(x, y, BxImage, cmap='RdBu', vmin=z_min, vmax=z_max)
#    plt.title('pcolor')
#    # set the limits of the plot to the limits of the data
#    plt.axis([xrel.min(), xrel.max(), yrel.min(), yrel.max()])
#    plt.colorbar()
