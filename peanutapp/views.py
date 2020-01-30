# -*- coding: utf-8 -*-
import json
import requests
from django.utils.dateformat import DateFormat
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect, QueryDict
from .forms import careerForm, oauthForm, noteForm, educationForm
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import View
from django.views.generic.edit import FormView
from .models import career, oauth, note, education

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
        #print(career_list)

        dict = {
            'c_name0' : request.POST.get('c_name0') or None,
            'em_status0' : request.POST.get('em_status0'),
            'rank0' : request.POST.get('rank0'),
            'c_sdate0' : request.POST.get('c_sdate0') or None,
            'c_edate0' : request.POST.get('c_edate0') or None,
            'c_status0' : request.POST.get('c_status0'),
            'c_quit_reason0' : request.POST.get('c_quit_reason0') or None,
            'content0' : request.POST.get('content0') or None,
            'c_name1': request.POST.get('c_name1') or None,
            'em_status1': request.POST.get('em_status1'),
            'rank1': request.POST.get('rank1'),
            'c_sdate1': request.POST.get('c_sdate1') or None,
            'c_edate1': request.POST.get('c_edate1') or None,
            'c_status1': request.POST.get('c_status1'),
            'c_quit_reason1': request.POST.get('c_quit_reason1') or None,
            'content1': request.POST.get('content1') or None,
            'c_name2': request.POST.get('c_name2') or None,
            'em_status2': request.POST.get('em_status2'),
            'rank2': request.POST.get('rank2'),
            'c_sdate2': request.POST.get('c_sdate2') or None,
            'c_edate2': request.POST.get('c_edate2') or None,
            'c_status2': request.POST.get('c_status2'),
            'c_quit_reason2': request.POST.get('c_quit_reason2') or None,
            'content2': request.POST.get('content2') or None,
            'c_name3': request.POST.get('c_name3') or None,
            'em_status3': request.POST.get('em_status3'),
            'rank3': request.POST.get('rank3'),
            'c_sdate3': request.POST.get('c_sdate3') or None,
            'c_edate3': request.POST.get('c_edate3') or None,
            'c_status3': request.POST.get('c_status3'),
            'c_quit_reason3': request.POST.get('c_quit_reason3') or None,
            'content3': request.POST.get('content3') or None,
            'c_name4': request.POST.get('c_name4') or None,
            'em_status4': request.POST.get('em_status4'),
            'rank4': request.POST.get('rank4'),
            'c_sdate4': request.POST.get('c_sdate4') or None,
            'c_edate4': request.POST.get('c_edate4') or None,
            'c_status4': request.POST.get('c_status4'),
            'c_quit_reason4': request.POST.get('c_quit_reason4') or None,
            'content4': request.POST.get('content4') or None,
            'c_name5': request.POST.get('c_name5') or None,
            'em_status5': request.POST.get('em_status5'),
            'rank5': request.POST.get('rank5'),
            'c_sdate5': request.POST.get('c_sdate5') or None,
            'c_edate5': request.POST.get('c_edate5') or None,
            'c_status5': request.POST.get('c_status5'),
            'c_quit_reason5': request.POST.get('c_quit_reason5') or None,
            'content5': request.POST.get('content5') or None,
            'c_name6': request.POST.get('c_name6') or None,
            'em_status6': request.POST.get('em_status6'),
            'rank6': request.POST.get('rank6'),
            'c_sdate6': request.POST.get('c_sdate6') or None,
            'c_edate6': request.POST.get('c_edate6') or None,
            'c_status6': request.POST.get('c_status6'),
            'c_quit_reason6': request.POST.get('c_quit_reason6') or None,
            'content6': request.POST.get('content6') or None,
            'c_name7': request.POST.get('c_name7') or None,
            'em_status7': request.POST.get('em_status7'),
            'rank7': request.POST.get('rank7'),
            'c_sdate7': request.POST.get('c_sdate7') or None,
            'c_edate7': request.POST.get('c_edate7') or None,
            'c_status7': request.POST.get('c_status7') or None,
            'c_quit_reason7': request.POST.get('c_quit_reason7') or None,
            'content7': request.POST.get('content7') or None,
            'c_name8': request.POST.get('c_name8') or None,
            'em_status8': request.POST.get('em_status8') or None,
            'rank8': request.POST.get('rank8'),
            'c_sdate8': request.POST.get('c_sdate8') or None,
            'c_edate8': request.POST.get('c_edate8') or None,
            'c_status8': request.POST.get('c_status8'),
            'c_quit_reason8': request.POST.get('c_quit_reason8') or None,
            'content8': request.POST.get('content8') or None,
            'c_name9': request.POST.get('c_name9') or None,
            'em_status9': request.POST.get('em_status9'),
            'rank9': request.POST.get('rank9'),
            'c_sdate9': request.POST.get('c_sdate9') or None,
            'c_edate9': request.POST.get('c_edate9') or None,
            'c_status9': request.POST.get('c_status9') or None,
            'c_quit_reason9': request.POST.get('c_quit_reason9') or None,
            'content9': request.POST.get('content9') or None,
            'reg_date': career_list.reg_date
        }

        career.objects.filter(id=request.session.get('id')).update(**dict)
        return HttpResponseRedirect("/career")

