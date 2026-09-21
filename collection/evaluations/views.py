from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_http_methods

from .services import evaluate_query


@never_cache
@login_required
@require_http_methods(["GET", "POST"])
def index(request):
    query = ""
    error = ""
    submitted = False
    results = []

    if request.method == "POST":
        query = request.POST.get("query", "").strip()
        if not query:
            error = "请先输入一个问题。"
        elif len(query) > 5000:
            error = "问题不能超过 5000 个字符。"
        else:
            results = evaluate_query(query)
            submitted = True

    context = {
        "query": query,
        "error": error,
        "submitted": submitted,
        "results": results,
    }
    return render(request, "evaluations/index.html", context)
