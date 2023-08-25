from django.shortcuts import render
from .forms import ReviewForm
from .classification import make_prediction
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = make_prediction([form.data['review_text']])[0]
            label = 'Positive' if rating >= 7 else 'Negative'
            return render(request, 'main/index.html', {'form': form,
                                                       'rating': rating,
                                                       'label': label})
    else:
        form = ReviewForm()
    return render(request, 'main/index.html')

