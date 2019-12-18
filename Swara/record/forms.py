from django import forms
from record.models import Entry, Word

class Entryform(forms.ModelForm):
   title = forms.CharField(max_length=10)
   upload = forms.FileField()


   def clean(self):
      title, created = Word.objects.get_or_create(
         name=self.cleaned_data['title'],
      )
      self.cleaned_data['title'] = title
      return super(Entryform, self).clean()



   class Meta:
      model = Entry
      fields = ('title','upload')


