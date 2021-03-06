from django.contrib import admin
from courses.models import Course, Lesson
# Register your models here.

class LessonInline(admin.StackedInline):
    model = Lesson
    fields = ['subject', 'description', 'order']

class CourseAdmin(admin.ModelAdmin):
    
    
    list_display = ['name', 'short_description']
    search_fields = ['name']
    inlines = [LessonInline]




admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)


