
from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests

psid = "g.a000gAhi7_OaUqP_N3Z6QpnPhlHA5SkkALsRUZGSakMVeTeTDWCWJtzvC1bCtF17fg8vhAOr4QACgYKAYYSAQASFQHGX2MiOj5L3NEcThm17D_TQoXtDhoVAUF8yKragEjbHjK_fD4b9HaSQ9-W0076"
psidts = "sidts-CjEBPVxjSvErkxsCA83_yBbIOEop70pouKGNSWK9BO5U3xqARtF3kiPrcBQYrbR3ACCGEAA"
psidcc = "ABTWhQGJDwiWbZJ3mxb7VtAE5pcxkyEfkkJn_sunibUoQbQ9_cARnpW5lOL53Opv-44kCgn9lV8"
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
        else:
            bard.conversation_id = None
    
        answer = bard.get_answer(data['question'])

        return Response(status=201,data=answer)

