from locust import TaskSet,HttpUser
# 定义任务
def login(l):
    l.client.post("/wx/auth/login",data={"username":"user123","password":"user123"})

def index(l):
    l.client.get("/wx/home/index")

def getMyOrders(l):
    l.client.get("/wx/order/list?showType=0&page=1&limit=10")

# def logout(l):
#     l.client.post("/logout")

class UserBehavier(TaskSet):
    tasks = {index:3,getMyOrders:1}

    def on_start(self):
        login(self)

    # def on_stop(self):
    #     logout(self)

class WebsitUser(HttpUser):
    # task_set = UserBehavier
    tasks = [UserBehavier]
    min_wait = 500
    max_wait = 1000
    host = "http://www.litemall360.com"
    weight = 10