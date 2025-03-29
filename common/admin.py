from django.contrib import admin

admin.site.index_title = 'Home'
admin.site.site_title = 'Play2Learn Admin'
admin.site.site_header = 'PlayLearn Admin'

class Play2LearnAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_max_show_all = 1000