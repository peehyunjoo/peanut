from django import forms
from .models import career, oauth, note, education

class oauthForm(forms.ModelForm):
    class Meta:
        model = oauth
        fields = ('id', 'nickname', 'reg_date')

class careerForm(forms.ModelForm):
    class Meta:
        model = career
        fields = ('id','c_name0','em_status0','rank0','c_sdate0','c_edate0','c_status0','c_quit_reason0','content0',
                  'c_name1', 'em_status1', 'rank1', 'c_sdate1', 'c_edate1', 'c_status1', 'c_quit_reason1', 'content1',
                  'c_name2', 'em_status2', 'rank2', 'c_sdate2', 'c_edate2', 'c_status2', 'c_quit_reason2', 'content2',
                  'c_name3', 'em_status3', 'rank3', 'c_sdate3', 'c_edate3', 'c_status3', 'c_quit_reason3', 'content3',
                  'c_name4', 'em_status4', 'rank4', 'c_sdate4', 'c_edate4', 'c_status4', 'c_quit_reason4', 'content4',
                  'c_name5', 'em_status5', 'rank5', 'c_sdate5', 'c_edate5', 'c_status5', 'c_quit_reason5', 'content5',
                  'c_name6', 'em_status6', 'rank6', 'c_sdate6', 'c_edate6', 'c_status6', 'c_quit_reason6', 'content6',
                  'c_name7', 'em_status7', 'rank7', 'c_sdate7', 'c_edate7', 'c_status7', 'c_quit_reason7', 'content7',
                  'c_name8', 'em_status8', 'rank8', 'c_sdate8', 'c_edate8', 'c_status8', 'c_quit_reason8', 'content8',
                  'c_name9', 'em_status9', 'rank9', 'c_sdate9', 'c_edate9', 'c_status9', 'c_quit_reason9', 'content9','reg_date')


class noteForm(forms.ModelForm):
    class Meta:
        model = note
        fields = ('id','title','type','content','reg_date')

class educationForm(forms.ModelForm):
    class Meta:
        model = education
        fields = ('id','edu_category', 'name', 'location','sdate','edate','graduated_yn','subject','grades','high_category','uni_category')