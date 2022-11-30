from three_letters import three_letters_list
from five_letters import five_letters_list
from seven_letters import seven_letters_list
from stadii import lista_stadii
from random import choice
from random import randint
from simple_colors import blue
from simple_colors import black
from simple_colors import green
from simple_colors import magenta
from simple_colors import red
from simple_colors import yellow
from simple_colors import cyan
g=open("C:\\Users\\Celestin\\Desktop\\seif.txt","w")
print(blue("Bine ai venit la jocul spanzuratoarea!"))
print(black("Regulile jocului sunt destul de simple:Ai o spanzuratoare si un cuvant de ghicit.."))
print(green("La fiecare pas trebuie sa ghicesti o litera din cuvant,iar daca litera sa gaseste in cuvant se vor completa"
" casutele goale cu toate aparitiile ei,dar daca nu se va completa omuletul la spanzuratoare.."))
print(magenta("Ai voie la maximul 5 greseli ca sa ghicesti cuvantul si ai posibilitatea(daca esti absolut sigur de "
"raspuns) sa ghicesti cuvantul,dar daca nu este cuvantul care trebuie ai pierdut!.."))
print(red("De asemenea,iti poti selecta dificultatea:usor(cuvantul are 3 litere),mediu(cuvantul are 5 litere),"
"dificil(cuvantul are 7 litere)"))
print(cyan("La dificultatea usor ti se va da o litera bonus pe o pozitie random,la mediu 2 si la dificil 3"))
print(yellow("Doresti sa joci?da/nu"))
s=input()
if s=='da':
  print(lista_stadii[0])
  dificultate=input(magenta("Selecteaza dificultatea(usor,mediu,dificil):"))
  if dificultate=="usor":
      build="___"
      ghicit=False
      greseli=0
      cuvant=choice(three_letters_list)
      g.write(cuvant)
      rnd=randint(0,2)
      build2=list(build)
      cuvant2=list(cuvant)
      build2[rnd]=cuvant2[rnd]
      build="".join(build2)
      print(green(build))
      while ghicit==False and greseli<=5:
         alegere=input(blue("Ce doresti sa ghicesti?(litera,cuvant):"))
         if alegere=="litera":
           litera=input(red("Introdu litera:"))
           if litera in cuvant:
               cuvant2 = list(cuvant)
               litera2 = list(litera)
               build2 = list(build)
               for i in range(len(cuvant2)):
                   if cuvant2[i] == litera2[0]:
                       build2[i] = litera2[0]
               build="".join(build2)
               print(black("Litera "+litera+" se afla in cuvant!"))
               print(lista_stadii[greseli])
               print(build)
           else:
               print(green("Litera " + litera + " nu se afla in cuvant!"))
               greseli+=1
               print(lista_stadii[greseli])
               print(build)
         else:
           cuvv=input(cyan("Introdu cuvantul:"))
           if cuvv==cuvant:
               ghicit=True
           else:
               greseli=6
         if build.count('_')==0:
             ghicit=True
      if ghicit==True:
          print(magenta("Felicitari!Ai castigat jocul!"))
          print(lista_stadii[greseli])
      else:
          print(red("Nu ai ghicit cuvantul!Ai pierdut jocul!"))
          print(lista_stadii[greseli])


  elif dificultate=="mediu":
      build="_____"
      ghicit=False
      greseli=0
      cuvant = choice(five_letters_list)
      g.write(cuvant)
      rnd = randint(1, 4)
      rnd2=randint(0,rnd-1)
      build2 = list(build)
      cuvant2 = list(cuvant)
      build2[rnd] = cuvant2[rnd]
      build2[rnd2]=cuvant2[rnd2]
      build = "".join(build2)
      print(yellow(build))
      while ghicit == False and greseli <= 5:
          alegere = input(blue("Ce doresti sa ghicesti?(litera,cuvant):"))
          if alegere == "litera":
              litera = input(red("Introdu litera:"))
              if litera in cuvant:
                  cuvant2 = list(cuvant)
                  litera2 = list(litera)
                  build2 = list(build)
                  for i in range(len(cuvant2)):
                      if cuvant2[i] == litera2[0]:
                          build2[i] = litera2[0]
                  build = "".join(build2)
                  print(black("Litera " + litera + " se afla in cuvant!"))
                  print(lista_stadii[greseli])
                  print(build)
              else:
                  print(green("Litera " + litera + " nu se afla in cuvant!"))
                  greseli += 1
                  print(lista_stadii[greseli])
                  print(build)
          else:
              cuvv = input(cyan("Introdu cuvantul:"))
              if cuvv == cuvant:
                  ghicit = True
              else:
                  greseli = 6
          if build.count('_') == 0:
              ghicit = True
      if ghicit == True:
          print(magenta("Felicitari!Ai castigat jocul!"))
          print(lista_stadii[greseli])
      else:
          print(red("Nu ai ghicit cuvantul!Ai pierdut jocul!"))
          print(lista_stadii[greseli])
  else:
      build="_______"
      ghicit=False
      greseli=0
      cuvant = choice(seven_letters_list)
      g.write(cuvant)
      rnd = randint(2, 6)
      rnd2=randint(1,rnd-1)
      rnd3=randint(0,rnd2-1)
      build2 = list(build)
      cuvant2 = list(cuvant)
      build2[rnd] = cuvant2[rnd]
      build2[rnd2]=cuvant2[rnd2]
      build2[rnd3]=cuvant2[rnd3]
      build = "".join(build2)
      print(green

            (build))
      while ghicit == False and greseli <= 5:
          alegere = input(blue("Ce doresti sa ghicesti?(litera,cuvant):"))
          if alegere == "litera":
              litera = input(red("Introdu litera:"))
              if litera in cuvant:
                  cuvant2 = list(cuvant)
                  litera2 = list(litera)
                  build2 = list(build)
                  for i in range(len(cuvant2)):
                      if cuvant2[i] == litera2[0]:
                          build2[i] = litera2[0]
                  build = "".join(build2)
                  print(black("Litera " + litera + " se afla in cuvant!"))
                  print(lista_stadii[greseli])
                  print(build)
              else:
                  print(green("Litera " + litera + " nu se afla in cuvant!"))
                  greseli += 1
                  print(lista_stadii[greseli])
                  print(build)
          else:
              cuvv = input(cyan("Introdu cuvantul:"))
              if cuvv == cuvant:
                  ghicit = True
              else:
                  greseli = 6
          if build.count('_') == 0:
              ghicit = True
      if ghicit == True:
          print(magenta("Felicitari!Ai castigat jocul!"))
          print(lista_stadii[greseli])
      else:
          print(red("Nu ai ghicit cuvantul!Ai pierdut jocul!"))
          print(lista_stadii[greseli])
else:
  print("Tu pierzi boss xD")
