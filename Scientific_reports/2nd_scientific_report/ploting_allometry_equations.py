#plotting graphs - 2nd scientific reports

import math as m
import random
import matplotlib.pyplot as plt  # Modulo para fazer gráficos


#1st: wood density + stem vs. diameter

#####generating random values for dw (g/cm3)---> 
# list of random float between a range 0.1 to 1.21
wood_density = []
diameter = []
stem = []
leaves = []
SLA = []

# Set a length of the list to 200 for wood density (kg/m3)
for i in range(0, 200):
    # any random float - reference: Fearnside 1997
    # don't use round() if you need number as it is
    x = round(random.uniform(140.,1210.),2)
    wood_density.append(x)

# print(len(wood_density))

 # Set a length of the list to 200 for stem (kgC/m2)
for i in range(0, 200):
     stm = round(random.uniform(8.,30.),2)
     stem.append(stm)

 # Set a length of the list to 200 for leaves (kgC/m2)
for i in range(0, 200):
     lvs = round(random.uniform(0.1,1.5),2)
     leaves.append(lvs)

 # Set a length of the list to 200 for SLA (m2/kg)
for i in range(0, 200):
     spec_leaf = round(random.uniform(4.,28.),2)
     SLA.append(spec_leaf)


# #calculating diameter (m), stm in kgc/m2 and wd in KgC/m3 para que o diam dê em m
for wd in wood_density:
 	 # for stm in stem:
    diam =((4*25.)/(wd*3.14*40.))**(1./(2.+0.5))
       
    diameter.append(diam)




# plt.scatter(wood_density,diameter)	
# plt.xlabel('wood density')
# plt.ylabel('diameter')
# plt.show()

# print(len(diameter))
#print(diameter)
# print(stem)

##2nd: diameter vs. crown area
crown_area=[]
for diam in diameter:
	k_allom1=100.
	krp=1.6
	crn_area = k_allom1*(diam**krp)
	crown_area.append(crn_area)


# # #print(crown_area)
# plt.scatter(diameter,crown_area)
# plt.xlabel('diameter')
# plt.ylabel('crown area')
# plt.show()



# #3rd: height vs. diameter
height = []
for diam in diameter:
	k_allom2=36.
	k_allom3=0.22

	hg=k_allom2*(diam**k_allom3)
	height.append(hg)

# # print(height)

# plt.plot(diameter,height)
# plt.xlabel('diameter')
# plt.ylabel('height')
# plt.show()

plt.scatter(wood_density,height)
plt.xlabel('wood density')
plt.ylabel('height')
plt.show()

# #4th LAI vs crown area


# LAI_1=[]
# # for lvs in leaves:
# # 	for crn_area in crown_area:
# for spec_leaf in SLA:
# #	print('for 1')
# 	for lvs in leaves:
# #		print('for 2')
# 		fst_lai=lvs*spec_leaf
# 		LAI_1.append(fst_lai)

# LAI=[]
# for fst_lai in LAI_1:
# 	print('for 1b')
# 	for crn_area in crown_area:
# 		print('for2b')
# 		scnd_lai=fst_lai/crn_area
# 		LAI.append(scnd_lai)

# # print(LAI)

# plt.scatter(SLA,LAI)

# plt.xlabel('SLA')
# plt.ylabel('LAI')
# plt.show()

