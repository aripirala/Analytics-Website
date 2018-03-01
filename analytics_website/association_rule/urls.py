from django.conf.urls import url
from  association_rule.views import AssociationRuleView

urlpatterns = [
				url(r'^$', AssociationRuleView.as_view(), name='AssociationRuleView')]