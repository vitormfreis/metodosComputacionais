import numpy

print("Esse programa simula o aquecimento das faces de um cubo e como a temperatura ira se comportar ao longo deste corpo.")

#Parametros da simulacao ***ESCOLHA DO USUARIO***
dT = 0              #Valor da derivada da borda. Quando face esta isolada dT=0
f_relax = 1.5       #Fator de relaxacao do metodo de liebmann
tol_des = 0.01      #Tolerancia desejada para o erro
faceCCderiv = 6    # 0-Nenhuma face/1-Face Superior/2-Face Inferior/3-Frontal/4-Traseira/5-Esquerda/6-Direita

faceCCderiv = int(input("Escolha a face que deve ser isolada (0-Nenhuma face/1-Face Superior/2-Face Inferior/3-Frontal/4-Traseira/5-Esquerda/6-Direita): "))
dT = float(input("Defina o valor da derivada da face isolada: "))

LS = int(input("Escolha o limite superior para os 3 eixos: "))
LI = int(input("Escolha o limite inferior para os 3 eixos: "))

#Intervalos em X, Y e Z -- ***ESCOLHA DO USUARIO***
LS_X = LS        #Limite Superior em X
LI_X = LI        #Limite Inferior em X
LS_Y = LS        #Limite Superior em Y
LI_Y = LI        #Limite Inferior em Y
LS_Z = LS        #Limite Superior em Z
LI_Z = LI        #Limite Inferior em Z
 
#Passo em X, Y e Z-- ***ESCOLHA DO USUARIO*** OS PASSOS DEVEM SER IGUAL PELO METODO DE LIEBMANN
dx=1
dy=1
dz=1

dx = int(input("Escolha o passo em relacao ao eixo 'x': "))
dy = int(input("Escolha o passo em relacao ao eixo 'y': "))
dz = int(input("Escolha o passo em relacao ao eixo 'z': "))

#Declaracao das temperaturas nas faces ***ESCOLHA DO USUARIO***
Tf = 1 #Face Frontal
Tt = 2 #Face Traseira
Ts = 3 #Face Superior
Ti = 4 #Face Inferior
Te = 5 #Face Esquerda
Td = 6 #Face Direita

Tf = int(input("Escolha a temperatura para a Face Frontal: "))
Tt = int(input("Escolha a temperatura para a Face Traseira: "))
Ts = int(input("Escolha a temperatura para a Face Superior: "))
Ti = int(input("Escolha a temperatura para a Face Inferior: "))
Te = int(input("Escolha a temperatura para a Face Esquerda: "))
Td = int(input("Escolha a temperatura para a Face Direita: "))

# Definindo intervalos para o loop
#Somando com o passo para a funcao range incluir o ultimo elemento
x = range(LI_X,LS_X+dx,dx)
Nx = len(x)
y = range(LI_Y,LS_Y+dy,dy)
Ny = len(y)
z = range(LI_Z,LS_Z+dz,dz)
Nz = len(z)

# Declaracao dos vetores
T = numpy.zeros((Nz,Ny,Nz))
erro = numpy.zeros((Nz,Ny,Nz))

#Preenchendo valores das bordas, faces e quinas
T[0,0,0] = (Tf+Ts+Te)/3     #Quina (0,0,0) - Frontal Superior Esquerda
T[0,0,Nx-1] = (Tf+Ts+Td)/3    #Quina (0,0,Nx) - Frontal Superior Direita
T[0,Ny-1,0] = (Tf+Ti+Te)/3    #Quina (0,Ny,0) - Frontal Inferior Esquerda
T[0,Ny-1,Nx-1] = (Tf+Ti+Td)/3   #Quina (0,Ny,Nx) - Frontal Inferior Direita
T[Nz-1,0,0] = (Tt+Ts+Te)/3    #Quina (Nz,0,0) - Traseira Superior Esquerda
T[Nz-1,0,Nx-1]= (Tt+Ts+Td)/3    #Quina (Nz,0,Nx) - Traseira Superior Direita
T[Nz-1,Ny-1,0] = (Tt+Ti+Te)/3   #Quina (Nz,Ny,0) - Traseira Inferior Esquerda
T[Nz-1,Ny-1,Nx-1] = (Tt+Ti+Td)/3  #Quina (Nz,Ny,Nx) - Traseira Inferior Direita

T[0,1:Ny-1,0] = (Tf+Te)/2     #Borda Frontal Esquerda
T[0,1:Ny-1,Nx-1] = (Tf+Td)/2    #Borda Frontal Direita
T[0,0,1:Nx-1] = (Tf+Ts)/2     #Borda Frontal Superior
T[0,Ny-1,1:Nx-1] = (Tf+Ti)/2    #Borda Frontal Inferior
T[Nz-1,1:Ny-1,0] = (Tt+Te)/2    #Borda Traseira Esquerda
T[Nz-1,1:Ny-1,Nx-1] = (Tt+Td)/2   #Borda Traseira Direita
T[Nz-1,0,1:Nx-1] = (Tt+Ts)/2    #Borda Traseira Superior
T[Nz-1,Ny-1,1:Nx-1] = (Tt+Ti)/2   #Borda Traseira Inferior
T[1:Nz-1,0,0] = (Ts+Te)/2     #Borda Meio Superior Esquerda
T[1:Nz-1,0,Nx-1] = (Ts+Td)/2    #Borda Meio Superior Direita
T[1:Nz-1,Ny-1,0] = (Ti+Te)/2    #Borda Meio Inferior Esquerda
T[1:Nz-1,Ny-1,Nx-1] = (Ti+Td)/2   #Borda Meio Inferior Direita

