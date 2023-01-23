from django import forms
from app.models import User_Task


class VeiwForm(forms.ModelForm):
    class Meta:
        model = User_Task
        fields = ('author', 'user_file', 'file_status')
    def as_p(self):
        return self._html_output(
            normal_row=u'<p%(html_class_attr)s>%(label)s</p> %(field)s%(help_text)s',
            error_row=u'%s',
            row_ender='</p>',
            help_text_html=u' <span class="helptext">%s</span>',
            errors_on_separate_row=True)
