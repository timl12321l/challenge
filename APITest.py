from Page import PageInfo
import requests, unittest, urllib, json

class APITest(unittest.TestCase):

    def setUp(self):
        self.api = PageInfo()

    def testRequireAPIKey(self):
        payload = {'api_key':''}
        self.response = requests.get(self.api.baseURL, params=urllib.urlencode(payload))
        self.assertEquals(self.response.status_code, 200, self.response.json()['error']['message'])


    def testStatus200ReturnsDataCopyright(self):
        payload = {'api_key': self.api.apiKey}
        self.response = requests.get(self.api.baseURL, params=urllib.urlencode(payload))
        if self.response.status_code == 200:
            self.dict = self.response.json()

            if 'date' not in self.dict:
                self.assertFalse("ERROR: The field 'date' does not exists.")

            if 'copyright' not in self.dict:
                self.assertFalse("ERROR: The field 'copyright' does not exist.")

            self.urlResp = self.dict['url']
            self.hdurlResp = self.dict['hdurl']
            self.assertNotEqual(self.urlResp, self.hdurlResp)



    def testResponseUrlDiffFromHDUrl(self):
        payload = {'api_key': self.api.apiKey}
        self.response = requests.get(self.api.baseURL, params=urllib.urlencode(payload))
        if self.response.status_code == 200:
            self.dict = self.response.json()
            self.urlResp = self.dict['url']
            self.hdurlResp = self.dict['hdurl']
            self.assertNotEqual(self.urlResp, self.hdurlResp)



    def tearDown(self):
        self.api = None



if __name__ == '__main__':
    unittest.main()
