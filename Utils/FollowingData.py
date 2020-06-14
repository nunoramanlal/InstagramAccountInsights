def doesntFollowMeIFollow (followers, following):
    return [x for x in following if x not in followers]

def Follow_FollowBack(followers, following):
    return [element for element in followers if element in following]