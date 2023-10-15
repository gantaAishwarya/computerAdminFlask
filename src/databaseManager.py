from sqlalchemy import func
from resources.config import DB_config
from data.dom import Computers,db

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
        
    def getComputerByMac(self, MAC):
        print('[DatabaseManager.py] [getComputersByUser] retrieving computer details of mac address ' + MAC)

        try:
            # Query for retrieving computer records belonging to MAC address
            result = Computers.query.filter_by(MAC=MAC).first()
            
            if result:
                return result.to_json()
            else:
                return 'No computers found for the mac address' + MAC

        except Exception as e:
            return 'ERROR!! ' + str(e)
    
    def getComputerByEmp(self, empAbr):
        print('[DatabaseManager.py] [getComputerByEmp] retrieving computer details of employee abbreviation ' + empAbr)

        try:
            # Query for retrieving computer records belonging to MAC address
            result = Computers.query.filter_by(empAbr=empAbr).all()
            
            if result:
                computer_data = [computer.to_json() for computer in result]
                return computer_data
            else:
                return 'No computers found for the employee abbreviation ' + empAbr

        except Exception as e:
            return 'ERROR!! ' + str(e)
        
    def updateComputer(self, data:dict):

        MAC = data.get('MAC')
        #Handling the NULL Value case
        if MAC is None:
            return 'ERROR!! MAC Address is required'
        
        print('[DatabaseManager.py] [updateComputer] updating computer with MAC address: '+ MAC)

        # Extract values from the input data dictionary
        name = data.get('name')
        IPAddr = data.get('IPAddr')
        empAbr = data.get('empAbr')
        description = data.get('description')

        try:
            #Assuming MAC address is unique for each computer
            result = Computers.query.filter_by(MAC=MAC).first()
            if result is not None:
                # Updating the attributes
                result.name = name
                result.ipAddr = IPAddr
                result.empAbr = empAbr
                result.description = description

                # Commit the changes to the database
                db.session.commit()
                print('[DatabaseManager.py] [updateComputer] Successfully updated the computer data')
                return 'success'
            else:
                return 'ERROR!! Computer not found'
            
        except Exception as e:
            return 'ERROR!! ' + str(e)
        
    def deleteComputer(self, MAC):
        print('[DatabaseManager.py] [getComputerByEmp] deleting computer data related to MAC address ' + MAC)

        try:        
            #Filtering the computer with required MAC address
            result = Computers.query.filter_by(MAC=MAC).first()
            
            if result:
                # Query for deleting computer data related to mac address
                db.session.delete(result)
                db.session.commit()
                print('[DatabaseManager.py] [deleteComputer] Successfully deleted computer data')
                return 'success'
            else:
                return 'ERROR!! Computer not found'

        except Exception as e:
            return 'ERROR!! ' + str(e)
        
    def getAllComputers(self):
        print('[DatabaseManager.py] [getAllComputers] retrieving all computer details')

        try:
            # Query for retrieving all computer details
            result = Computers.query.all()
            
            if result:
                computer_data = [computer.to_json() for computer in result]
                return computer_data
            else:
                return 'No computers found'

        except Exception as e:
            return 'ERROR!! ' + str(e)
    

