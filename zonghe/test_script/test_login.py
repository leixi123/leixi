import pytest

from zonghe.baw import Member
from zonghe.caw import DataRead, MySqlOp


# 前置条件，注册的数据
@pytest.fixture(params=DataRead.read_yaml(r"test_data\login_setup.yaml"))
def setup_data(request):
    return request.param


# 登录的测试数据
@pytest.fixture(params=DataRead.read_yaml(r"test_data\login_data.yaml"))
def login_data(request):
    return request.param


# 测试前置与后置，环境准备与清理
@pytest.fixture()
def register(setup_data, baserequest, url, db_info):
    # 初始化环境，避免环境中已有本次测试的数据
    MySqlOp.delete_user(db_info, setup_data['data']['mobilephone'])
    # 注册用户
    r = Member.register(baserequest, url, setup_data['data'])
    yield
    # 删除注册用户
    MySqlOp.delete_user(db_info, setup_data['data']['mobilephone'])


def test_login(register, login_data, baserequest, url, db_info):
    # 下发登录请求
    r = Member.login(baserequest, url, login_data['data'])
    # 检查接口的返回结果与预期结果一致
    assert r.json()['code'] == login_data['expect']['code']
    assert r.json()['status'] == login_data['expect']['status']
    assert r.json()['msg'] == login_data['expect']['msg']
