import json
from flask import request
from flask_restful import Resource
from .initialisationManager import databaseManager


class GetComputerByMac(Resource):

    def post(self):

        print('[app.py] [/GetComputerByMac] got request')
        macAddr = request.args['MAC']
        print('[app.py] [/GetComputerByMac] received mac address is '+ macAddr)

        try:
            print('[app.py] [/GetComputerByMac] calling databaseManager getComputerByMac')
            res = databaseManager.getComputerByMac(macAddr)
            return res,200
        except Exception as e:
            print('ERRORR!! [app.py] [GetComputerByMac]'+ str(e))
            return 'ERROR'