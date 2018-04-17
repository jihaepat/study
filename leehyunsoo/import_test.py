import os,sys

DEPLOYMENT_LEVEL = os.environ.setdefault("DEPLOYMENT_LEVEL", "staging")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jtelips.settings_{dlevel}".format(dlevel=DEPLOYMENT_LEVEL))
# sys.path.append('/home/leehyunsoo/jtelips')


def first_sentry_log():
    from base.models import Model
    f = Model.objects.first()
    print(f)

if __name__ == '__main__':
    import django
    django.setup(set_prefix=False)

    first_sentry_log()