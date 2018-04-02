from django.db.models import *
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class BaseModel(Model):
    def Meta(self):
        abstracte = True


class Snippet(BaseModel):
    created = DateTimeField(auto_now_add=True)
    title = CharField(max_length=100, blank=True, default='')
    code = TextField()
    linenos = BooleanField(default=False)
    language = CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = ForeignKey('auth.User', related_name='snippets', on_delete=True)
    highlighted = TextField()

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)
