from django.shortcuts import redirect
from django.views import View


class TodoView(View):
    all_todos = []

    def post(self, request, *args, **kwargs):
        doing = request.POST.get('todo')
        if doing not in self.all_todos:
            self.all_todos.append(doing)
        return redirect('/')
