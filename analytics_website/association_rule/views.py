from django.shortcuts import render
from django.views.generic import TemplateView

from association_rule.forms import AssociationRuleForm

from association_rule.AssociationRule import AssociationRulesAlgo

FILE_PATH = 'S:/B&M/Analytics & Store Segmentation/Ad Hoc Analyses/Association Rule - 2017 Halloween/'

class AssociationRuleView(TemplateView):
	template_name = 'association_rule/model.html'
	AR_output = 'association_rule/ar_output.html'
	
	def get(self,request):
		form = AssociationRuleForm()
		return render(request, self.template_name, {'form':form})
		
	def post(self, request):
		form = AssociationRuleForm(request.POST)
		if form.is_valid():
			Dept = form.cleaned_data['Department']
			Class = form.cleaned_data['Class']
			
		else:
			Dept = 'Not processed Correctly'
			Class = 'Not processed'
		assRules = AssociationRulesAlgo(FILE_PATH,support=0.007,lift=1, confidence=0.1)
		rules = assRules.getRules()
		rules_list = rules.values.tolist()
		count = rules.shape[0]
		args = {'rules_list':rules_list,'count':count}
		return render(request, self.AR_output,args)