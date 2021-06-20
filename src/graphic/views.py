from django.shortcuts import render, redirect
from django.views.generic import ListView

# Create your views here.
from graphic.form import GraphicModuleForm
from graphic.models import Graphic
#from graphic.tasks import plot
from graphic.utils import plot


def test(request):
    if request.method == 'POST':
        print(request.POST)
        form = GraphicModuleForm(request.POST)
        if form.is_valid():
            form.save()
            plot(form.cleaned_data.get('function'), form.cleaned_data.get('bot_interval'),
                              form.cleaned_data.get('top_interval'), form.cleaned_data.get('step'))
            return redirect('/')
        return render(request, 'graphic\List.html', {'form': form})

    form = GraphicModuleForm()
    objects = Graphic.objects.all()
    return render(request, 'graphic\List.html', {'form': form, 'objects': objects})


class RouteListView(ListView):
    model = Graphic
    template_name = 'graphic/List.html'
