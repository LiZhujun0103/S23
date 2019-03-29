from django.conf.urls import url
from crm.views import home, depart, user, maintion, account

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'index/', home.index, name='index'),
    url(r'login/', account.login, name='login'),
    url(r'depart/list/', depart.depart_list, name='depart_list'),
    url(r'maintions/list/', maintion.server_list, name='server_list'),
    url(r'user/list/', user.user_list, name='user_list'),
    url(r'user/add/', user.users, name='user_add'),
    url(r'maintions/add/', maintion.servers, name='server_add'),
    url(r'depart/add/', depart.depart_add, name='depart_add'),
    url(r'depart/edit/(\d+)', depart.depart_edit, name='depart_edit'),
    url(r'user/edit/(\d+)', user.users, name='user_edit'),
    url(r'maintions/edit/(\d+)', maintion.servers, name='server_edit'),
    url(r'depart/del/(\d+)', depart.depart_del, name='depart_del'),
    url(r'user/del/(\d+)', user.user_del, name='user_del'),
    url(r'maintions/del/(\d+)', maintion.server_del, name='server_del'),
]
