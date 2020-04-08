from flask import Flask
from flask import jsonify
from pymongo import MongoClient

app = Flask(__name__)

cluster = MongoClient("mongodb+srv://jordanh:Rainbow1@cluster0-i7aze.mongodb.net/test?retryWrites=true&w=majority")

db = cluster['game-on']

activity_collection = db['activities']

basketball = {"_id": 1, "name": "basketball", "description": "i be playin hoops"}
volleyball = {"_id": 2, "name": "volleyball", "description": "i be spikin"}
spike_ball = {"_id": 3, "name": "spike ball", "description": "i still be spikin"}

# activity_collection.insert_many([volleyball, spike_ball])

spike_query = {"name":"spike ball"}

found_sports = activity_collection.find({})

# activity_collection.delete_one({"name":"b-ball"})
# activity_collection.insert_one(basketball)

# bball = activity_collection.update_one({"name": "basketball"}, {"$set":{"name": 'b-ball'}})




# print(found_sport['name'])

@app.route('/activities', methods = ['GET'])
def activities_index():
  # return jsonify(activity_collection.find({}))
  x = [sport for sport in found_sports]
  return jsonify(x)
    # return response


app.run()




# return jsonify(activity_collection)


# myclient = pymongo.MongoClient('mongodb://localhost:27017/')

# round_up_db = myclient['mydatabase']


# app = Flask(__name__)

# current_events = [
#          {
#             'id': 1,
#             'activity': 'Volleyball',
#             'location': 'Wash Park',
#             'lat': 123.45,
#             'long': 543.21,
#             'time': 1700,
#             'duration': 'Could be a min and max input from the user -- ex. 15 min 120 max',
#             'notes': 'If the weather is poor, meet here instead',
#             'max_players': 10,
#             'players_going': 5,
#             'skill_level': 'Professional',
#             'equipment': [
#                {
#                'name': 'Net',
#                'still_needed': False
#                },
#                {
#                'name': 'Ball',
#                'still_needed': True
#                }
#             ]
#          },
#          {
#             'id': 2,
#             'activity': 'Volleyball',
#             'location': 'Wash Park',
#             'lat': 123.45,
#             'long': 543.21,
#             'time': 1700,
#             'duration': 'Could be a min and max input from the user -- ex. 15 min 120 max',
#             'notes': 'If the weather is poor, meet here instead',
#             'max_players': 10,
#             'players_going': 5,
#             'skill_level': 'Professional',
#             'equipment': [
#                {
#                'name': 'Net',
#                'still_needed': False
#                },
#                {
#                'name': 'Ball',
#                'still_needed': True
#                }
#             ]
#          }
#       ]

# dblist = myclient.list_database_names()
# if "mydatabase" in dblist:
#   print("The database exists.")
# else:
#   print('nada')

# @app.route('/events')
# def events():
#   return jsonify(current_events)
  
