#Importing the required libraries
from flask import Flask
from flask_restful import Api, Resource
from resources.config import DB_config
from .extensions import db
from .addComputer import AddComputer
from .getComputerByMAC import GetComputerByMac
from .getComputerByEmp import GetComputerByEmp
from .updateComputer import UpdateComputer
from .deleteComputer import DeleteComputer
from .getAllComputers import GetAllComputers
from .notifyAdmin import NotifyAdmin

#Function to register required extensions
def register_extensions(app):
    #initialising db
    db.init_app(app=app)
    with app.app_context():
        db.create_all()


#Function to create application
def create_app(config):
    app = Flask(__name__)
    app.config |= config
    register_extensions(app=app)
    
    return app

#Initialising the flask application
app = create_app(DB_config)

#Adding the required resources
api = Api(app)
api.add_resource(AddComputer,'/api/addComputer')
api.add_resource(GetComputerByMac,'/api/getComputerByMac')
api.add_resource(GetComputerByEmp,'/api/getComputerByEmp')
api.add_resource(UpdateComputer,'/api/updateComputer')
api.add_resource(DeleteComputer,'/api/deleteComputer')
api.add_resource(GetAllComputers,'/api/getAllComputers')
