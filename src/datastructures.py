
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
#Api
# De una Famili
# Agregar miembro
# Actualizar miembro
# Borrar miembro
# Obtener miembro

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [ 
              {"id": 1, "first_name": "John", "age": 33, "lucky_numbers": [7, 13, 22]},
              {"id": 2, "first_name": "Jane", "age": 35, "lucky_numbers": [10, 14, 3]},
              {"id": 3, "first_name": "Jimmy", "age": 5, "lucky_numbers": [1]}
           ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        #las lista tienen el append para a;adir cosas

        if not member.get("id"): #se utilizan parentesis en vez de corchetes xq si python no lo consigue detectara error en cambio con () si no lo consigue cae en NULL
             member["id"] = self._generateId() # crea id
        self._members.append(member)
        


    def delete_member(self, id):
        # fill this method and update the return
       print(id)
       for member in self._members:
           if member["id"] == id :
               self._members.remove(member)
               return True # porque entramos en manejar errores ,y si no existe retorno un false
       
       return False

    def update_member(self, id, member):
        # fill this method and update the return
        print("actualizando",id)
        for family_member in self._members:
            if family_member ["id"] == id:
               self._members.remove(family_member) # lo elimino
               member["id"] = id # vuelvo a crear con datos actualizados
               self._members.append(member)
               return True # simboliza operacion exitosa
        return False # no se actualizo ningun miembro por lo tanto no fue exitosa

        print("no son iguales")


    def get_member(self, id):
        # fill this method and update the return
        for family_member in self._members:
            if family_member["id"] == id:
                return family_member
        
        return False

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
