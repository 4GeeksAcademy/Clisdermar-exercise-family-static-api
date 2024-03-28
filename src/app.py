"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

#from models import Person

app = Flask(__name__) #iniciar mi flask
app.url_map.strict_slashes = False # esto me permite fenerar los url 
CORS(app) # permite la comunicacion entre la api y el frontend o entre el punto A y B

# create the jackson family object
jackson_family = FamilyStructure("jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints

@app.route('/')
def sitemap():
    return generate_sitemap(app)

# GET | POST | PUT | DELETE |PATCH
# CRUD CREAR LEER ACTUALIZAR ELIMINAR
@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "miembros": members
    }


    return jsonify(response_body), 200

@app.route('/member', methods = ['POST'])

def add_member() :
    nw_member = request.json
    print(nw_member)
   
    jackson_family.add_member(nw_member)
    return jsonify({"done": "usuario creado"}), 200


@app.route('/member/<int:member_id>', methods = ['DELETE'])
def delete_family_member(member_id) :
    eliminar_familiar = jackson_family.delete_member(member_id)
    if not eliminar_familiar:
        return jsonify({"msj" : "familiar no encontrado"}), 400
    
    return jsonify({"done":"familiar eliminado"})
    _

@app.route('/member/<int:member_id>', methods= ['PUT'])
def update_family_member(member_id):
    nw_member = request.json
    update_member = jackson_family.update_member(member_id,nw_member)

    if update_member is not update_member:
        return({"msj": "no se encontro al miembro"}) , 400
    return jsonify({"done":"miembro update"})

@app.route('/member/<int:member_id>', methods= ['GET'])
def get_one_member(member_id):
    
    miembro_encontrado = jackson_family.get_member(member_id)
    if not miembro_encontrado:
        return jsonify({"msj":"miembro no encontrado"}),400
    
    return jsonify(miembro_encontrado),200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
