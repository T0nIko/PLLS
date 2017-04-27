from django import forms
from codemirror import CodeMirrorTextarea

codemirror_widget = CodeMirrorTextarea(
    config={
        'fixedGutter': True,
    },
)


class EditorForm(forms.Form):
    text = forms.CharField(widget=codemirror_widget)
