import os

from django.conf import settings
from django.template.defaultfilters import addslashes

from webassets.filter import Filter, register_filter


class AngularFilter(Filter):
    name = 'angular'
    max_debug_level = None
    options = {
        'module': 'ANGULAR_TEMPLATE_MODULE'
    }

    def get_name(self, source_path):
        return os.path.relpath(source_path, os.path.dirname(settings.STATIC_ROOT))

    def input(self, _in, out, **kw):
        name = self.get_name(kw['source_path'])
        content = addslashes(_in.read().replace('\n', ''))
        str = u"\n$templateCache.put(\"{name}\",\"{content}\");".format(name=name, content=content)
        out.write(str)

    def concat(self, out, hunks, **kw):
        name = self.module
        out.write("angular.module('%s', []).run(['$templateCache', function($templateCache) {" % name)
        for hunk, name in hunks:
            out.write(hunk.data())
        out.write("}]);")

register_filter(AngularFilter)
