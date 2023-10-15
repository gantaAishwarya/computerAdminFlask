import json
from flask import request
from flask_restful import Resource
from .initialisationManager import databaseManager


class GetComputerByEmp(Resource):

    def post(self):

        print('[app.py] [/GetComputerByEmp] got request')
        empAbr = request.args['empAbr']
        print('[app.py] [/GetComputerByEmp] received employee abbreviation is '+ empAbr)
        # TODO: Handle invalid cases or empty cases
        try:
            print('[app.py] [/GetComputerByEmp] calling databaseManager getComputerByEmp')
            res = databaseManager.getComputerByEmp(empAbr)
            return res,200
        except Exception as e:
            print('ERRORR!! [app.py] [GetComputerByEmp]'+ str(e))
            return 'ERROR'