from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .models import Header

# Create your views here.


class HeaderListView(View):
    def get(self, request):
        headers = Header.objects.all().order_by('id')
        context = {'headers': headers}
        return render(request, 'main/headers.html', context)


class HeaderView(View):
    def get(self, request, pk):
        try:
            header = Header.objects.get(id=pk)
            context = {'header': header}
            return render(request, 'main/header.html', context)
        except:
            return render(request, 'main/error.html')


class HeaderCreateView(View):
    def get(self, request):
        return render(request, 'main/create_header.html')

    def post(self, request):
        header = Header.objects.create(
            title=request.POST.get('title')
        )
        header.save()
        return redirect(reverse('headers'))


class HeaderUpdateView(View):
    def get(self, request, pk):
        return render(request, 'main/update_header.html')

    def post(self, request, pk):
        header = Header.objects.get(id=pk)
        header.title = request.POST.get('title')
        header.save()
        return redirect(reverse('headers'))


class HeaderDeleteView(View):
    def get(self, request, pk):
        try:
            header = Header.objects.get(id=pk)
            return render(request, 'main/delete_header.html')
        except:
            return render(request, 'main/error.html')

    def post(self, request, pk):
        if 'positive' in request.POST:
            header = Header.objects.get(id=pk)
            header.delete()
        return redirect(reverse('headers'))
