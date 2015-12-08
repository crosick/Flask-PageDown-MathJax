from jinja2 import Markup
from flask import current_app


class _pagedown(object):
    def include_pagedown(self):
        return Markup('''
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.3/underscore-min.js"></script>
<script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>            
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/pagedown/1.0/Markdown.Converter.min.js"></script>
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/pagedown/1.0/Markdown.Sanitizer.min.js"></script>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    tex2jax: {
        inlineMath: [['$','$'], ['\\(','\\)']],
        displayMath: [["$$", "$$"], ["\\[","\\]"]]
    },
    "HTML-CSS": {
        availableFonts: ["STIX", "TeX"],
        linebreaks: { automatic: true },
        imageFont: null 
    }
});
</script>
''')

    def html_head(self):
        return self.include_pagedown()


class PageDown(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['pagedown'] = _pagedown()
        app.context_processor(self.context_processor)

    @staticmethod
    def context_processor():
        return {'pagedown': current_app.extensions['pagedown']}
