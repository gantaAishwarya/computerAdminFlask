from flask import request
from flask_restful import Resource
from .initialisationManager import databaseManager


class DeleteComputer(Resource):

    def post(self):

        print('[app.py] [/DeleteComputer] got request')
        MAC = request.args['MAC']

        print('[app.py] [/DeleteComputer] received MAC address is '+ MAC)
        # TODO: Handle invalid cases or empty cases
        try:
            print('[app.py] [/DeleteComputer] calling databaseManager deleteComputer function')
            res = databaseManager.deleteComputer(MAC)
            return res,200
        
        except Exception as e:
            print('ERRORR!! [app.py] [DeleteComputer]'+ str(e))
            return 'ERROR'