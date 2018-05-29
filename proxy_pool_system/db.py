#from .utils import get_page
from random import choice
import setting
import redis

HOST=setting.HOST
PASSWORD=setting.PASSWORD
PORT=setting.PORT
INITIAL_SCORE=setting.INITIAL_SCORE
REDIS_KRY =setting.REDIS_KRY
MAX_SCORE = setting.MAX_SCORE
MIN_SCORE = setting.MIN_SCORE



class RedisClient(object):
    def __init__(self,host = HOST,password=PASSWORD,port = PORT):
        self.db = redis.StrictRedis(host=host,password=password,port=port,db=0)

    def add(self,proxy,score=INITIAL_SCORE):
        if not self.db.zscore(REDIS_KRY,proxy):
            print("添加",proxy,"成功")
            self.db.zadd(REDIS_KRY,score,proxy)


    def random(self):
        result = self.db.zrangebyscore(REDIS_KRY,MAX_SCORE,MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KRY,0,100)
            if len(result):
                return choice(result)
            else:
                print('代理池空')
                return
    def decrease(self,proxy):
        score = self.db.zscore(REDIS_KRY,proxy)
        if score and score>MIN_SCORE:
            print("代理",proxy,'当前分数：',score,"减 1 ")
            self.db.zincrby(REDIS_KRY,proxy,-1)
        else:
            print("代理",proxy,'当前分数：',score,'移除')
            self.db.zrem(REDIS_KRY,proxy)

    def exists(self,proxy):
        if self.db.zrem(REDIS_KRY,proxy):
            return True
        else:
            return False

    def max(self,proxy):
        print("代理",proxy,"可用，设置为",MAX_SCORE)
        self.db.zadd(REDIS_KRY,MAX_SCORE,proxy)

    def count(self):
        return self.db.zcard(REDIS_KRY)

    def all(self):
        return self.db.zrangebyscore(REDIS_KRY,MIN_SCORE,MAX_SCORE)

    def remove_all(self):
        self.db.zremrangebyrank(REDIS_KRY,MIN_SCORE,MAX_SCORE)
