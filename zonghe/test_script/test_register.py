'''
测试注册的脚本
'''

import pytest

from zonghe.baw import Member
from zonghe.caw import DataRead, MySqlOp, Check


@pytest.fixture(params=DataRead.read_yaml("test_data/register_fail.yaml"))
def fail_data(request):
    return request.param


def test_register_fail(fail_data, baserequest, url):
    '''
    注册失败的脚本
    :return:
    '''
    print(fail_data)
    # 下发请求
    r = Member.register(baserequest, url, fail_data['data'])
    print(r.text)
    # 检查结果与预期结果一致
    # assert r.json()['code'] == fail_data['expect']['code']
    # assert r.json()['status'] == fail_data['expect']['status']
    # assert r.json()['msg'] == fail_data['expect']['msg']
    Check.equal(r.json(), fail_data['expect'], 'code,status,msg')

@pytest.fixture(params=DataRead.read_yaml("test_data/register_pass.yaml"))
def pass_data(request):
    return request.param


def test_register_pass(pass_data, baserequest, url, db_info):
    '''
    注册成功
    :return:
    '''
    MySqlOp.delete_user(db_info, pass_data['data']['mobilephone'])
    print(pass_data)
    # 下发请求
    r = Member.register(baserequest, url, pass_data['data'])
    # 检查接口的返回结果与预期结果一致
    # assert r.json()['code'] == pass_data['expect']['code']
    # assert r.json()['status'] == pass_data['expect']['status']
    # assert r.json()['msg'] == pass_data['expect']['msg']
    Check.equal(r.json(), pass_data['expect'], 'code,status,msg')

    # 检查用户在系统中注册成功（1、该用户可以登录成功；
    # 2、数据库中查有没有这个用户；3、list 接口返回值能查到这个用户）
    r = Member.list(baserequest, url)
    assert pass_data['data']['mobilephone'] in r.text
    # 清理环境：删除用户（1、接口删除用户；2、数据库删除用户）
    MySqlOp.delete_user(db_info, pass_data['data']['mobilephone'])

    # 自动化测试原则
    # 1、测试环境：再执行脚本前是什么状态，执行完脚本要恢复到之前的状态
    # 2、脚本执行依赖的环境，要在脚本中自己构造。比如：
    # 审核项目接口测试时依赖已有的项目，需要先调用添加项目的接口准备测试环境。
    # 脚本的健壮性、稳定性比较高。

# @pytest.fixture(params=DataRead.read_yaml("test_data/register_repeat.yaml"))
# def repeat_data(request):
#     return request.param

# def test_register_repeat(repeat_data, baserequest,url,db_info):
#     # 重复注册测试逻辑
#     print(repeat_data)
#     # 环境准备：下发注册请求
#     r = Member.register(baserequest, url, repeat_data['data'])
#     # 测试步骤：下发注册请求（检查结果，报错重复注册）
#     # assert r.json()['code'] == repeat_data['expect']['code']
#     # assert r.json()['status'] == repeat_data['expect']['status']
#     # assert r.json()['msg'] == repeat_data['expect']['msg']
#     # 恢复环境：删除用户
#     # MySqlOp.delete_user(db_info, repeat_data['data']['mobilephone'])