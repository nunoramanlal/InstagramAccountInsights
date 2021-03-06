from Api.Endpoint import Endpoint

class RetrieveData:
    
    def __init__(self): 
            username = 'nunodeveloping'
            password = 'nunodev1234'
            self.endpoint = Endpoint(username, password)
            self.userId = self.endpoint.getUserID()
    
    def getFollowers(self):
        return self.endpoint.getFollowers(self.userId)
    
    def getFollowing(self):
        return self.endpoint.getFollowing(self.userId)

    def tag_follow_suggestions(self):
        return self.endpoint.getFeedLiked()