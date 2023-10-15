import json
from flask import request
from flask_restful import Resource
from .initialisationManager import databaseManager

class AddComputer(Resource):

    def post(self):
        print('[app.py] [/AddComputer] got request')
        try:
            data = request.args['data']
            data_dict = json.loads(data)
            print('[app.py] [/AddComputer] calling databaseManager AddComputer')
        
            res = databaseManager.addComputer(data_dict)    
            return res,200
        except Exception as e:
            print('ERRORR!! [app.py] [AddComputer]'+ str(e))
            return 'ERROR'