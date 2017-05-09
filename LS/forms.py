from django import forms
from codemirror import CodeMirrorTextarea


codemirror_widget = CodeMirrorTextarea(
    mode="python",
    config={
        'fixedGutter': True,
    },
)

class HtmlEditor(forms.Textarea):
    def __init__(self, *args, **kwargs):
        super(HtmlEditor, self).__init__(*args, **kwargs)
        self.attrs['class'] = 'html-editor'

    class Media:
        css = {
            'all': (
                '/static/js/codemirror/lib/codemirror.css',
            )
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.25.2/codemirror.js',
            'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.25.2/mode/python/python.js',
            '/static/js/init_ce.js'
        )


class EditorForm(forms.Form):
    text = forms.CharField(widget=HtmlEditor(attrs={'style': 'width: 100%; height: 100%;'}))
    #forms.CharField(widget=AceWidget(mode='python', width="700px", height="300px"))
