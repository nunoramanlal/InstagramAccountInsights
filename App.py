from Services.RetrieveDataService import RetrieveData
import Services.ReadDataService as ReadData

#followingResponse = RetrieveData().getFollowing()
#followersResponse = RetrieveData().getFollowers()
tagsSuggestions = RetrieveData().tag_follow_suggestions()

print(tagsSuggestions)

#followingListUsers = ReadData.getFollowingUserNames(followingResponse)
#followersListUsers = ReadData.getFollowersUserNames(followersResponse)

#print('following')
#for user in followingListUsers:
#    print(user)

print('.............')
#print('following')
#for user in followersListUsers:
#    print(user)


