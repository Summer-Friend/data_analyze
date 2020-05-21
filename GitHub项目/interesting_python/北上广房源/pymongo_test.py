'''
@Author: your name
@Date: 2020-02-02 15:17:22
@LastEditTime : 2020-02-03 19:44:08
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\北上广房源\bag_test.py
'''
import pymongo

from pymongo import MongoClient

client = MongoClient()
#print(client)
# 列出当前所有数据库名称
#读取 MongoDB 中的所有数据库，并判断指定的数据库是否存在：
'''
database_names = client.database_names()
print(database_names)
if 'local' in database_names:
    print('集合已存在')
print(client.test_database)
print(client.database_names() )
'''
db = client.test
# 调用client的test属性即可返回test数据库，当然也可以这样来指定：
# db = client['test']
#　两种方式是等价的。
collection = db.students
# collection = db['students']
# 插入数据,接下来我们便可以进行数据插入了，对于students这个Collection，我们新建一条学生数据，以字典的形式表示：
 
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
# 在这里我们指定了学生的学号、姓名、年龄和性别，然后接下来直接调用collection的insert()方法即可插入数据。
''' 
result = collection.insert(student)
print(result)
# 在MongoDB中，每条数据其实都有一个_id属性来唯一标识，如果没有显式指明_id，MongoDB会自动产生一个ObjectId类型的_id属性。
# insert()方法会在执行后返回的_id值。

# 当然我们也可以同时插入多条数据，只需要以列表形式传递即可，示例如下：
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
 
student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
 
result = collection.insert([student1, student2])
print(result)
# 返回的结果是对应的_id的集合，运行结果：
# [ObjectId('5932a80115c2606a59e8a048'), ObjectId('5932a80115c2606a59e8a049')]
# 实际上在PyMongo 3.X版本中，insert()方法官方已经不推荐使用了，当然继续使用也没有什么问题，
# 官方推荐使用insert_one()和insert_many()方法将插入单条和多条记录分开。

result = collection.insert_one(student)
print(result)
print(result.inserted_id)
# 运行结果：
# <pymongo.results.InsertOneResult object at 0x10d68b558>
# 5932ab0f15c2606f0c1cf6c5
# 返回结果和insert()方法不同，这次返回的是InsertOneResult对象，我们可以调用其inserted_id属性获取_id。
 
# 对于insert_many()方法，我们可以将数据以列表形式传递即可，示例如下：
 
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
 
student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
 
result = collection.insert_many([student1, student2])
print(result)
print(result.inserted_ids)
# insert_many()方法返回的类型是InsertManyResult，调用inserted_ids属性可以获取插入数据的_id列表，运行结果：
 
# <pymongo.results.InsertManyResult object at 0x101dea558>
# [ObjectId('5932abf415c2607083d3b2ac'), ObjectId('5932abf415c2607083d3b2ad')]


# 查询，插入数据后我们可以利用find_one()或find()方法进行查询，find_one()查询得到是单个结果，find()则返回多个结果。
result = collection.find_one({'name': 'Mike'})
print(type(result))
print(result)

# 对于多条数据的查询，我们可以使用find()方法，例如在这里查找年龄为20的数据，示例如下：
results = collection.find({'age': 20})
print(results)
for result in results:
    print(result)

# 返回结果是Cursor类型，相当于一个生成器，我们需要遍历取到所有的结果，每一个结果都是字典类型。
 
# 如果要查询年龄大于20的数据，则写法如下：
 
results = collection.find({'age': {'$gt': 20}})
for result in results:
    print(result)
# 在这里查询的条件键值已经不是单纯的数字了，而是一个字典，其键名为比较符号$gt，意思是大于，键值为20，这样便可以查询出所有
# 年龄大于20的数据。
"""     #如果用单引号，下面的汉字不能注释掉
符号含义示例
$lt小于{'age': {'$lt': 20}}
$gt大于{'age': {'$gt': 20}}
$lte小于等于{'age': {'$lte': 20}}
$gte大于等于{'age': {'$gte': 20}}
$ne不等于{'age': {'$ne': 20}}
$in在范围内{'age': {'$in': [20, 23]}}
$nin不在范围内{'age': {'$nin': [20, 23]}}
"""

# 另外还可以进行正则匹配查询，例如查询名字以M开头的学生数据，示例如下：
results = collection.find({'name': {'$regex': '^M.*'}})
for result in results:
    print(result)
    
# 在这里将一些功能符号再归类如下：
"""
符号含义示例示例含义
$regex匹配正则{'name': {'$regex': '^M.*'}}name以M开头
$exists属性是否存在{'name': {'$exists': True}}name属性存在
$type类型判断{'age': {'$type': 'int'}}age的类型为int
$mod数字模操作{'age': {'$mod': [5, 0]}}年龄模5余0
$text文本查询{'$text': {'$search': 'Mike'}}text类型的属性中包含Mike字符串
$where高级条件查询{'$where': 'obj.fans_count == obj.follows_count'}自身粉丝数等于关注数
"""
# 这些操作的更详细用法在可以在MongoDB官方文档找到：
# https://docs.mongodb.com/manual/reference/operator/query/


# 计数
# 要统计查询结果有多少条数据，可以调用count()方法，如统计所有数据条数：
 
count = collection.find().count()
print(count)
# 或者统计符合某个条件的数据：
 
count = collection.find({'age': 20}).count()
print(count)

# 排序
# 可以调用sort方法，传入排序的字段及升降序标志即可，示例如下：
 
results = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])

# 偏移,可能想只取某几个元素，在这里可以利用skip()方法偏移几个位置，比如偏移2，就忽略前2个元素，得到第三个及以后的元素。
 
results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])

# 另外还可以用limit()方法指定要取的结果个数，示例如下：
 
results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])
# 如果不加limit()原本会返回三个结果，加了限制之后，会截取2个结果返回。

# 值得注意的是，在数据库数量非常庞大的时候，如千万、亿级别，最好不要使用大的偏移量来查询数据，很可能会导致内存溢出，
# 可以使用类似find({'_id': {'$gt': ObjectId('593278c815c2602678bb2b8d')}}) 这样的方法来查询，记录好上次查询的_id。
 
# 更新
# 对于数据更新可以使用update()方法，指定更新的条件和更新后的数据即可，例如：
 
condition = {'name': 'Jordan'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update(condition, student)
print(result)
# 在这里我们将name为Jordan的数据的年龄进行更新，首先指定查询条件，然后将数据查询出来，修改年龄，
# 之后调用update方法将原条件和修改后的数据传入，即可完成数据的更新。
# 运行结果：
# {'ok': 1, 'nModified': 1, 'n': 1, 'updatedExisting': True}
# 返回结果是字典形式，ok即代表执行成功，nModified代表影响的数据条数。
 
# 另外update()方法其实也是官方不推荐使用的方法，在这里也分了update_one()方法和update_many()方法，用法更加严格，
# 第二个参数需要使用$类型操作符作为字典的键名，我们用示例感受一下。
condition = {'name': 'Kevin'}
student = collection.find_one(condition)
student['age'] = 26
result = collection.update_one(condition, {'$set': student})
print(result)
print(result.matched_count, result.modified_count)
# 在这里调用了update_one方法，第二个参数不能再直接传入修改后的字典，而是需要使用{'$set': student}这样的形式，
# 其返回结果是UpdateResult类型，然后调用matched_count和modified_count属性分别可以获得匹配的数据条数和影响的数据条数。
 
# 运行结果：
#
# <pymongo.results.UpdateResult object at 0x10d17b678>
# 1 0
# 我们再看一个例子：
 
condition = {'age': {'$gt': 20}}
result = collection.update_one(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)
# 在这里我们指定查询条件为年龄大于20，然后更新条件为{'$inc': {'age': 1}}，执行之后会讲第一条符合条件的数据年龄加1。
 
# 运行结果：
#
# <pymongo.results.UpdateResult object at 0x10b8874c8>
# 1 1
# 可以看到匹配条数为1条，影响条数也为1条。
 
# 如果调用update_many()方法，则会将所有符合条件的数据都更新，示例如下：
 
condition = {'age': {'$gt': 20}}
result = collection.update_many(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)
# 这时候匹配条数就不再为1条了，运行结果如下：
#
# <pymongo.results.UpdateResult object at 0x10c6384c8>
# 3 3
# 可以看到这时所有匹配到的数据都会被更新。
 
# 删除
# 删除操作比较简单，直接调用remove()方法指定删除的条件即可，符合条件的所有数据均会被删除，示例如下：
 
result = collection.remove({'name': 'Kevin'})
print(result)
# 运行结果：
#
# {'ok': 1, 'n': 1}
# 另外依然存在两个新的推荐方法，delete_one()和delete_many()方法，示例如下：
 
result = collection.delete_one({'name': 'Kevin'})
print(result)
print(result.deleted_count)
result = collection.delete_many({'age': {'$lt': 25}})
print(result.deleted_count)
# 运行结果：
 
# <pymongo.results.DeleteResult object at 0x10e6ba4c8>
# 1
# 4
# delete_one()即删除第一条符合条件的数据，delete_many()即删除所有符合条件的数据，返回结果是DeleteResult类型，
# 可以调用deleted_count属性获取删除的数据条数。
 
# 更多
# 另外PyMongo还提供了一些组合方法，如find_one_and_delete()、find_one_and_replace()、find_one_and_update()，
# 就是查找后删除、替换、更新操作，用法与上述方法基本一致。
 
# 另外还可以对索引进行操作，如create_index()、create_indexes()、drop_index()等。
'''
#具体参照网址https://blog.csdn.net/howsoever/article/details/79424632