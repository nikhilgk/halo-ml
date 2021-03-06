from os import listdir, curdir
from os.path import isfile, join
import pandas as pd
import numpy as np
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
columns='scale(0) id(1) desc_scale(2) num_prog(4) phantom(8) sam_mvir(9) mvir(10) rvir(11) \
rs(12) vrms(13) mmp?(14) scale_of_last_MM(15) vmax(16) x(17) y(18) z(19) vx(20) vy(21) vz(22)\
 Jx(23) Jy(24) Jz(25) Spin(26) Orig_halo_ID(30) Rs_Klypin(34) Mvir_all(35) M200b(36) M200c(37)\
  M500c(38) M2500c(39) Xoff(40) Voff(41) Spin_Bullock(42) b_to_a(43) c_to_a(44) A[x](45) A[y](46)\
   A[z](47) b_to_a(500c)(48) c_to_a(500c)(49) A[x](500c)(50) A[y](500c)(51) A[z](500c)(52) T/|U|(53) \
   M_pe_Behroozi(54) M_pe_Diemer(55) Macc(56) Mpeak(57) Vacc(58) Vpeak(59) Halfmass_Scale(60) \
   Acc_Rate_Inst(61) Acc_Rate_100Myr(62) Acc_Rate_1*Tdyn(63) Acc_Rate_2*Tdyn(64) Acc_Rate_Mpeak(65) \
   Mpeak_Scale(66) Acc_Scale(67) First_Acc_Scale(68) First_Acc_Mvir(69) First_Acc_Vmax(70) Vmax@Mpeak(71)'.split()

indexes=range(1,6)
indexes.extend(range(34,44))
remove_columns=[columns[index] for index in indexes]


for column in remove_columns:
	columns.remove(column)
for column in range(0,len(columns)):
	columns[column]=columns[column][:-4]
onlyfiles = [ f for f in listdir(curdir) if isfile(join(curdir,f)) and str(f)[-3:]=='txt']

values=[]
for file_name in onlyfiles:
	f=open(file_name,'r')
	timestep=f.read().replace(',','').split()
	timestep_list=[float(step) for step in timestep]
	portionstep=[float(step)/sum(timestep_list) for step in timestep]
	values.append(portionstep)

df = pd.DataFrame(np.array(values), index=range(0,len(onlyfiles)), columns=columns)
series=df.mean(axis=0)
series=series.order()

sorted_indexes=series.index[::-1][0:10]

# top_columns = []
# for index in sorted_indexes:
# 	if index not in ['x','y','z','vx','vy','vz','Jx','Jy','Jz']:
# 		top_columns.append(index)

# df_top = df[top_columns]
# df_top['rest'] = 1 - df_top.sum(axis=1,numeric_only=True,ignore_index=True) 
# print df_top
# print df_top.values

y = np.transpose(df.values)
x = np.arange(len(onlyfiles))

print y.shape

fig = plt.figure()
ax = fig.add_subplot(111)

ax.stackplot(x, y)
ax.set_title('100 % stacked area chart')
ax.set_ylabel('Percent (%)')
ax.margins(0, 0) # Set margins to avoid "whitespace"



plt.show()
# plt.savefig('plot.png')