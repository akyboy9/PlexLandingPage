from plexapi import myplex, exceptions


def verify_plex_access(username, password):
    __master_acc = myplex.MyPlexAccount(username='', password='')
    __master_acc_friends = __master_acc.users()
    try:
        curr_user = myplex.MyPlexAccount(username=username, password=password)
        curr_user_friends = curr_user.users()
        if curr_user in __master_acc_friends:
            if __master_acc in curr_user_friends:
                return True
            else:
                return False
        else:
            return False
    except exceptions.BadRequest:
        return False
