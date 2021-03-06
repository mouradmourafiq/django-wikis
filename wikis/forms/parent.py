# -*- coding: utf-8 -*-
from django.utils.translation import ugettext, ugettext_lazy as _
from django import forms
from wikis.fields import CommaSeparatedArticleField

class ParentForm(forms.Form):
    parent = CommaSeparatedArticleField(label=_(u"parent"), required=False)
    error_css_class = "error"
    def clean_assign(self):
        """
        Check that has assigned the cal to a friend
        """
        if self.cleaned_data['parent']:
            return self.cleaned_data['parent']
