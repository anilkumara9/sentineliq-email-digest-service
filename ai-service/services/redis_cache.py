import redis
import os
import hashlib
import json

class RedisCache:
    def __init__(self):
        redis_host = os.getenv('REDIS_HOST', 'localhost')
        redis_port = int(os.getenv('REDIS_PORT', 6379))
        self.client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
        self.ttl = 900 # 15 minutes

    def _generate_key(self, prompt):
        return f"ai_cache:{hashlib.sha256(prompt.encode()).hexdigest()}"

    def get(self, prompt):
        try:
            key = self._generate_key(prompt)
            cached = self.client.get(key)
            if cached:
                return json.loads(cached)
        except Exception as e:
            print(f"Redis get error: {e}")
        return None

    def set(self, prompt, response):
        try:
            key = self._generate_key(prompt)
            self.client.setex(key, self.ttl, json.dumps(response))
        except Exception as e:
            print(f"Redis set error: {e}")

redis_cache = RedisCache()
