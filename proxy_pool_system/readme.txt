###构件一个代理池
#requests+xpath+flask+redis+多线程（或者微线程异步处理）

##主要模块：存储模块+爬取模块+检测模块+接口模块

##主要功能：
#1 存储模块：用于存储爬取的ip代理，用Redis的有序集合存储，存储方式（ip+ip可用度）
#2 爬取模块：用于爬取免费的ip代理，用requests库爬取
#3 检测模块：用于检测Redis数据库中ip的可用度，不可用淘汰
#4 接口模块：用于获取Redis数据库中的可用度较高的ip

##使用方法：
#启动Redis-------redis-server.exe
#启动爬取模块和接口模块   python run.py api.py

然后连接requests.get('http://127.0.0.1/random')就可以接受到一个随机ip

