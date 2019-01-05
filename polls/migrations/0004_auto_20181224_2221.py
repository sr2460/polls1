# Generated by Django 2.0.2 on 2018-12-24 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20181123_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_comment_text', models.TextField(blank=True, null=True, verbose_name='コメント(未入力可)')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='choice_comment',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Choice'),
        ),
        migrations.AddField(
            model_name='choice_comment',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]
