from flask import Flask
from flask_restful import Api
from ..resources.config import server_config
from .addComputer import AddComputer

app = Flask(__name__)
api = Api(app)

#Adding resources
api.add_resource(AddComputer,'/api/addComputer')


if __name__ == '__main__':
    #Running Flask application
    app.run(host=server_config.host,port=server_config.port,debug=True)