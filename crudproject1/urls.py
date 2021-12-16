
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('ss/',views.add_show,name="addandshow"),
    path('',views.gives,name="gives"),
    path('delete/<int:id>/',views.deleteCrd,name="deletedata"),
    path('update/<int:id>/',views.updateCrd,name="updatedata"),
    path('search/', views.search, name="search"),

]


