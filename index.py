import elasticsearch
from elasticsearch_dsl import Search
import pathlib

INDEX_NAME = 'index-1'

ELASTIC_HOST = 'http://localhost:9200/'

client = elasticsearch.Elasticsearch(hosts=[ELASTIC_HOST])

data_1 = {
    'id':1,
    'name':'med',
    'tag':'the beast'
}
data_2 = {
     'id':2,
    'name':'meg',
    'tag':'wa7ech '
}
data_3 = {
     'id':3,
    'name':'elastic',
    'tag':pathlib.Path('es.txt').read_text()
}

#add_data_1 = client.index(index=INDEX_NAME , body=data_1)
#print(add_data_1)
#add_data_2 = client.index(index=INDEX_NAME , body=data_2)
#print(add_data_2)
if __name__ == '__main__':
    q = input('what do you want?')

    field = ['name','tag']

    res = Search(index = INDEX_NAME).using(client).query('multi_match',fields=field,fuzziness='AUTO',query=q)
    
    for hit in res:
        print(hit.id,hit.name)