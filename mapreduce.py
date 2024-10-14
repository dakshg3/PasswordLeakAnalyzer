from bson.code import Code
import pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["test"]
mycol = mydb["test_con"]
col = mydb["mapred"]

mostUsed = []

map = Code("function () {"
            "  emit(this.pass,1);"
            "}")


reduce = Code("function (key, values) {"
               "  var total = 0;"
               "  for (var i = 0; i < values.length; i++) {"
               "    total += values[i];"
               "  }"
               "  return total;"
               "}")

result = mycol.map_reduce(map, reduce, "mapred")

mostUsed = col.find({"value": {"$gt": 1}}).sort([("value",-1)]).limit(50)

for p in mostUsed:
	print(p)