T[0,1:Ny-1,1:Nx-1] = Tf         #Face Frontal
T[Nz-1,1:Ny-1,1:Nx-1] = Tt        #Face Traseira
T[1:Nz-1,0,1:Nx-1] = Ts         #Face Superior
T[1:Nz-1,Ny-1,1:Nx-1] = Ti        #Face Inferior
T[1:Nz-1,1:Ny-1,0] = Te         #Face Esquerda
T[1:Nz-1,1:Ny-1,Nx-1] = Td        #Face Direita

interacoes = 0
Tvelho=0
tol_enc = 1

#Parametrizando os valores para loop de acordo com face com cond Contor na derivada
ini_X = 9999
ini_Y = 9999
ini_Z = 9999
fim_X = 9999
fim_Y = 9999
fim_Z = 9999

if faceCCderiv==1:      #Borda Superior
    ini_X = 1
    ini_Y = 0
    ini_Z = 1
    fim_X = Nx-1
    fim_Y = Ny-1
    fim_Z = Nz-1
elif faceCCderiv==2:    #Borda Inferior
    ini_X = 1
    ini_Y = 1
    ini_Z = 1
    fim_X = Nx-1
    fim_Y = Ny
    fim_Z = Nz-1
elif faceCCderiv==3:    #Borda Frontal
    ini_X = 1
    ini_Y = 1
    ini_Z = 0
    fim_X = Nx-1
    fim_Y = Ny-1
    fim_Z = Nz-1
elif faceCCderiv==4:    #Borda Traseira
    ini_X = 1
    ini_Y = 1
    ini_Z = 1
    fim_X = Nx-1
    fim_Y = Ny-1
    fim_Z = Nz
elif faceCCderiv==5:    #Borda Esquerda
    ini_X = 0
    ini_Y = 1
    ini_Z = 1
    fim_X = Nx-1
    fim_Y = Ny-1
    fim_Z = Nz-1
elif faceCCderiv==6:    #Borda Direita
    ini_X = 1
    ini_Y = 1
    ini_Z = 1
    fim_X = Nx
    fim_Y = Ny-1
    fim_Z = Nz-1
elif faceCCderiv==0:    #Nenhuma Borda
    ini_X = 1
    ini_Y = 1
    ini_Z = 1
    fim_X = Nx-1
    fim_Y = Ny-1
    fim_Z = Nz-1
    
#Enquanto o erro encontrado for maior que o erro desejado
while(tol_enc>tol_des):
    for i in range(ini_X,fim_X,1):
        for j in range(ini_Y,fim_Y,1):
            for k in range(ini_Z,fim_Z,1):

                Tvelho = T[k,j,i]                    
                if (faceCCderiv==1) and (j==0):         #Face Superior CC na Derivada: T[k,j-1,i] = T[k,j+1,i]-2*dy*dT
                    Tnovo = (T[k+1,j,i]+T[k-1,j,i]+T[k,j+1,i]+(T[k,j+1,i]-2*dy*dT)+T[k,j,i+1]+T[k,j,i-1])/6

                elif (faceCCderiv==2) and (j==Ny-1):    #Face Inferior CC na Derivada: T[k,j+1,i] = T[k,j-1,i]-2*dy*dT
                    Tnovo = (T[k+1,j,i]+T[k-1,j,i]+(T[k,j-1,i]-2*dy*dT)+T[k,j-1,i]+T[k,j,i+1]+T[k,j,i-1])/6

                elif (faceCCderiv==3) and (k==0):       #Face Frontal CC na Derivada: T[k-1,j,i] = T[k+1,j,i]-2*dz*dT
                    Tnovo = (T[k+1,j,i]+(T[k+1,j,i]-2*dz*dT)+T[k,j+1,i]+T[k,j-1,i]+T[k,j,i+1]+T[k,j,i-1])/6 

                elif (faceCCderiv==4) and (k==Nz-1):    #Face Traseira CC na Derivada: T[k+1,j,i] = T[k-1,j,i]-2*dz*dT
                    Tnovo = ((T[k-1,j,i]-2*dz*dT)+T[k-1,j,i]+T[k,j+1,i]+T[k,j-1,i]+T[k,j,i+1]+T[k,j,i-1])/6

                elif (faceCCderiv==5) and (i==0):   #Face Esquerda CC na Derivada: T[k,j,i-1] = T[k,j,i+1]-2*dx*dT
                    Tnovo = (T[k+1,j,i]+T[k-1,j,i]+T[k,j+1,i]+T[k,j-1,i]+T[k,j,i+1]+(T[k,j,i+1]-2*dx*dT))/6

                elif (faceCCderiv==6) and (i==Nx-1):   #Face Direita CC na Derivada: T[k,j,i+1] = T[k,j,i-1]-2*dx*dT
                    Tnovo = (T[k+1,j,i]+T[k-1,j,i]+T[k,j+1,i]+T[k,j-1,i]+(T[k,j,i-1]-2*dx*dT)+T[k,j,i-1])/6
                else:
                    Tnovo = (T[k+1,j,i]+T[k-1,j,i]+T[k,j+1,i]+T[k,j-1,i]+T[k,j,i+1]+T[k,j,i-1])/6

                
                T[k,j,i] = (Tnovo*f_relax)+((1-f_relax)*Tvelho)
                erro[k,j,i] = (Tnovo-Tvelho)/Tnovo

    interacoes = interacoes + 1
    tol_enc = erro.max()

print(T)
print("So pra Segurar o break")



