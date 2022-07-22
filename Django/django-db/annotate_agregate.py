"""
--------------------------------------------------------------------------------------------------
sources:
    https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
    https://docs.djangoproject.com/en/4.0/ref/models/querysets/#annotate
    https://docs.djangoproject.com/en/4.0/ref/models/querysets/#aggregate
    https://docs.djangoproject.com/en/4.0/ref/models/querysets/#alias


    https://django.fun/docs/django/ru/4.0/topics/db/aggregation/

    https://docs.djangoproject.com/en/4.0/ref/models/querysets/#id6

    об агрегации
    https://www.ibm.com/docs/ru/spss-statistics/25.0.0?topic=SSLVMB_25.0.0/spss/base/idh_aggr.html

Если вкратце то:


--- annotate:
       - many2many:
         (some_count=Count('some_field_many2many')):
                делает один SQL запрос используя LEFT OUTER JOIN


---------------------------------------------------------------------------------------------------
"""
