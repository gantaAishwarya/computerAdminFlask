from flask import request
from flask_restful import Resource
from .initialisationManager import databaseManager


class GetAllComputers(Resource):

    def get(self):

        print('[app.py] [/GetAllComputers] got request')

        print('[app.py] [/GetAllComputers] retrieving all the computers from "computers" table')
        
        try:
            print('[app.py] [/GetAllComputers] calling databaseManager getAllComputers')
            res = databaseManager.getAllComputers()
            return res,200
        
        except Exception as e:
            print('ERRORR!! [app.py] [GetAllComputers]'+ str(e))
            return 'ERROR'