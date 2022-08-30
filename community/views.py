from distutils.cmd import Command
import math
import os
from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponseRedirect
from community.models import Board, Comment
from urllib.parse import urlparse

# Create your views here.
def list(request):
    boardCount = Board.objects.count() # 레코드 카운드

    try:
        start=int(request.GET['start']) # 레코드 시작 번호 [start:end]
    except:
        start = 0

    page_size = 10 # 한 화면에 보여지는 레코드 수
    page_list_size = 10 # 보여지는 페이지 개수
    end = start+page_size # 페이지 끝
    total_page = math.ceil(boardCount/page_size) # 페이지 개수
    current_page = math.ceil((start+1)/page_size) # 현재 페이지
    start_page = math.floor((current_page-1)/page_list_size)*page_list_size+1 # 시작 페이지
    end_page = start_page + page_list_size - 1 # 마지막 페이지
    if total_page < end_page:
        end_page = total_page
    
    # 이전 페이지
    if start_page >= page_list_size:
        prev_list = (start_page - 2 * page_size)
    else:
        prev_list = 0
    
    # 다음 페이지
    if total_page > end_page:
        next_list = end_page*page_size
    else:
        next_list = 0

    boardList = Board.objects.all()
    commentList = Comment.objects.all()

    links = []
    for i in range(start_page, end_page + 1):
        page = (i - 1) * page_size
        links.append("<a href='?start="+ str(page) + "'>"+ str(i) + "</a>")

    return render(request, 'list.html',
    {'boardList': boardList, 'commentCount': len(commentList), 'boardCount': len(boardList), 'range':range(start_page-1, end_page),
    'start_page': start_page, 'end_page': end_page, 'page_list_size':page_list_size, 'total_page':total_page,
    'prev_list':prev_list, 'next_list':next_list, 'links':links})

def write(request):
    return render(request, 'write.html')

def insert(request):
    row = Board(title=request.POST['title'],content=request.POST['content'])
    row.save()
    return redirect('/')

def detail(request):
    id=request.GET['idx']
    row = Board.objects.get(idx=id)
    commentList=Comment.objects.filter(board_idx=id).order_by('idx')
    return render(request, 'detail.html', {'row':row, 'commentList': commentList})

def update(request):
    id = request.POST['idx']
    row_new = Board(idx=id, writer=request.POST['writer'], title=request.POST['title'],content=request.POST['content'])
    row_new.save()
    return redirect('/')

def delete(request):
    id = request.POST['idx']
    Board.objects.get(idx=id).delete()
    return redirect('/')

def reply_insert(request):
    id = request.POST['idx']
    row = Comment(board_idx=id, writer=request.POST['writer'],content=request.POST['content'])
    row.save()
    return HttpResponseRedirect('detail?idx='+id)