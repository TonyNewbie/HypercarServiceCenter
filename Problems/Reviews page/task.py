from django.shortcuts import render
from django.views import View


class ReviewView(View):
    reviews = ['Nice']  # List of reviews as plain strings

    def get(self, request, *args, **kwargs):
        return render(request, 'book/reviews.html', context={'reviews': self.reviews})
