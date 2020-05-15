from django.shortcuts import redirect, Http404
from django.views import View


class TodoView(View):
    all_todos = []

    def delete(self, request, doing, *args, **kwargs):
        if doing in self.all_todos:
            self.all_todos.remove(doing)
            return redirect('/')
        raise Http404
