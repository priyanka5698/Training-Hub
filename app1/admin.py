from django.contrib import admin
from . import models
from . models import Regform1,ContactUs,Assignment,PythonTask,PLSQLTask,DjangoTask,NodeJSTask

# Register your models here.
admin.site.register(Regform1)
admin.site.register(ContactUs)
admin.site.register(Assignment)
admin.site.register(PythonTask)
admin.site.register(PLSQLTask)
admin.site.register(DjangoTask)
admin.site.register(NodeJSTask)
