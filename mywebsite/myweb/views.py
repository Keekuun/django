from django.shortcuts import render
from django.http import HttpResponseRedirect
import logging
from .models import *
from .forms import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

logger = logging.getLogger('myweb.views')


# Create your views here.
# 全局变量
def global_var(request):
    avatar = User.objects.values('avatar')[-1]
    return locals()


# 主页
def main(request):
    try:
        article_list = Article.objects.all()
        article_list = getPage(request, article_list)
    except Exception as e:
        print(e)
        logger.error(e)
    return render(request, 'main.html', locals())


# 分页代码
def getPage(request, article_list):
    paginator = Paginator(article_list, 3)
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list


# 文章详情
def article(request):
    try:
        # 获取文章id
        id = request.GET.get('id', None)
        try:
            # 获取文章信息
            article = Article.objects.get(pk=id)
        except Article.DoesNotExist:
            return render(request, 'failure.html', {'reason': '没有找到对应的文章'})
    except Exception as e:
        print(e)
        logger.error(e)
    return render(request, 'article.html', locals())



def add_article(request):
    add_article_form = AddArticleForm(request.POST)
    if add_article_form.is_valid():
        add_article_form.save()
        return HttpResponseRedirect('/')
    else:
        add_article_form = AddArticleForm()
        return render(request, 'add_article.html', locals())


# 社区小广场
def community(request):
    return render(request, 'community.html', locals())