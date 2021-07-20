# Generated by Django 3.2.5 on 2021-07-20 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
                ('is_active', models.BooleanField(default=True, verbose_name='активность')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='пометка удаленности')),
                ('title', models.CharField(help_text='Название опроса', max_length=300, verbose_name='Название')),
                ('description', models.CharField(blank=True, default='', help_text='Описание', max_length=1000, verbose_name='Описание')),
                ('date_start', models.DateTimeField(blank=True, null=True, verbose_name='дата старта')),
                ('date_finish', models.DateTimeField(blank=True, null=True, verbose_name='дата окончания')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
                ('is_active', models.BooleanField(default=True, verbose_name='активность')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='пометка удаленности')),
                ('text', models.CharField(blank=True, default='', help_text='Описание', max_length=1000, verbose_name='Текст вопроса')),
                ('type', models.CharField(choices=[('text answer', 'ответ текстом'), ('answer with a choice of one option', 'ответ с выбором одного варианта'), ('answer with a choice of several options', 'ответ с выбором нескольких вариантов')], default='text answer', max_length=100, verbose_name='Тип вопроса')),
                ('variants', models.JSONField(blank=True, null=True, verbose_name='Список вариантов')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.poll', verbose_name='Опрос')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
