
from django.urls import reverse_lazy
from switch.models import Switch
from django.contrib.messages.views import SuccessMessageMixin
from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.utils import timezone


class CadastroSw(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('denied')
    group_required = [u'adm']
    model = Switch
    fields = ['hostname', 'ip']
    template_name = 'switch/cadastro.html'
    success_url = reverse_lazy('lista_sw')
    success_message = 'Switch cadastrado com sucesso!'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.data = timezone.now()
        return super(CadastroSw, self).form_valid(form)

class ListaSw(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('denied')
    group_required = [u'suporte', u'adm']
    model = Switch
    template_name = 'switch/lista.html'
    paginate_by = 5

    def get_queryset(self):
        sw_nome = self.request.GET.get('search')

        if sw_nome:
            sw = Switch.objects.filter(hostname__icontains=sw_nome)

        else:
            sw = Switch.objects.all()

            return sw
class EditaSw(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('denied')
    group_required = [u'adm']
    model = Switch
    fields = ['hostname', 'ip']
    template_name = 'switch/cadastro.html'
    success_url = reverse_lazy('lista_sw')
    success_message = 'Switch atualizado!!'
