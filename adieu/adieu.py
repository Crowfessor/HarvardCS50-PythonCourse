#Adieu, adieu, to Liesl
#Adieu, adieu, to Liesl and Friedrich
#Adieu, adieu, to Liesl, Friedrich, and Louisa
#Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

import inflect
p = inflect.engine()

names = [ ]
text = "Adieu, adieu, to "

while True:
    try:
         name = input("Name: ")
         names.append(name)
    except EOFError:
        print()
        break

join_names = p.join(names)
print(text + join_names)
