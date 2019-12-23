# -*- coding: utf-8 -*-
import json
import requests
from django.utils.dateformat import DateFormat
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect, QueryDict
from .forms import careerForm, oauthForm
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import View
from django.views.generic.edit import FormView
from .models import career, oauth

class IndexView(View):

    form_class = oauthForm
    initial = {'key': 'value'}
    template_name = 'peanutapp/main.html'

    def get(self, request):
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
                'nickname' : json.loads(kakao_response.text).get('properties').get('nickname'),
                'reg_date' : DateFormat(datetime.now()).format('Y-m-d')
            }

            login_check = oauth.objects.filter(id=data['id']).values()
            print(login_check)

            if( len(login_check) == 0 ):
                form = self.form_class(data)
                oauth_save = form.save(commit=False)       #oauth란 이름으로 모델을 가져왔으므로 변수명을  oauth로 똑같이 쓸수 없음.
                oauth_save.save()
                request.session['id'] = data['id']
                request.session['nickname'] = data['nickname']
                #return render(request, self.template_name, data)
                return HttpResponseRedirect("/")
            else:
                request.session['id'] = data['id']
                request.session['nickname'] = data['nickname']
                #return render(request, self.template_name, data)
                return HttpResponseRedirect("/")

            #return HttpResponse(data)
        else:
            return render(request, self.template_name)

    def post(self, request):
            return render(request, self.template_name)

'''
#함수형 뷰
@csrf_exempt
def career(request):
    if request.method == "POST":
        dict = request.POST.dict()

        dict['id'] = request.POST.get('id')
        dict['c_name0'] = request.POST.get('c_name0')
        dict['em_status0'] =  request.POST.get('em_status0')
        dict['rank0'] = request.POST.get('rank0')
        dict['c_sdate0'] = request.POST.get('c_sdate0')
        dict['c_edate0'] = request.POST.get('c_edate0')
        dict['c_status0'] = request.POST.get('c_status0')
        dict['c_quit_reason0'] = request.POST.get('c_quit_reason0')
        dict['content0'] = request.POST.get('content0')
        dict['c_name1'] = request.POST.get('c_name1')
        dict['em_status1'] = request.POST.get('em_status1')
        dict['rank1'] = request.POST.get('rank1')
        dict['c_sdate1'] = request.POST.get('c_sdate1')
        dict['c_edate1'] = request.POST.get('c_edate1')
        dict['c_status1'] = request.POST.get('c_status1')
        dict['c_quit_reason1'] = request.POST.get('c_quit_reason1')
        dict['content1'] = request.POST.get('content1')
        dict['c_name2'] = request.POST.get('c_name2')
        dict['em_status2'] = request.POST.get('em_status2')
        dict['rank2'] = request.POST.get('rank2')
        dict['c_sdate2'] = request.POST.get('c_sdate2')
        dict['c_edate2'] = request.POST.get('c_edate2')
        dict['c_status2'] = request.POST.get('c_status2')
        dict['c_quit_reason2'] = request.POST.get('c_quit_reason2')
        dict['content2'] = request.POST.get('content2')
        dict['c_name3'] = request.POST.get('c_name3')
        dict['em_status3'] = request.POST.get('em_status3')
        dict['rank3'] = request.POST.get('rank3')
        dict['c_sdate3'] = request.POST.get('c_sdate3')
        dict['c_edate3'] = request.POST.get('c_edate3')
        dict['c_status3'] = request.POST.get('c_status3')
        dict['c_quit_reason3'] = request.POST.get('c_quit_reason3')
        dict['content3'] = request.POST.get('content3')
        dict['c_name4'] = request.POST.get('c_name4')
        dict['em_status4'] = request.POST.get('em_status4')
        dict['rank4'] = request.POST.get('rank4')
        dict['c_sdate4'] = request.POST.get('c_sdate4')
        dict['c_edate4'] = request.POST.get('c_edate4')
        dict['c_status4'] = request.POST.get('c_status4')
        dict['c_quit_reason4'] = request.POST.get('c_quit_reason4')
        dict['content4'] = request.POST.get('content4')
        dict['c_name5'] = request.POST.get('c_name5')
        dict['em_status5'] = request.POST.get('em_status5')
        dict['rank5'] = request.POST.get('rank5')
        dict['c_sdate5'] = request.POST.get('c_sdate5')
        dict['c_edate5'] = request.POST.get('c_edate5')
        dict['c_status5'] = request.POST.get('c_status5')
        dict['c_quit_reason5'] = request.POST.get('c_quit_reason5')
        dict['content5'] = request.POST.get('content5')
        dict['c_name6'] = request.POST.get('c_name6')
        dict['em_status6'] = request.POST.get('em_status6')
        dict['rank6'] = request.POST.get('rank6')
        dict['c_sdate6'] = request.POST.get('c_sdate6')
        dict['c_edate6'] = request.POST.get('c_edate6')
        dict['c_status6'] = request.POST.get('c_status6')
        dict['c_quit_reason6'] = request.POST.get('c_quit_reason6')
        dict['content6'] = request.POST.get('content6')
        dict['c_name7'] = request.POST.get('c_name7')
        dict['em_status7'] = request.POST.get('em_status7')
        dict['rank7'] = request.POST.get('rank7')
        dict['c_sdate7'] = request.POST.get('c_sdate7')
        dict['c_edate7'] = request.POST.get('c_edate7')
        dict['c_status7'] = request.POST.get('c_status7')
        dict['c_quit_reason7'] = request.POST.get('c_quit_reason7')
        dict['content7'] = request.POST.get('content7')
        dict['c_name8'] = request.POST.get('c_name8')
        dict['em_status8'] = request.POST.get('em_status8')
        dict['rank8'] = request.POST.get('rank8')
        dict['c_sdate8'] = request.POST.get('c_sdate8')
        dict['c_edate8'] = request.POST.get('c_edate8')
        dict['c_status8'] = request.POST.get('c_status8')
        dict['c_quit_reason8'] = request.POST.get('c_quit_reason8')
        dict['content8'] = request.POST.get('content8')
        dict['c_name9'] = request.POST.get('c_name9')
        dict['em_status9'] = request.POST.get('em_status9')
        dict['rank9'] = request.POST.get('rank9')
        dict['c_sdate9'] = request.POST.get('c_sdate9')
        dict['c_edate9'] = request.POST.get('c_edate9')
        dict['c_status9'] = request.POST.get('c_status9')
        dict['c_quit_reason9'] = request.POST.get('c_quit_reason9')
        dict['content9'] = request.POST.get('content9')
        dict['reg_date'] = DateFormat(datetime.now()).format('Y-m-d')

        form = careerForm(dict)

        if form.is_valid():
            career = form.save(commit=False)
            career.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("error")


    else:
        return render(request, 'peanutapp/career.html')
'''

