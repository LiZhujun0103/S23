import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydjango.settings")
    import django
    django.setup()

    from welkin import models

    lins = models.Appline.objects.all()
    b = []
    for x in lins:
        r = x.line_user.all()
        b.append(r)
    for i in b:
        for m in i:
            print(m.name)