'''from elasticsearch import Elasticsearch
es = Elasticsearch('http://localhost:9200')'''
#es.index(index='my_index',id=1,body={'text': 'this is a test'})
#es.index(index='my_index',id=2,body={'text': 'this is a second test'})

'''try:
    res = es.search(index='my_index', body={'query': {'match' : {'text': 'this second test'}}})
    print(res)
    print(res['hits']['hits'][0]['_source']['text'])
    print(res['hits']['hits'][1]['_source']['text'])
except:
    print("Nothing found, sorry")'''

#es.indices.delete('my_index')

from app import create_app
from app.search import add_to_index, query_index
from app.models import Post
app = create_app()

with app.app_context():
    query, total = Post.search('is', 1, 100)
    for p in query.all():
        print(p)    