# -*- coding: utf-8 -*-
"""

@author: libra
"""

import nltk 
import codecs

from nltk.tokenize.toktok import ToktokTokenizer

#tokenizador TokTok (palabras)
toktok = ToktokTokenizer()

#tokenizador de oraciones
es_tokenizador_oraciones = nltk.data.load('tokenizers/punkt/spanish.pickle')

#obtener oraciones de un parrafo
parrafo = "Este es un texto de prueba. ¿Crees que pueda tokenizar bien cada oración? ¡Ya lo veremos!"

#abrir archizo a tokenizar
file = codecs.open("practica3.txt", "r", "utf-8")
content = file.read()
#print(content)
file.close()

#oraciones = es_tokenizador_oraciones.tokenize(parrafo)
oraciones = es_tokenizador_oraciones.tokenize(content)

#obtener token de cada oración
for s in oraciones:
    print([t for t in toktok.tokenize(s)])

#Salto de linea en codigo
print("----------------------------")

#Remover las palabras funcionales
#from nltk.corpus import stopwords

#print(stopwords.words("spanish"))

#print("----------------------------")

#print(content)

#print("----------------------------")

#print(stopwords.words(content))

#Stemming con NLTK
from nltk.stem.snowball import SnowballStemmer
 
# Stemmer en Espa˜nol
stemmer = SnowballStemmer("spanish")

tokens = [] # <- aquí va el texto tokenizado
 
for t in tokens:
    # Obtener la raiz
    print(stemmer.stem(t))
    
    