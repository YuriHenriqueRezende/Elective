from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests

token1 = "g.a000fwg9KGLhjgoUC4tf-3hLyw2Epui9nWBbW4zRNeRbfXGmhgTsblL_ZDfuWygszVRPPH8zNwACgYKAVESAQASFQHGX2Mi4EzOYrhkwaTX6Wy_cu6liBoVAUF8yKrlwXlubOjOM_Es78sI1lLh0076"; 
token2 = "sidts-CjEBPVxjSg9vk32FHdIFYnq1mVfWyQrVK2zuwuHRwaIKDecRbIN3WJsqZVN_CbbOYGzwEAA";
token3 = "ABTWhQFgQcwEw5fXWPNEMiE2zaJxHHE2yz_Dx8V8w5psyXcxt2sUR_Au0mMgbDYLD2alaZbO";

TokenCookies = {
    "__Secure-1PSID":token1,
    "__Secure-1PSIDTS":token2,
    "__Secure-1PSIDCC":token3,
};

bard = BardCookies(cookie_dict=TokenCookies);

class ChatBotAPIView(APIView):
    def post(self,requests):
        data = requests.data;
        print("data recived:");
        print(data['question']);
        
        answer = bard.get_answer(data["question"]);
        return Response(status=201,data=answer)