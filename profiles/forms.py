from django import forms

from .models import personal_information

from home.models import story

from ckeditor.widgets import CKEditorWidget

#from django.utils.html import format_html


#from django.utils.safestring import mark_safe

#class ImagePreviewWiget(forms.ClearableFileInput):

#    def render(self,name,value,attrs=None,**kwargs):
#
#        input_html=format_html(f"""<img src="{value.url}"  class="rounded-circle" width="150" height="150" /><br/>
#        <label for="avatar-clear_id">remove</label>
#        <input type="checkbox" name="avatar-clear" id="avatar-clear_id"><br/>
#       
#        <br/>Change:
#        <input type="file" name="avatar" accept="image/*">""")
         #<label for="avatar-clear_id">remove</label>
        #<input type="checkbox" name="avatar-clear" id="avatar-clear_id"><br/>
        
        #input_html=super().render(name,value,attrs=None,**kwargs)

        #print(input_html,1000000000000000000000000000000000000)

        #image_html=mark_safe(f'<img src="{value.url}"/>')

#        return f'{input_html}'








class Form(forms.ModelForm):
    class Meta:
        model = story
        fields = ("title",'sound','image','caption')
        widgets={
            'caption':CKEditorWidget()
        }

       
        
       
        
        



