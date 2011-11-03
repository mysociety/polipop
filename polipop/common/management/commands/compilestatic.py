import subprocess

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        # First, call collectstatic as normal
        call_command('collectstatic', interactive=False)
        # Then compile any SCSS there to CSS
        subprocess.call([ 'sass', '--scss', '--update', '--style', 'compressed', settings.STATIC_ROOT ])
