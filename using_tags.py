from elasticsearch import Elasticsearch
from pprint import pprint

es = Elasticsearch()

req = {"query":{"match_all":{}},"size":0,"aggregations":{"tags":{"terms":{"field":"tags","size":1000},"aggregations":{"sigterms":{"significant_terms":{"field":"description","min_doc_count":10}}}}}}

res = es.search(index="nullvals", body=req)


for ag in res["aggregations"]["tags"]["buckets"]:
    sigt = []
    for term in ag["sigterms"]["buckets"]:
        if term["score"] > 1:
            sigt.append(term["key"])
    if len(sigt) > 3:
        print({ag["key"] : sigt})

