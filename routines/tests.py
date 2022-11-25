from extractor.utils import MongoDB


### delete from mongo 

league = MongoDB('league')

pipeline = [
    {
        '$group': {
            '_id': {
                'tier': '$tier', 
                'division': '$division'
            }, 
            'count': {
                '$first': {
                    'entries': '$entries.summonerName', 
                    'region': '$region'
                }
            }
        }
    }, {
        '$unwind': {
            'path': '$count.entries'
        }
    }, {
        '$project': {
            '_id': 0, 
            'name': '$count.entries', 
            'region': '$count.region'
        }
    }
]

x = league.aggregate(pipeline)
print(x)
for i in x:
    print(i)

