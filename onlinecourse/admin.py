from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice
from nested_admin import NestedModelAdmin, NestedTabularInline

# <HINT> Register QuestionInline and ChoiceInline classes here
class ChoiceInLine(NestedTabularInline):
    model = Choice
    extra = 2

class QuestionInLine(NestedTabularInline):
    inlines = [ChoiceInLine]
    model = Question
    extra = 1

class LessonInline(NestedTabularInline):
    inlines = [QuestionInLine]
    model = Lesson
    extra = 0


# Register your models here.
class CourseAdmin(NestedModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(NestedModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question)
admin.site.register(Choice)
