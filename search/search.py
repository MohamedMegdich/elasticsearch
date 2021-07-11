import elasticsearch
from elasticsearch_dsl import Search
import pathlib

ELASTIC_HOST = 'http://localhost:9200/'

client = elasticsearch.Elasticsearch(hosts=[ELASTIC_HOST])

INDEXES=['products']
def lookup(query, index=INDEXES ,fields = ['title','description']):
    if not query:
        return 0
    res = Search(index = index).using(client).query('multi_match',fields=fields,fuzziness='AUTO',query=query)
    results=[]
    for hit in res:
        print(hit.title,hit.description)

        data = {
            'title':hit.title,
            'description':hit.description,
            'url':hit.url
        }
        results.append(data)
    return results