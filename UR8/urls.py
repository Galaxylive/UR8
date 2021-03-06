from django.conf.urls import url
from . import views
handler404 = views.handler404
handler500 = views.handler500
handler403 = views.handler403
handler400 = views.handler400
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^sign-up/$', views.signup_view, name="sign_up"),
    url(r'^sign-in/$', views.signin_view, name="sign_in"),
    url(r'^sign-out/$', views.signout_view, name="sign_out"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^edit_avatar/$', views.edit_avatar, name="edit_avatar"),
    url(r'^reset-pwd/$', views.reset_pwd, name="reset_pwd"),
    url(r'^upload_video/$', views.upld_vid, name="upld_vid"),
    url(r'^uploaded_video/$', views.view_vid, name="view_vid"),
    url(r'^delete-video/(\d+)/$', views.del_vid, name="del_vid"),
    url(r'^sub/(\d+)/$', views.sub, name="sub"),
    url(r'^del_subscribes/(\d+)/$', views.del_subscribes, name="del_subscribes"),
    url(r'^del-notifications/(\d+)/$', views.del_notifications, name="del_notifications"),
    url(r'^update-video/(\d+)/$', views.updt_vid, name="updt_vid"),
    url(r'^search_video/$', views.search_vid, name="search_vid"),
    url(r'^view-video/(\d+)/$', views.s_vid, name="s_vid"),
    url(r'^rated-video/(\d+)/$', views.rated_video, name="rated_video"),
    url(r'^liked-review/(\d+)/(\d+)/$', views.rated_review, name="rated_review"),
    url(r'^disliked-review/(\d+)/(\d+)/$', views.rated_review2, name="rated_review2"),
    url(r'^delete-review/(\d+)/$', views.delete_review, name="delete_review"),
    url(r'^edit-review/(\d+)/(\d+)/$', views.edit_review, name="edit_review"),
    url(r'^channel/(\w+)/$', views.channel, name="channel"),
    url(r'^notifications/$', views.notifications, name="notifications"),
    url(r'^subscribes/$', views.subscribes, name="subscribes"),
    url(r'^channels/$', views.channels, name="channels"),
]
