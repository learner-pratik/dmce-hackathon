from django.contrib import admin
from .models import login,User,Restaurants,Visits,Orders,Res_Click,Posts

admin.site.register(login)
admin.site.register(User)
admin.site.register(Restaurants)
admin.site.register(Visits)
admin.site.register(Orders)
admin.site.register(Res_Click)
admin.site.register(Posts)