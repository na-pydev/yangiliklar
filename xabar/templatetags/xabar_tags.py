from django import template
from xabar.models import Xabar
register = template.Library()

@register.simple_tag(name="kop_oqilgan")
def eng_kop_oqilgan():
    oqilgan_list = Xabar.objects.all().order_by('-korildi')[:4]
    return oqilgan_list