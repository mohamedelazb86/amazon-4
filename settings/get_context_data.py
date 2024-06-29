from .models import Setting

def context_data(request):
    data=Setting.objects.last()
    return{'context_data':data}