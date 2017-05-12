from django.conf.urls import url,include
from .views import (
                    BookCreate, 
                    BookUpdate, 
                    BookDelete,
                    BookDetailView,
                    BookListView
                    )
 
urlpatterns = [
    url(r'^$', BookListView.as_view(), name='book-list'),
    url(r'^(?P<pk>[0-9]+)/$', BookDetailView.as_view(), name='book-detail'),
    url(r'^add/$', BookCreate.as_view(), name='book-add'),
    url(r'^(?P<pk>[0-9]+)/update$', BookUpdate.as_view(), name='book-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', BookDelete.as_view(), name='book-delete'),
]