class TestLogin:
    def test_001(self, login): #login的前置
        print("登录用例1")
    def test_002(self, db,login): # db的前置
        print("登录用例2")
    def test_003(self):
        print("登录用例3")   # login、db的后置