import pymongo

client = pymongo.MongoClient('mongodb+srv://sharshweta8879:Shweta90821@cluster0.y2fxqsz.mongodb.net/')

db=client['janhit']

contactdb=db['contact']
joindb=db['join']
donationdb=db['donation']

admin=db['admin']

