from elasticsearch import Elasticsearch
from pprint import pprint
import requests
es = Elasticsearch()
es.cluster.health(wait_for_status='yellow', request_timeout=500)

req = '''{"query":{"match_all":{}},"size":0,"aggregations":{"tags":{"terms":{"field":"description","size":5000, "order" : { "_count" : "asc" },
"shard_size": 0,
"min_doc_count":30
},"aggregations":{"sigterms":{"significant_terms":{"field":"description","min_doc_count":5}}}}}}'''
import json
#res = es.search(index="como", body=req, timeout=500)
data=requests.post("http://localhost:9200/como/_search",data=req)

res = data.json()

for ag in res["aggregations"]["tags"]["buckets"]:
    sigt = []
    for term in ag["sigterms"]["buckets"]:
        if term["score"] > 1:
            sigt.append(term["key"])
    if len(sigt) > 3:
        print({ag["key"] : sigt})

