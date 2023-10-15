from sqlalchemy import func
from ..resources.config import DB_config
from ..data.dom import Computers,db

class DatabaseManager:
    def __init__(self):
        # If you are using any external cloud or other databases then you can perform database initialisations here
        pass

    def __finally__(self):
        # If you are using any external databases and need to close connections or cursors can use this function
        pass

    def addComputer(self, data:dict):
        print('[DatabaseManager.py] [addComputer] adding new computer to computers table')

        # Extract values from the input data dictionary
        MAC = data.get('MAC')
        name = data.get('name')
        IPAddr = data.get('IPAddr')
        empAbr = data.get('empAbr')
        description = data.get('description')

        try:
            #Executing the query
            computer_count = self.getComputerCount(empAbr)
            if(computer_count <= 3):
                newComputer = Computers(MAC=MAC,name=name,IPAddr=IPAddr,empAbr=empAbr,description=description)
                db.session.add(newComputer)
                # Commit the changes to the database
                db.session.commit()  
                print('[DatabaseManager.py] [addComputer] computer Successfully added to the table')
                #self.__finally__()
                return 'success'
            else:
                # TODO: Handle the docker call here
                return 'success'


        except Exception as e:
            #self.__finally__()
            return 'ERROR!! ' + str(e)
    
    def getComputerCount(self, empAbr):
        print('[DatabaseManager.py] [getComputerCount] Counting computers belonging to user ' + empAbr)

        try:
            # Query for counting the number of computers for the specified user (empAbr)
            count = db.session.query(func.count(Computers.MAC)).filter_by(empAbr=empAbr).scalar()

            print('[DatabaseManager.py] [getComputerCount] Successfully retrieved data')
            return count

        except Exception as e:
            return 'ERROR!! ' + str(e)

