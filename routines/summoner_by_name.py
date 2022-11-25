from extractor.utils import MongoDB

mongo = MongoDB('league')

all_summoners = mongo.query_documents(query={"entries" : {"$exists" : 1}}, projection={"entries.summonerName" : 1})

print(type(all_summoners))
print(all_summoners)

summoners_names_list = []


for i in all_summoners:

    try:
        for k in i['entries']:

            summoners_names_list.append(k['summonerName'])

    except Exception as e:
        print(i)
        continue


print(summoners_names_list[:10])
print(len(summoners_names_list))