import src.app as root
from resources.config import server_config
app = root.app

if __name__ == '__main__':
    #Running Flask application
    app.run(host=server_config.host,port=server_config.port,debug=True)