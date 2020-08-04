import csv
import pandas 

id_rx = [-1,-1,-1,-1]
colnames = ['id', 'timestamp', 'x' , 'y' ,'radius', 'radius_x', 'radius_y','event']
data = pandas.read_csv('drawData_[32947473][normal erase].csv', names=colnames)
id = data.id.tolist()
timestamp = data.timestamp.tolist()
x = data.x.tolist()
y = data.y.tolist()
radius = data.radius.tolist()
radius_x = data.radius_x.tolist()
radius_y = data.radius_y.tolist()
event = data.event.tolist()
j = 0

for i in range(0,data.count().id - 1):
	
	if radius_x[i]==0:
		radius_x[i] = id_rx[id[i]]
	elif radius_x[i]!=0:
		id_rx[id[i]] = radius_x[i];
	if event[i]==0 and radius_x[i]>=4 and radius_x[i-1]<4:
		diff_x = abs(x[i-1] - x[i])
		diff_y = abs(y[i-1] - y[i])
		sq_dis = (diff_y**2 + diff_x**2)**(0.5)
		j = j+1
		fields=[diff_x, diff_y , radius[i] ,sq_dis ,'1']
		with open(r'draw_erase.csv', 'a') as f:
		    writer = csv.writer(f)
		    writer.writerow(fields)
		