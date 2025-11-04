from django.db import models
from django.utils.text import camel_case_to_spaces

class BaseMeta(models.base.ModelBase):
    def __new__(cls, name, bases, attrs, **kwargs):

        meta = attrs.get('Meta')

        if meta:
            print(f"BaseMeta: {name} has meta")

            if (
                not hasattr(meta, 'db_table')
                and not getattr(meta, 'abstract', False)
            ):
                print(f"BaseMeta: {name} is concrete and has no db_table meta")
                meta.db_table = name.lower()
            else:
                print(f"BaseMeta: {name} is abstract or has db_table meta")
        else:
            print(f"BaseMeta: {name} has no meta")
            class Meta:
                db_table = name.lower()
            attrs['Meta'] = Meta

        return super().__new__(cls, name, bases, attrs, **kwargs)

class BaseModel(models.Model, metaclass=BaseMeta):
    class Meta:
        abstract = True
