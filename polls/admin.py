from django.contrib import admin

from .models import Choice, Question, Choice_Comment

#modelsからインポート
#管理サイトのテキストの初期選択数
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#管理サイトのサーチ機能
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Choice_Comment)
