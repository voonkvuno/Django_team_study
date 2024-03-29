# Generated by Django 3.2.13 on 2022-11-02 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='갱신일')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='이메일')),
                ('fullname', models.CharField(max_length=20, verbose_name='이름')),
                ('password', models.CharField(max_length=255, verbose_name='비밀번호')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='휴대폰')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile/image/', verbose_name='프로필 사진')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성 여부')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자 여부')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자 목록',
            },
        ),
    ]
