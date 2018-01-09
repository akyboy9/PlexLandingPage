from plexapi import myplex, exceptions


def verify_plex_access(username, password):
    __master_acc = myplex.MyPlexAccount(username='zhoffm@gmail.com', password='akyzachypoo')
    __master_acc_friends = [friend.username for friend in __master_acc.users()]
    try:
        curr_user = myplex.MyPlexAccount(username=str(username), password=str(password))
        curr_user_friends = [friend.username for friend in curr_user.users()]
        if curr_user.username == __master_acc.username:
            return True
        elif curr_user.username in __master_acc_friends:
            if __master_acc.username in curr_user_friends:
                return True
            else:
                return False
        else:
            return False
    except exceptions.BadRequest:
        return False
