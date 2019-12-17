# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class career(models.Model):

    id = models.CharField(max_length=20,primary_key=True)
    c_name0 = models.CharField(max_length=30, null=True, blank=True)
    em_status0 = models.CharField(max_length=1, null=True, blank=True)
    rank0 = models.CharField(max_length=1, null=True, blank=True)
    c_sdate0 = models.DateField(null=True, blank=True)
    c_edate0 = models.DateField(null=True, blank=True)
    c_status0 = models.CharField(max_length=1 ,null=True,blank=True)
    c_quit_reason0 = models.CharField(max_length=20, null=True,blank=True)
    content0 = models.TextField(null=True, blank=True)
    c_name1 = models.CharField(max_length=30 ,null=True, blank=True)
    em_status1 = models.CharField(max_length=1, null=True,blank=True)
    rank1 = models.CharField(max_length=1, null=True,blank=True)
    c_sdate1 = models.DateField(null=True, blank=True)
    c_edate1 = models.DateField(null=True, blank=True)
    c_status1 = models.CharField(max_length=1 , null=True,blank=True)
    c_quit_reason1 = models.CharField(max_length=20, null=True,blank=True)
    content1 = models.TextField(null=True,blank=True)
    c_name1 = models.CharField(max_length=30, null=True,blank=True)
    em_status1 = models.CharField(max_length=1 , null=True,blank=True)
    rank1 = models.CharField(max_length=1 ,null=True,blank=True)
    c_sdate1 = models.DateField(null=True, blank=True)
    c_edate1 = models.DateField(null=True, blank=True)
    c_status1 = models.CharField(max_length=1 , null=True,blank=True)
    c_quit_reason1 = models.CharField(max_length=20 , null=True,blank=True)
    content1 = models.TextField(null=True,blank=True)
    c_name2 = models.CharField(max_length=30 ,null=True,blank=True)
    em_status2 = models.CharField(max_length=1 ,null=True,blank=True)
    rank2 = models.CharField(max_length=1 , null=True,blank=True)
    c_sdate2 = models.DateField(null=True, blank=True)
    c_edate2 = models.DateField(null=True, blank=True)
    c_status2 = models.CharField(max_length=1 , null=True,blank=True)
    c_quit_reason2 = models.CharField(max_length=20, null=True,blank=True)
    content2 = models.TextField(null=True,blank=True)
    c_name3 = models.CharField(max_length=30 ,null=True,blank=True)
    em_status3 = models.CharField(max_length=1 ,null=True,blank=True)
    rank3 = models.CharField(max_length=1 , null=True,blank=True)
    c_sdate3 = models.DateField(null=True, blank=True)
    c_edate3 = models.DateField(null=True, blank=True)
    c_status3 = models.CharField(max_length=1 , null=True,blank=True)
    c_quit_reason3 = models.CharField(max_length=20 , null=True,blank=True)
    content3 = models.TextField(null=True,blank=True)
    c_name4 = models.CharField(max_length=30 ,null=True,blank=True)
    em_status4 = models.CharField(max_length=1 ,null=True,blank=True)
    rank4 = models.CharField(max_length=1 ,null=True,blank=True)
    c_sdate4 = models.DateField(null=True, blank=True)
    c_edate4 = models.DateField(null=True, blank=True)
    c_status4 = models.CharField(max_length=1 ,null=True,blank=True)
    c_quit_reason4 = models.CharField(max_length=20 ,null=True,blank=True)
    content4 = models.TextField(null=True,blank=True)
    c_name5 = models.CharField(max_length=30 ,null=True,blank=True)
    em_status5 = models.CharField(max_length=1 ,null=True,blank=True)
    rank5 = models.CharField(max_length=1 ,null=True,blank=True)
    c_sdate5 = models.DateField(null=True, blank=True)
    c_edate5 = models.DateField(null=True, blank=True)
    c_status5 = models.CharField(max_length=1 , null=True,blank=True)
    c_quit_reason5 = models.CharField(max_length=20 ,null=True,blank=True)
    content5 = models.TextField(null=True,blank=True)
    c_name6 = models.CharField(max_length=30 ,null=True,blank=True)
    em_status6 = models.CharField(max_length=1 ,null=True,blank=True)
    rank6 = models.CharField(max_length=1 ,null=True,blank=True)
    c_sdate6 = models.DateField(null=True, blank=True)
    c_edate6 = models.DateField(null=True, blank=True)
    c_status6 = models.CharField(max_length=1 ,null=True,blank=True)
    c_quit_reason6 = models.CharField(max_length=20 ,null=True,blank=True)
    content6 = models.TextField(null=True,blank=True)
    c_name7 = models.CharField(max_length=30 ,null=True,blank=True)
    em_status7 = models.CharField(max_length=1 ,null=True,blank=True)
    rank7 = models.CharField(max_length=1 ,null=True,blank=True)
    c_sdate7 = models.DateField(null=True, blank=True)
    c_edate7 = models.DateField(null=True, blank=True)
    c_status7 = models.CharField(max_length=1, null=True,blank=True)
    c_quit_reason7 = models.CharField(max_length=20 ,null=True,blank=True)
    content7 = models.TextField(null=True,blank=True)
    c_name8 = models.CharField(max_length=30 ,null=True,blank=True)
    em_status8 = models.CharField(max_length=1, null=True,blank=True)
    rank8 = models.CharField(max_length=1 , null=True,blank=True)
    c_sdate8 = models.DateField(null=True, blank=True)
    c_edate8 = models.DateField(null=True, blank=True)
    c_status8 = models.CharField(max_length=1 ,null=True,blank=True)
    c_quit_reason8 = models.CharField(max_length=20 ,null=True,blank=True)
    content8 = models.TextField(null=True,blank=True)
    c_name9 = models.CharField(max_length=30 ,null=True,blank=True)
    em_status9 = models.CharField(max_length=1 ,null=True,blank=True)
    rank9 = models.CharField(max_length=1 ,null=True,blank=True)
    c_sdate9 = models.DateField(null=True, blank=True)
    c_edate9 = models.DateField(null=True, blank=True)
    c_status9 = models.CharField(max_length=1 , null=True,blank=True)
    c_quit_reason9 = models.CharField(max_length=20 , null=True, blank=True)
    content9 = models.TextField(null=True,blank=True)
    reg_date = models.DateField()


    def __str__(self):
         return "id="+self.id+"c_name0"+self.c_name0+"em_status0"+self.em_status+"rank0"+self.rank0+"c_sdate0"+self.c_sdate0+"c_edate0"+self.c_edate0+"c_status0"+self.c_status0+"c_quit_reason0"+self.c_quit_reason0+ "content0"+content0+\
                "c_name1"+self.c_name1+"em_status1"+self.em_status+"rank1"+self.rank1+"c_sdate1"+self.c_sdate1+"c_edate1"+self.c_edate1+"c_status1"+self.c_status1+"c_quit_reason1"+self.c_quit_reason1+"content1"+self.content1+\
                "c_name2"+self.c_name2+"em_status2"+self.em_status+"rank2"+self.rank2+"c_sdate2"+self.c_sdate2+"c_edate2"+self.c_edate2+"c_status2"+self.c_status2+"c_quit_reason2"+self.c_quit_reason2 +"content2"+self.content2+\
                "c_name3"+self.c_name3+"em_status3"+self.em_status+"rank3"+self.rank3+"c_sdate3"+self.c_sdate3+"c_edate3"+self.c_edate3+"c_status3"+self.c_status3+"c_quit_reason3"+self.c_quit_reason3+"content3"+self.content3+\
                "c_name4"+self.c_name4+"em_status4"+self.em_status+"rank4"+self.rank4+"c_sdate4"+self.c_sdate4+"c_edate4"+self.c_edate4+"c_status4"+self.c_status4+"c_quit_reason4"+self.c_quit_reason4+"content4"+self.content4+\
                "c_name5"+self.c_name5+"em_status5"+self.em_status+"rank5"+self.rank5+"c_sdate5"+self.c_sdate5+"c_edate5"+self.c_edate5+"c_status5"+self.c_status5+"c_quit_reason5"+self.c_quit_reason5+"content5"+self.content5+\
                "c_name6"+self.c_name6+"em_status6"+self.em_status+"rank6"+self.rank6+"c_sdate6"+self.c_sdate6+"c_edate6"+self.c_edate6+"c_status6"+self.c_status6+"c_quit_reason6"+self.c_quit_reason6+"content6"+self.content6+\
                "c_name7"+self.c_name7+"em_status7"+self.em_status+"rank7"+self.rank7+"c_sdate7"+self.c_sdate7+"c_edate7"+self.c_edate7+"c_status7"+self.c_status7+"c_quit_reason7"+self.c_quit_reason7+"content7"+self.content7+\
                "c_name8"+self.c_name8+"em_status8"+self.em_status+"rank8"+self.rank8+"c_sdate8"+self.c_sdate8+"c_edate8"+self.c_edate8+"c_status8"+self.c_status8+"c_quit_reason8"+self.c_quit_reason8+"content8"+self.content8+\
                "c_name9"+self.c_name9+"em_status9"+self.em_status+"rank9"+self.rank9+"c_sdate9"+self.c_sdate9+"c_edate9"+self.c_edate9+"c_status9"+self.c_status9+"c_quit_reason9"+self.c_quit_reason9+"content9"+self.content9+"reg_date"+self.reg_date