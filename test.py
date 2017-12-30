from plexapi.myplex import MyPlexAccount

#master account login information

account_1 = raw_input('type in your username Zach: ')
password_1 = raw_input('type in your password Zach: ')

account_1 = str(account_1)
password_1 = str(password_1)

master_acc = MyPlexAccount(account_1, password_1)
str_1 = str(master_acc)

master_friends = master_acc.users()
master_friends = str(master_friends)

print str_1 + " ----->  login succesfull buddy"

#secondary login information
#username: akyboy9
#password: calvin999

account_2 = raw_input('type in the account username you want to login to: ')
password_2 = raw_input('type in the corresponding password: ')

login_acc = MyPlexAccount(account_2, password_2)
login_user = login_acc.username

login_user = str(login_user)

#check if its in friends list
if login_user in master_friends:
    print "LOGIN SUCCESFUL"
else:
    print "COULD NOT FIND IN FRIENDS LIST"


