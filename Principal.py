__author__=  'Agustin Rodriguez Ochoa'
from MemoriaDinamica import*

bodeguita = ['aceite','manzana', 'pepsi', 'jamon', 'jugo' , 'jitomates']
precios = [26, 40, 50, 45, 10,20]

listas=memDinamica(bodeguita);
listas.imprimirLista()
listas.ordenarLista()
listas.imprimirLista()
listas.agregarelementoarray('jabon')
listas.imprimirLista()

listas2= memDinamica(precios)
listas2.imprimirLista()
listas2.agregarelementoarray(60)
listas2.imprimirLista()