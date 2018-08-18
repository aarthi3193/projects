#Em-624 Assignment 5
#AARTHI SHUNMUGAM -10411286



import matplotlib.pyplot as plt
import numpy as np

f = open("C:\\Users\\aarth\\Desktop\\EM624\\Marketing Data\\Marketing Data\\marketingdata.txt",'r')

parts = []

for rows in f:
    if "NA" not in rows:
        parts.append(rows.strip().split())
    else:
        pass
#print parts
#print(len(parts),len(parts[0]))

def get_index(parts):
    count_list =[]
    lower_income_men = 0
    lower_income_women = 0
    middle_income_men = 0
    middle_income_women = 0
    upper_income_men = 0
    upper_income_women = 0
    for i in range(len(parts)):
        if parts[i][1] == '1' and parts[i][0] in ('1','2','3'):
            lower_income_men = lower_income_men + 1

        elif parts[i][1] == '1'  and parts[i][0] in ('4','5','6'):
            middle_income_men = middle_income_men + 1

        elif  parts[i][1] == '1' and parts[i][0] >= '7':
            upper_income_men = upper_income_men + 1
        elif  parts[i][1] == '2' and parts[i][0] >= '7':
            upper_income_women = upper_income_women + 1
        elif  parts[i][1] == '2' and parts[i][0] in ('4','5','6'):
            middle_income_women = middle_income_women + 1
        elif  parts[i][1] == '2' and parts[i][0] in ('1','2','3'):
            lower_income_women = lower_income_women + 1
    return lower_income_men,middle_income_men,upper_income_men,lower_income_women,middle_income_women,upper_income_women
    
print (get_index(parts))

a=plt.figure(1)

labels = 'lower_income_men','middle_income_men','upper_income_men','lower_income_women','middle_income_women','upper_income_women'
sizes = [939, 925, 1203, 1350, 1066, 1393]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','blue','red']
explode = (0.1, 0.1,0.1,0, 0, 0) 
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
a.show()

b= plt.figure(2)
objects = ('lower_income_men','middle_income_men','upper_income_men','lower_income_women','middle_income_women','upper_income_women')
y_pos = np.arange(len(objects))
performance = [200,400,600,800,1000,1200]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Income')
plt.title('Income by Gender')
f.show()

