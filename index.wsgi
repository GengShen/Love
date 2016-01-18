import sys
import os.path
import sae
import django.core.handlers.wsgi
root=os.path.dirname(__file__)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
sys.path.append(os.path.join(root,'requests'))
sys.path.append(os.path.join(root,'mysite'))

application=sae.create_wsgi_app(django.core.handlers.wsgi.WSGIHandler())