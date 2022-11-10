from django.forms import ModelForm
from .models import BooksModel,SimpleBook,TestBook
class TestBookForm(ModelForm):
    class Meta:
        model = TestBook
        fields = fields = '__all__'

class TestBookFormOne(ModelForm):
    class Meta:
        model = TestBook
        #fields = ['bookname', 'cover', 'price']
        fields = '__all__'