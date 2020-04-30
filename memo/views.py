from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from .forms import MemoForm
from django.views.decorators.http import require_POST


def index(request):
    """メモ一覧"""
    memos = Memo.objects.all().order_by('created_date')
    return render(request, 'memo/index.html', {'memos': memos})


def detail(request, memo_id):
    """メモ詳細"""
    memo = get_object_or_404(Memo, id=memo_id)
    return render(request, 'memo/detail.html', {'memo': memo})


def add_memo(request):
    """メモ追加"""
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('memo:index')
    else:
        form = MemoForm
    return render(request, 'memo/add_memo.html', {'form': form })


@require_POST # request.method=GET の時は実行されない
def del_memo(request, memo_id):
    """メモ削除"""
    memo = get_object_or_404(Memo, id=memo_id)
    memo.delete()
    return redirect('memo:index')


def mod_memo(request, memo_id):
    """メモ編集"""
    memo = get_object_or_404(Memo, id=memo_id)
    if request.method == "POST":
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('memo:index')
    else:
        form = MemoForm(instance=memo)
    return render(request, 'memo/mod_memo.html', {'form': form, 'memo': memo})
