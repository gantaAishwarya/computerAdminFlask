import json
from flask import request
from flask_restful import Resource

class AddComputer(Resource):

    def post(self):
        print('[app.py] [/AddComputer] got request')
        try:
            data = request.args['data']
            data_dict = json.loads(data)
            print('[app.py] [/AddComputer] calling databaseManager AddComputer')
            #Check if current user has more than 3 computers
            #Add user to database if count of computers is less than or equal to 3
            res = 'OK'
            return res,200
        except Exception as e:
            print('ERRORR!! [app.py] [AddComputer]'+ str(e))
            return 'ERROR'