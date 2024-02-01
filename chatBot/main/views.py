
from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests

psid = "ewhi7-YV_AAxa1Um0B7YNBpK_pHzMRRyyWTl0eFim914qZuN-qwYyjjNOnQDqhziAEMRjQ."
psidts = "sidts-CjEBPVxjSqob-1RIOgvtm-kPwI931pW6mfrH9oC9ISObChi8HGfsHDX40eBEfwAGJrpzEAA"
psidcc = "ABTWhQEvmBXNB8QXavuzP2zYFr2A1K6fnp72aoH-Uck4uT4jw3rU6G1ASWkwqsquOi86CPNs_Fw"
#cria um conjunto com os tokens de autenticação
#para poder usar o Bard
tokenCookies = {
    "__Secure-1PSID": psid,
    "__Secure-1PSIDTS": psidts,
    "__Secure-1PSIDCC": psidcc, 
}
#cria o objeto bard para ser usado
bard = BardCookies(cookie_dict=tokenCookies)

#define as ações da API para receber
#os comandos a ser passado para o Bard
class ChatBotAPIView(APIView):
    def post(self, request):
        #pega os dados que veio na requisição
        data = request.data

        print("data received:")
        print(data['question'])

        conversationId = data.get('conversationId')
        if(conversationId is not None):
            bard.conversation_id = conversationId

        answer = bard.get_answer(data['question'])

        return Response(status=201,data=answer)

