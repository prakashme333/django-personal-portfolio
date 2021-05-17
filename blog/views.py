from django.shortcuts import render, get_object_or_404
from blog.models import Blog

# Create your views here.
def all_blogs(request):
   # by doing this only first 5 recent will be displayed
   # for all jst do objects.all()
   blog_count = Blog.objects.count
   blog = Blog.objects.order_by('-date')[:5]
   return render(request, 'blog/all_blogs.html', {'blogs':blog , 'blog_count':blog_count})


def detail(request,id):
   blog = get_object_or_404(Blog,pk=id)
   return render(request,'blog/detail.html',{'blog':blog})