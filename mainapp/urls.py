from rest_framework.routers import DefaultRouter as DR

from mainapp.views import TodoView

router = DR()

router.register('todo', TodoView)

urlpatterns = [

]

urlpatterns += router.urls