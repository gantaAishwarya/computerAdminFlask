from flask import request
from flask_restful import Resource
from .initialisationManager import databaseManager


class NotifyAdmin(Resource):

    def post(self):

        print('[app.py] [/NotifyAdmin] got request')
        empAbr = request.args['empAbr']

        print('[app.py] [/NotifyAdmin] received employee abbreviation is '+ empAbr)
        # TODO: Handle invalid cases or empty cases
        try:
            print('[app.py] [/NotifyAdmin] calling databaseManager notifyAdmin')
            res = databaseManager.notifyAdmin(empAbr)
            return res,200
        except Exception as e:
            print('ERRORR!! [app.py] [GetComputerByEmp]'+ str(e))
            return 'ERROR'