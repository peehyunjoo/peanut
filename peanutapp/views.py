# -*- coding: utf-8 -*-
import json
import requests
#from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
def index(request):
    if(request.GET.get('code')):
        #return HttpResponse(request.GET.get('code'))
        code = request.GET.get('code')
        url = 'https://kauth.kakao.com/oauth/token'

        headers = {'Content-type': 'application/x-www-form-urlencoded; charset=utf-8'}

        body = {'grant_type' : 'authorization_code',
                'client_id' : '448844327114515aa2e08f9cbf79a49a',
                'redirect_uri' : 'http://49.174.123.151:8000/',
                'code': code }

        #return HttpResponse(f'{body}')
        kakao_response = requests.post(url, headers = headers, data = body)
        #return HttpResponse(f'{kakao_response.text}')

        access_token = json.loads(kakao_response.text).get('access_token')

        url = 'https://kapi.kakao.com/v2/user/me'

        headers = {
            'Authorization' : f'Bearer {access_token}',
            'Content-type' : 'application/x-www-form-urlencoded; charset=utf-8'
        }

        kakao_response = requests.get(url, headers = headers)

        data = {
            'id' : json.loads(kakao_response.text).get('id'),
            'nickname' : json.loads(kakao_response.text).get('properties').get('nickname')
        }

        print(data)
        #return render(request, 'peanutapp/main.html',data)
        return HttpResponseRedirect("/")
        #return HttpResponse(data)
    else:
        return render(request, 'peanutapp/main.html')
