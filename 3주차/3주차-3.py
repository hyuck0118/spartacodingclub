from pymongo import MongoClient
client = MongoClient('localhost', 27017)

# localhost = 270.0.0.1

db = client.dbsparta

param = {'name': '아무개'}
data = {'age':30}
db.users.update_one(param, {'$set': data})


# all_users = list(db.users.find())
# find function gives a list while find_one gives a dictionary which is why list is used
# when using find_one, the id of something is associated frequently because there must be guarantee that the thing looked for is the only one

