from elasticsearch import Elasticsearch

es = Elasticsearch()
import json
with open("./companies.json") as f:
    d = {"withdesc" :0,
    "withtags" :0,
    "withoverview" :0,
    "od" : 0 }
    for line in f:
        comp = json.loads(line)
        comp["screenshots"] = ""
        comp["image"] = ""
        if comp["tag_list"]:
            comp["tag_list"] = comp["tag_list"].replace(",", " ").replace('-', "")

        else:
            comp["tag_list"] = "NULL"
        data = {"tags" : comp["tag_list"], 
                "category" : comp["category_code"],
                "description" : "%s %s" % (comp["description"] , comp["overview"])  }
        od = False
        if comp["description"]:
            d["withdesc"] += 1
            od=True
        if comp["overview"]:
            d["withoverview"] += 1
            od =True
        if comp["tag_list"]:
            d["withtags"] += 1
        
        if od:
            d["od"] += 1
        if comp["tag_list"] != "NULL":
            print es.index(index="nullvals", doc_type="compy", body=json.dumps(data))
    print d