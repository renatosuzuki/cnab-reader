from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from .models import UploadFile

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']

        cnab_file = UploadFile.objects.create(cnab_file=file)
        cnab_file.save()
        
        return HttpResponse('The name of the file is ' + str(file))
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})