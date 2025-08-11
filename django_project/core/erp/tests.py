
from core.erp.models import Type


new_type = Type()
new_type.name = "Gerente"
new_type.save()


# listar

# select * from table
Type.objects.all()





