from django.shortcuts import render

def post_list(request):
    return render(request,'posts/post_list.html',{})


def post_detail(request,slug):
    return render(request,'posts/post_detail.html',{})

