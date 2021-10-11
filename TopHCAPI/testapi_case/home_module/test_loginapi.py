from TopHCAPI.others.filepath import readFilepath
from TopHCAPI.others.yamlexcelload import loadyaml
from TopHCAPI.pageapi.home_module.loginapi import LoginToken


class TestLoginApi:
    def setup(self):
        self.loginapi = LoginToken()

    filepath = readFilepath.LoginTestDataPath
    data = loadyaml(filepath)

    #@pytest.mark.parametrize("is_ldap, password, tenant, user", yaml.safe_load(open("")))
    def test_post_token(self):
        testdata = self.data['TH-CP-LOGIN-0001']
        res = self.loginapi.login_token()
        assert res['scode'] == testdata['scode']
        assert res['message'] == testdata['message']
        print(res['data']['token']) #获取企业云的login_token(用户身份验证信息)

