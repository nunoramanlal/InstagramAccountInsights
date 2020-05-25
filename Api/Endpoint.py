from instagram_private_api import Client, ClientCompatPatch


class Endpoint:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.api = Client(username, password)
     
    def getUserID(self):
     return self.api.authenticated_user_id

    def getFollowers(self, userid):
        return self.api.user_followers(userid, self.api.generate_uuid())

    def getFollowing(self, userid):
        return self.api.user_following(userid, self.api.generate_uuid())
          
       

