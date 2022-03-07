import  configparser
config=configparser.RawConfigParser
file=".\\Configurations\\Config.ini"
config.read(file)
class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        URL=config.get('COMMON INFO','BASE_URL')
        return URL

    @staticmethod
    def getUserEmail():
        User_Name = config.get('COMMON INFO', 'USER_NAME')
        return User_Name

    @staticmethod
    def getUserPassword():
        Password = config.get('COMMON INFO', 'PASSWORD')
        return Password