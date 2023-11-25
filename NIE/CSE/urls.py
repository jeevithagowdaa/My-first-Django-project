from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def prodcts(request):
    return render(request, 'prodcts.html')

def service(request):
    return render(request, 'service.html')

def contacts(request):
    return render(request, 'contacts.html')

def aboutus(request):
    return render(request, 'aboutus.html')


from CSE.models import Sudent
def students(request):
    stu = Sudent.objects.all()
    context = {'stu': stu}
    return render(request, 'student.html', context)



from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

class Forms(CreateView):
    model = Sudent
    fields = "_all_"
    template_name = 'forms.html'
    success_url = '/'

class StudentList(ListView):
    model = Sudent
    template_name = 'stulist.html'

class StudentDetail(DetailView):
    model = Sudent
    template_name = 'studetail.html'

class StudentUpdate(UpdateView):
    model = Sudent
    fields = '_all_'
    template_name = 'stuupdate.html'
    success_url = '/'

class StudentDelete(DeleteView):
    model = Sudent
    template_name = 'studelete.html'
    success_url = '/'