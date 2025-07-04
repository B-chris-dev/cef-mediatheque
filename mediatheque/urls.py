"""
URL configuration for mediatheque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path
from bibliothecaire.views import add_borrower, update_book, update_bg, borrow_list, borrowers_list, media_list, add_book, add_dvd, \
    add_cd, \
    add_bg, update_cd, update_dvd, delete_media, delete_borrower, create_borrow
urlpatterns = [
    path('', media_list),
    path('addborrower/', add_borrower),
    path('borrowerslist/', borrowers_list),
    path('borrowlist/', borrow_list),
    path('createborrow/<int:id>/', create_borrow),
    path('addbook/', add_book),
    path('adddvd/', add_dvd),
    path('addcd/', add_cd),
    path('addbg', add_bg),
    path('updatebook/<int:id>/', update_book),
    path('updatedvd/<int:id>/', update_dvd),
    path('updatebg/<int:id>/', update_bg),
    path('updatecd/<int:id>/', update_cd),
    path('delete/<int:id>', delete_media),
    path('delete/<int:id>', delete_borrower),
    path('admin/', admin.site.urls),
]