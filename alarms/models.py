from django.db import models
from users.models import Baseclass
from subscriptions.models import Subscription

class Alarm(Baseclass):
    """
    최선우 : 구독정보 알림 모델 추가
    """
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    DDAY_TYPE = [
        (ONE, '1일전'), (TWO, '2일전'), (THREE, '3일전'), (FOUR, '4일전'),
        (FIVE, '5일전'), (SIX, '6일전'), (SEVEN, '7일전'),
    ]
    d_day = models.PositiveSmallIntegerField(verbose_name='카테고리 종류', choices=DDAY_TYPE, help_text='선택 시, 해당 일자에 메일이 발송됩니다.', null=True)
    subscription = models.ForeignKey(Subscription, verbose_name='구독정보', on_delete=models.SET_NULL, null=True, related_name='alarm_subscription')
    is_active = models.BooleanField(verbose_name="메일 발송 여부", default=False)

    def __str__(self):
        return f"({self.subscription})의 {self.get_d_day_display()} 알림"

    class Meta:
        verbose_name = '알림 정보'
        verbose_name_plural = "알림 정보 목록"
        
class AlarmHistory(Baseclass):
    """
    최선우 : 구독정보 알림 내역 모델 추가
    """
    alarm = models.ForeignKey(Alarm, verbose_name='알림', on_delete=models.SET_NULL, null=True)
    content = models.TextField(verbose_name='알림 내역', default='', null=True, blank=True, help_text='발송시 메일 내용을 그대로 넣어줍니다.')
    is_success = models.BooleanField(verbose_name='발송 성공 여부', default=False)
    traceback = models.TextField(verbose_name='발송 실패 원인', default='', blank=True)
    
    def __str__(self):
        return f"({self.alarm}) 내역"

    class Meta:
        verbose_name = '알림 내역'
        verbose_name_plural = "알림 내역 목록"