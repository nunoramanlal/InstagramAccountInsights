from Api.Endpoint import Endpoint

class RetrieveData:
    
    def __init__(self): 
            username = ''
            password = ''
            self.endpoint = Endpoint(username, password)
            self.userId = self.endpoint.getUserID()
    
    def getFollowers(self):
        return self.endpoint.getFollowers(self.userId)
    
    def getFollowing(self):
        return self.endpoint.getFollowing(self.userId)
