from django.contrib import admin
from .models import IpMark, IpMarkNiceClasses, TblTims, TblNmpt, TblAvtor, TblSp, TblOtz,\
    TblBd, TblInv, TblPm, TblPobr, TblEvm, TblCel, TblTrz, TblRp, License

admin.site.register(IpMark)
admin.site.register(IpMarkNiceClasses)
admin.site.register(TblTims)
admin.site.register(TblNmpt)
admin.site.register(TblAvtor)
admin.site.register(TblSp)
admin.site.register(TblOtz)
admin.site.register(TblBd)
admin.site.register(TblInv)
admin.site.register(TblPm)
admin.site.register(TblPobr)
admin.site.register(TblEvm)
admin.site.register(TblCel)
admin.site.register(TblTrz)
admin.site.register(TblRp)
admin.site.register(License)