from Services.RetrieveDataService import RetrieveData
import Services.ReadDataService as ReadData

followingResponse = RetrieveData().getFollowing()
followersResponse = RetrieveData().getFollowers()

followingListUsers = ReadData.getFollowingUserNames(followingResponse)
followersListUsers = ReadData.getFollowersUserNames(followersResponse)

print('following')
for user in followingListUsers:
    print(user)

print('.............')
print('following')
for user in followersListUsers:
    print(user)


