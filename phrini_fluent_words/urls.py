from django.urls import path
from . import views

urlpatterns = [
    # WordGroup URLs
    path('word-groups/public/', views.public_word_group_list, name='public-word-group-list'),
    path('word-groups/private/', views.private_word_group_list, name='private-word-group-list'),
    path('word-groups/<int:pk>/random/', views.private_word_group_list, name='random_word_from_group'),
    path('words/<int:word_id>/similarity/', views.word_similarity, name='word-similarity'),
]
