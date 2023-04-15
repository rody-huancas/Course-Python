from persona import Persona


persona1 = Persona('Rody', 25)
# persona1.__nombre = "Juan" #no se modificará __nombre porque es privado
# persona1.__metodo_privado() #no podrá mostrarse porque es privado
persona1.set_nombre("Juan")
persona1.get_nombre()
# print(persona1.__nombre)
print(persona1)