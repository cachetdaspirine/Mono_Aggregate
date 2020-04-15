#!/home/hugo/anaconda3/bin/python3

from Anneal import *
import os

time_start = time.perf_counter()

SerieNum=9

os.system('rm -rf Res/Serie'+str(SerieNum))
os.system('mkdir Res/Serie'+str(SerieNum))

Kmain=1.
Kcoupling=0.1
Eps=0.1
KVOL=8.
J=1.
Npmax=50
Npmin=3
TimeStepTot=2*10**3
seed=98230

with open('Res/Serie'+str(SerieNum)+'/Energy.out', 'w') as myfile:
    myfile.write('Number_of_particle Energy Final_Acceptance_rate\n')

for N in range(Npmin,Npmax+1):
    Energy,Statfinal=Annealing(Kmain=Kmain,
                               Kcoupling=Kcoupling,
                               Eps=Eps,
                               KVOL=KVOL,
                               J=J,
                               SizeX=2*N+10,
                               SizeY=2*N+10,
                               NumberOfParticle=N,
                               SimNum=N,
                               Path='Res/Serie'+str(SerieNum)+'/',
                               TimeStepTot=TimeStepTot,
                               Seed=seed)
    with open('Res/Serie'+str(SerieNum)+'/Energy.out', 'a') as myfile:
        myfile.write(str(N)+' '+str(Energy)+' '+str(Statfinal)+'\n')