#클래스형 뷰
class CareerView(View):
    form_class = careerForm
    initial = {'key': 'value'}
    template_name1 = 'peanutapp/career.html'
    template_name2 = 'peanutapp/career_list.html'
    success_url ='/'

    def get(self, request):
        if(request.session.get('id')):
            career_list = career.objects.filter(id = request.session.get('id')).values()
            print(career_list)
            if(career_list):
                data = {
                    'list' : career_list
                }
                return render(request, 'peanutapp/career_list.html', data)
            else:
                return render(request, self.template_name1)
        else:
            return HttpResponseRedirect("/")

    def post(self, request, *args, **kwargs):
        dict = request.POST.dict()

        dict['id'] = request.POST.get('id')
        dict['c_name0'] = request.POST.get('c_name0')
        dict['em_status0'] = request.POST.get('em_status0')
        dict['rank0'] = request.POST.get('rank0')
        dict['c_sdate0'] = request.POST.get('c_sdate0')
        dict['c_edate0'] = request.POST.get('c_edate0')
        dict['c_status0'] = request.POST.get('c_status0')
        dict['c_quit_reason0'] = request.POST.get('c_quit_reason0')
        dict['content0'] = request.POST.get('content0')
        dict['c_name1'] = request.POST.get('c_name1')
        dict['em_status1'] = request.POST.get('em_status1')
        dict['rank1'] = request.POST.get('rank1')
        dict['c_sdate1'] = request.POST.get('c_sdate1')
        dict['c_edate1'] = request.POST.get('c_edate1')
        dict['c_status1'] = request.POST.get('c_status1')
        dict['c_quit_reason1'] = request.POST.get('c_quit_reason1')
        dict['content1'] = request.POST.get('content1')
        dict['c_name2'] = request.POST.get('c_name2')
        dict['em_status2'] = request.POST.get('em_status2')
        dict['rank2'] = request.POST.get('rank2')
        dict['c_sdate2'] = request.POST.get('c_sdate2')
        dict['c_edate2'] = request.POST.get('c_edate2')
        dict['c_status2'] = request.POST.get('c_status2')
        dict['c_quit_reason2'] = request.POST.get('c_quit_reason2')
        dict['content2'] = request.POST.get('content2')
        dict['c_name3'] = request.POST.get('c_name3')
        dict['em_status3'] = request.POST.get('em_status3')
        dict['rank3'] = request.POST.get('rank3')
        dict['c_sdate3'] = request.POST.get('c_sdate3')
        dict['c_edate3'] = request.POST.get('c_edate3')
        dict['c_status3'] = request.POST.get('c_status3')
        dict['c_quit_reason3'] = request.POST.get('c_quit_reason3')
        dict['content3'] = request.POST.get('content3')
        dict['c_name4'] = request.POST.get('c_name4')
        dict['em_status4'] = request.POST.get('em_status4')
        dict['rank4'] = request.POST.get('rank4')
        dict['c_sdate4'] = request.POST.get('c_sdate4')
        dict['c_edate4'] = request.POST.get('c_edate4')
        dict['c_status4'] = request.POST.get('c_status4')
        dict['c_quit_reason4'] = request.POST.get('c_quit_reason4')
        dict['content4'] = request.POST.get('content4')
        dict['c_name5'] = request.POST.get('c_name5')
        dict['em_status5'] = request.POST.get('em_status5')
        dict['rank5'] = request.POST.get('rank5')
        dict['c_sdate5'] = request.POST.get('c_sdate5')
        dict['c_edate5'] = request.POST.get('c_edate5')
        dict['c_status5'] = request.POST.get('c_status5')
        dict['c_quit_reason5'] = request.POST.get('c_quit_reason5')
        dict['content5'] = request.POST.get('content5')
        dict['c_name6'] = request.POST.get('c_name6')
        dict['em_status6'] = request.POST.get('em_status6')
        dict['rank6'] = request.POST.get('rank6')
        dict['c_sdate6'] = request.POST.get('c_sdate6')
        dict['c_edate6'] = request.POST.get('c_edate6')
        dict['c_status6'] = request.POST.get('c_status6')
        dict['c_quit_reason6'] = request.POST.get('c_quit_reason6')
        dict['content6'] = request.POST.get('content6')
        dict['c_name7'] = request.POST.get('c_name7')
        dict['em_status7'] = request.POST.get('em_status7')
        dict['rank7'] = request.POST.get('rank7')
        dict['c_sdate7'] = request.POST.get('c_sdate7')
        dict['c_edate7'] = request.POST.get('c_edate7')
        dict['c_status7'] = request.POST.get('c_status7')
        dict['c_quit_reason7'] = request.POST.get('c_quit_reason7')
        dict['content7'] = request.POST.get('content7')
        dict['c_name8'] = request.POST.get('c_name8')
        dict['em_status8'] = request.POST.get('em_status8')
        dict['rank8'] = request.POST.get('rank8')
        dict['c_sdate8'] = request.POST.get('c_sdate8')
        dict['c_edate8'] = request.POST.get('c_edate8')
        dict['c_status8'] = request.POST.get('c_status8')
        dict['c_quit_reason8'] = request.POST.get('c_quit_reason8')
        dict['content8'] = request.POST.get('content8')
        dict['c_name9'] = request.POST.get('c_name9')
        dict['em_status9'] = request.POST.get('em_status9')
        dict['rank9'] = request.POST.get('rank9')
        dict['c_sdate9'] = request.POST.get('c_sdate9')
        dict['c_edate9'] = request.POST.get('c_edate9')
        dict['c_status9'] = request.POST.get('c_status9')
        dict['c_quit_reason9'] = request.POST.get('c_quit_reason9')
        dict['content9'] = request.POST.get('content9')
        dict['reg_date'] = DateFormat(datetime.now()).format('Y-m-d')

        #form = self.form_class(request.POST)
        form = self.form_class(dict)


        if form.is_valid():
            career = form.save(commit=False)
            career.save()
            return HttpResponseRedirect("/career")
        return render(request, self.template_name1)

class MypageView(View):
    #form_class = mypageForm
    initial = {'key': 'value'}
    template_name = 'peanutapp/mypage.html'

    def get(self, request):
        return render(request, self.template_name)

class CareerUpdateView(View):
    initial = {'key': 'value'}
    template_name = 'peanutapp/career_update.html'
    template_name2 = 'peanutapp/career_list.html'
    def get(self, request):
        career_list = career.objects.filter(id=request.session.get('id')).values()

        data = {
            'list' : career_list
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        career_list = career.objects.get(pk=request.session.get('id'))
        dict = {
            'c_name0' : request.POST.get('c_name0'),
            'em_status0' : request.POST.get('em_status0'),
            'rank0' : request.POST.get('rank0'),
            'c_sdate0' : request.POST.get('c_sdate0'),
            'c_edate0' : request.POST.get('c_edate0'),
            'c_status0' : request.POST.get('c_status0'),
            'c_quit_reason0' : request.POST.get('c_quit_reason0'),
            'content0' : request.POST.get('content0'),
        }

        career.objects.filter(id=request.session.get('id')).update(**dict)
        return HttpResponseRedirect("/career")

