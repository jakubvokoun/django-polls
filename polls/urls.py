from django.urls import path

from .views import index, detail, results, vote


urlpatterns = [
    # ex: /polls/
    path('', index, name='polls-index'),
    # ex: /polls/5/
    path('<int:question_id>/', detail, name='polls-detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', results, name='polls-results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', vote, name='polls-vote'),
]