class NoteView(View):
    form_class = noteForm
    initial = {'key': 'value'}
    template_name = 'peanutapp/note.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        dict = request.POST.dict()
        print(request.POST)

        dict['id'] = request.session.get('id')
        dict['title'] = request.POST.get('title')
        dict['type'] = request.POST.get('type')
        dict['content'] = request.POST.get('content')
        dict['reg_date'] = DateFormat(datetime.now()).format('Y-m-d')

        form = self.form_class(dict)

        if form.is_valid():
            career = form.save(commit=False)
            career.save()
            return HttpResponseRedirect("/noteList")

        return render(request, self.template_name)

class NoteListView(View):
    form_class = noteForm
    initial = {'key': 'value'}
    template_name = 'peanutapp/note_list.html'

    def get(self, request):
        if (request.session.get('id')):
            #note_list = note.objects.get()
            if(request.GET.get('type')):
                type = request.GET.get('type')
                note_list = note.objects.filter(id=request.session.get('id'), type=type).values()
            else:
                #type = ''
                note_list = note.objects.filter(id=request.session.get('id')).values()

            note_type = note.objects.filter(id=request.session.get('id')).values('type').distinct()
            print(note_list)
            data = {
                'list' : note_list,
                'type' : note_type
            }
            return render(request, self.template_name, data)
        else:
            return HttpResponseRedirect("/")

class NoteListUpdate(View):
    form_class = noteForm
    initial = {'key': 'value'}
    template_name = 'peanutapp/note_update.html'

    def get(self, request):
        print(request.GET.get('idx'))
        note_list = note.objects.filter(idx=request.GET.get('idx')).values()
        data = {
            'list': note_list
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):

        dict = {
            'title' : request.POST.get('title'),
            'idx' : request.POST.get('idx'),
            'content' : request.POST.get('content'),
            'type' : request.POST.get('type')
        }

        note.objects.filter(idx=request.POST.get('idx')).update(**dict)
        return HttpResponseRedirect("/noteList")

class NoteDelete(View):
    form_class = noteForm
    initial = {'key': 'value'}

    def get(self, request):
        idx = request.GET.get('idx')
        
        note_list = note.objects.filter(idx=idx)
        note_list.delete()
        return HttpResponseRedirect("/noteList")


class EducationView(View):
    form_class = educationForm
    initial = {'key': 'value'}
    template_name = 'peanutapp/education.html'
    template_name1 = 'peanutapp/education_list.html'
    def get(self, request):
        if (request.session.get('id')):
            education_list = education.objects.filter(id=request.session.get('id')).values()
            print(education_list)
            if (education_list):
                data = {
                    'list': education_list
                }
                return render(request,  self.template_name1, data)
            else:
                return render(request, self.template_name)
            return render(request, self.template_name)
        else:
            return HttpResponseRedirect("/")

    def post(self, request, *args, **kwargs):
        edu_category = request.POST.getlist('edu_category')
        name = request.POST.getlist('name')
        location = request.POST.getlist('location')
        sdate = request.POST.getlist('sdate')
        edate = request.POST.getlist('edate')
        graduated_yn =  request.POST.getlist('graduated_yn')
        subject = request.POST.getlist('subject')
        high_category = request.POST.getlist('high_category')
        grades = request.POST.getlist('grades')
        uni_category = request.POST.getlist('uni_category')

        print(sdate)

        for i in range(len(request.POST.getlist('name'))-1):
            print(i)
            print(edu_category[i])
            dict = {
                'id' : request.POST.get('id'),
                'edu_category': edu_category[i] or None,
                'name': name[i] or None,
                'location': location[i] or None,
                'sdate': sdate[i] or None,
                'edate': edate[i] or None,
                'graduated_yn' : graduated_yn[i] or None,
                'subject' : subject[i] or None,
                'high_category' : high_category[i] or None,
                'grades' : grades[i] or None,
                'uni_category' : uni_category[i] or None
            }

            print(dict)
    
            form = self.form_class(dict)
            if form.is_valid():
                edu_save = form.save(commit=False)
                edu_save.save()

        return HttpResponseRedirect("/education")

class EducationUpdateView(View):
    form_class = educationForm
    initial = {'key': 'value'}
    template_name = 'peanutapp/education_update.html'

    def get(self, request):
        if(request.GET.get('id')):
            education_list = education.objects.filter(id=request.GET.get('id')).values()
            print(education_list)
            if (education_list):
                data = {
                    'list': education_list
                }
                return render(request, self.template_name, data)
            else:
                return HttpResponseRedirect("/education")

    def post(self, request, *args, **kwargs):

        idx = request.POST.getlist('idx')
        edu_category = request.POST.getlist('edu_category')
        name = request.POST.getlist('name')
        location = request.POST.getlist('location')
        sdate = request.POST.getlist('sdate')
        edate = request.POST.getlist('edate')
        graduated_yn = request.POST.getlist('graduated_yn')
        subject = request.POST.getlist('subject')
        high_category = request.POST.getlist('high_category')
        grades = request.POST.getlist('grades')
        uni_category = request.POST.getlist('uni_category')

        #print(type(idx))
        #print(type(high_category))
        for i in range(len(request.POST.getlist('idx')) - 1):
            #print(edu_category[i])
            dict = {
                'edu_category': edu_category[i] or None,
                'name': name[i] or None,
                'location': location[i] or None,
                'sdate': sdate[i] or None,
                'edate': edate[i] or None,
                'graduated_yn': graduated_yn[i] or None,
                'subject': subject[i] or None,
                'high_category': high_category[i] or None,
                'grades': grades[i] or None,
                'uni_category': uni_category[i] or None
            }

            print(type(dict['sdate']))
            education.objects.filter(idx=idx[i]).update(**dict)

        return HttpResponseRedirect("/education")
