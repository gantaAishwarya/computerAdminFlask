from ..src.extensions import db

class Computers(db.Model):
    
    #Defining database columns based on assumptions
    MAC = db.Column(db.String(17), primary_key=True) #General MAC address is 17 characters long including special characters
    name = db.Column(db.String(80), unique=True, nullable=False) #General system name does not have any specific length
    IPAddr = db.Column(db.String(50), nullable=False) #IP Addresscan have maximum 49 characters length
    empAbr = db.Column(db.String(3)) #Given employee abbreviation is 3 characters long
    description = db.Column(db.String(100)) #Description length is not specified so giving 100 characters length

    def to_json(self):
        return {
            'MAC': self.MAC,
            'name': self.name,
            'IPAddr': self.IPAddr,
            'empAbr': self.empAbr,
            'description': self.description
        }
