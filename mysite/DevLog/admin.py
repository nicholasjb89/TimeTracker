from django.contrib import admin
from django import forms
from .models import Log, Category, Subject

# Register your models here.
#admin.site.register(Log)
admin.site.register(Category)
admin.site.register(Subject)


#first create a custom form to use in admin
class LogAdminForm(forms.ModelForm):
    #The product model is defined with out the category, so add one in for display
    category = forms.ModelChoiceField(queryset=Category.objects.all().order_by('name'), widget=forms.Select(attrs={'id':'category'}), required=False)
    #This field is used exclusively for the javascript so that I can select the
    #correct category when editing an existing product
    selected_cat = forms.CharField(widget=forms.HiddenInput, required=False)


    def __init__(self, *args, **kwargs):
        super(LogAdminForm, self).__init__(*args, **kwargs)
        #print dir(self.instance)
        try:
            #Try and set the selected_cat field from instance if it exists
            self.fields['selected_cat'].initial = self.instance.subject.category.id
        except:
            pass

    class Media:
        #Alter these paths depending on where you put your media
        js = (
            'js/mootools-1.2-core-yc.js',
            'js/log.js',
        )

class LogAdmin(admin.ModelAdmin):
    form = LogAdminForm
    #I don't like using a fieldset here, because it makes the form more brittle,
    #if you change the model for form be sure to update the fieldset.
    #I'm using it in this instance because I need for category to show up
    #right above the subject
    fieldsets = (
        (None, {
            'fields' : ('category','subject','hours','date_time','comment')
        }),
        ('Optional', {
            'classes' : ('collapse',),
            'fields' : ('selected_cat',)
        })
    )

admin.site.register(Log, LogAdmin)