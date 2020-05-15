from django.shortcuts import redirect
from django.views import View


class TodoView(View):
    all_todos = []

    def post(self, request, *args, **kwargs):
        doing = request.POST.get('todo')
        important = request.POST.get('important')
        if doing not in self.all_todos:
            if important:
                self.all_todos.insert(0, doing)
            else:
                self.all_todos.append(doing)
        return redirect('/')
