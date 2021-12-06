from influxdb import InfluxDBClient

# 初始化（指定要操作的数据库）
client = InfluxDBClient('localhost', 8086, 'admin', 'password', 'test2')
print(client.get_list_database()) # 显示所有数据库名称
client.create_database('testdb') # 创建数据库
print(client.get_list_database()) # 显示所有数据库名称
client.drop_database('testdb') # 删除数据库
print(client.get_list_database()) # 显示所有数据库名称
# test