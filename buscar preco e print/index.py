import os
import time
import os.path
##import tempfile
##import win32api
##import win32print
lista1 = []
codigoant = 0
def selecionar(lista,ini,fin):
     valor = ""
     while True:
       valor =  valor + lista[ini]
       ini = ini + 1
       if(ini >= fin):
          break
     return valor
##def imprimir(text,codigo2,desc,preco):
##     filename = tempfile.mktemp (".txt")
##     arquivo = open(filename, "w", encoding = "utf-8")
##     arquivo.write("%s\n%s\n%s\nR$:%s\n" % (text,codigo2,desc,preco))
##     win32api.ShellExecute (
##       0,
##       "print",
##       filename,
##       #
##       # If this is None, the default printer will
##       # be used anyway.
##       #
##       '/d:"%s"' % win32print.GetDefaultPrinter (),
##       ".",
##       0
##     )
##     arquivo.close()

     
def inicializacao():
     global codigoant
     while True:
          if os.path.isfile("produtos.txt") == False:
             arquivo = open("produtos.txt", "w")
             arquivo.close()
          arquivo = open("produtos.txt", "r")
          for l in arquivo.readlines():
             codigo = selecionar(l,0,13)
             produto = selecionar(l,13,33)
             preco = selecionar(l,33,45)
             lista1.append([codigo,produto,preco])
          arquivo.close()
          os.system('cls')
          print("\n\n    Supermercado Pag Menos\n")
          print(" Busca Preco")
          codigo = input(" ")
          for e in lista1:
              if(int(e[0])==int(codigo) and int(codigoant)!= int(codigo) ):
                   codigoant = codigo
                   os.system('cls')
                   print("\n\n   Produto Encontrado")
                   print("\n  %s"%e[1])
                   print("  R$ %.2f"%float(int(e[2])/100))
                   ##filename = tempfile.mktemp (".txt")
                   ##imprimir("SUPEMERCADO NOME",e[0],e[1],float(int(e[2])/100))
inicializacao()





