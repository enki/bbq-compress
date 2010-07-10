import os
os.environ['BBQ_SETTINGS_MODULE'] = 'bbq.settings'
from bbq.conf import settings
from compress.utils import needs_update, filter_css, filter_js
import sys

# force = options.get('force', False)
# verbosity = int(options.get('verbosity', 1))

force = True
verbosity = 4

for name, css in settings.COMPRESS_CSS.items():
    u, version = needs_update(css['output_filename'], 
        css['source_filenames'])

    if (force or u) or verbosity >= 2:
        msg = 'CSS Group \'%s\'' % name
        print msg
        print len(msg) * '-'
        print "Version: %s" % version

    if force or u:
        filter_css(css, verbosity)

    if (force or u) or verbosity >= 2:
        print

for name, js in settings.COMPRESS_JS.items():
    u, version = needs_update(js['output_filename'], 
        js['source_filenames'])

    if (force or u) or verbosity >= 2:
        msg = 'JavaScript Group \'%s\'' % name
        print msg
        print len(msg) * '-'
        print "Version: %s" % version

    if force or u:
        filter_js(js, verbosity)

    if (force or u) or verbosity >= 2:
        print
