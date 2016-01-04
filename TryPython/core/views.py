# coding: utf-8

import json
from StringIO import StringIO
from django.core.management import call_command
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from models import Step


class IndexView(TemplateView):
    template_name = "main.html"


class EvalView(View):

    def post(self, request):
        to_eval = request.POST.get("toEval")

        namespace = request.session.get('namespace', "{}")

        out = StringIO()
        call_command("eval", to_eval, namespace, stdout=out)
        values = json.loads(out.getvalue())
        out, namespace, err = values['out'], values[
            'namespace'], values['error']

        request.session['namespace'] = namespace
        return JsonResponse({'out':  out, 'err': err})


class StepView(View):

    def post(self, request):
        step_number = request.POST.get('step')
        step = get_object_or_404(Step, pk=int(step_number))
        return JsonResponse(step.to_dict())
