import json

def readJson(data):
	return json.loads(json.dumps(data))

def getFollowersList(data):
	return readJson(data)['users']

def getFollowingList(data):
	return readJson(data)['users']

def getFollowingUserNames(data):
	followingUsernames = []
	followingList = getFollowingList(data)
	for followingListEntry in followingList:
		entry = readJson(followingListEntry)['username']
		followingUsernames.append(entry)
	return followingUsernames

def getFollowersUserNames(data):
	followersUsernames = []
	followersList = getFollowersList(data)
	for followersListEntry in followersList:
		entry = readJson(followersListEntry)['username']
		followersUsernames.append(entry)
	return followersUsernames

