from ast import Not
convidados = 5
fumante = False
animaisDeEstimacao = False
area1 = "terreo"
area2 = "primeiro andar"
area3 = "area externa"

if ( not fumante == True) and (not animaisDeEstimacao == True) and (convidados < 5) :
  print("Os clentes devem ficar no ", area1)

elif (not fumante == True) or (not animaisDeEstimacao == True) and (convidados >= 5) :
  print("Os clientes devem ficar na ", area3)

else:
  print("Os clientes devem ficar na ", area2)