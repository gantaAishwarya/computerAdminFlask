import json
from flask import request
from flask_restful import Resource
from .initialisationManager import databaseManager

class UpdateComputer(Resource):

    def post(self):
        print('[app.py] [/UpdateComputer] got request')
        try:
            data = request.args['data']
            data_dict = json.loads(data)
            print('[app.py] [/UpdateComputer] calling databaseManager UpdateComputer')
        
            res = databaseManager.updateComputer(data_dict)    
            return res,200
        except Exception as e:
            print('ERRORR!! [app.py] [UpdateComputer]'+ str(e))
            return 'ERROR'