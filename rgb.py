import math
import matplotlib.pyplot as plt
from matplotlib import animation

frps=30
sec=3*60

fig, a=plt.subplots()

omegaM=2*math.pi/687
omegaE=2*math.pi/365
r=12
rE=3
rM=4
rcs=r-rE

xl=rM
yl=0
def run(frame):
	global xl,yl
	plt.clf()
	xE=rE*math.cos(omegaE*frame)
	yE=rE*math.sin(omegaE*frame)
	xM=rM*math.cos(omegaM*frame)
	yM=rM*math.sin(omegaM*frame)
	dx=xM-xE
	dy=yM-yE
	mag=math.sqrt(dx**2+dy**2)
	ct=dx/mag
	st=dy/mag
	dEx=rcs*ct
	dEy=rcs*st
	x=xE+dEx
	y=yE+dEy
	dxl=dEx-xl
	dyl=dEy-yl
	xl=dEx
	yl=dEy
	plt.arrow(xE,yE,dEx,dEy,head_width=0.4,length_includes_head=True,color='g')
	circle=plt.Circle((0,0),radius=0.4,fc='y')
	plt.gca().add_patch(circle)
	circle=plt.Circle((xE,yE),radius=0.2,fc='b')
	plt.gca().add_patch(circle)
	circle=plt.Circle((xE,yE),fill=False,radius=rcs,ec='g')
	plt.gca().add_patch(circle)
	circle=plt.Circle((xM,yM),radius=0.15,fc='r')
	plt.gca().add_patch(circle)
	plt.arrow(x,y,5*dxl,5*dyl,head_width=0.2,color='w')
	circle=plt.Circle((x,y),radius=0.15,fc='r')
	plt.gca().add_patch(circle)
	ax=plt.gca()
	ax.set_aspect(1)
	plt.xlim([-(r+1),r+1])
	plt.ylim([-(r+1),r+1])
	ax.set_facecolor('xkcd:black')	

ani=animation.FuncAnimation(fig,run,frames=frps*sec)
#writervideo=animation.FFMpegWriter(fps=frps)
#ani.save('rgb.mp4', writer=writervideo)
plt.show()

