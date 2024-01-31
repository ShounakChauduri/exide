import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")
#client = MongoClient("mongodb+srv://iammrdinda:T1%402m3%404l5@cluster1.tkf1tdq.mongodb.net/")

db=client.Databasename
collection2=db.Collection_two

def create_for_userdetails_db(data):
    data=dict(data)
    response=collection2.insert_one(data)
    return str(response.inserted_id)