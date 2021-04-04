import time
from locust import HttpUser, task, between

ip='''5
1
2
3
4
5
'''
c='''
n=int(input())
ans=0
for i in range(n):
	ans+=int(input())
print(ans)
# while True:
# 	print("test")
'''
class QuickstartUser(HttpUser):
    wait_time = between(1,2)

    @task
    def hello_world(self):
        # self.client.post('/',json={'lng':'python','code':c,'stdip':ip})
        self.client.get('/')



    def on_start(self):
        self.client.get('/')