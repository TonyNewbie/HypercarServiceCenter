from django.views import View
from django.http.response import HttpResponse, Http404
from django.shortcuts import redirect, render


# Common queue for service center
service_queue = {'change_oil': [], 'inflate_tires': [], 'diagnostic': []}
change_oil_time = 2
inflate_tires_time = 5
diagnostic_time = 30


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(View):
    def get(self, request, *args, **kwargs):
        menu = ('<ul>'
                '<li><a target="_blank" href="/get_ticket/change_oil">Change oil</a></li>'
                '<li><a target="_blank" href="/get_ticket/inflate_tires">Inflate tires</a></li>'
                '<li><a target="_blank" href="/get_ticket/diagnostic">Get diagnostic test</a></li>'
                '</ul>')
        return HttpResponse(menu)


class GetTicketView(View):
    ticket_num = 1

    def get(self, request, service_type, *args, **kwargs):
        if service_type == 'change_oil':
            waiting_time = len(service_queue['change_oil']) * change_oil_time
            service_queue['change_oil'].append(GetTicketView.ticket_num)
        elif service_type == 'inflate_tires':
            waiting_time = len(service_queue['change_oil']) * change_oil_time \
                           + len(service_queue['inflate_tires']) * inflate_tires_time
            service_queue['inflate_tires'].append(GetTicketView.ticket_num)
        elif service_type == 'diagnostic':
            waiting_time = len(service_queue['change_oil']) * change_oil_time \
                           + len(service_queue['inflate_tires']) * inflate_tires_time\
                           + len(service_queue['diagnostic']) * diagnostic_time
            service_queue['diagnostic'].append(GetTicketView.ticket_num)
        else:
            raise Http404
        ticket_info = (f'<div>Your number is {GetTicketView.ticket_num}</div>'
                       f'<div>Please wait around {waiting_time} minutes</div>')
        GetTicketView.ticket_num += 1
        return HttpResponse(ticket_info)


ticket_id = -1


class OperatorView(View):
    def get(self, request, *args, **kwargs):
        oil_number = len(service_queue["change_oil"])
        tires_number = len(service_queue["inflate_tires"])
        diagnostics_number = len(service_queue["diagnostic"])
        return render(request, 'process.html', context={'oil_number': oil_number, 'tires_number': tires_number,
                                                        'diagnostics_number': diagnostics_number})

    def post(self, request, *args, **kwargs):
        global ticket_id
        if service_queue['change_oil']:
            ticket_id = service_queue['change_oil'].pop(0)
        elif service_queue['inflate_tires']:
            ticket_id = service_queue['inflate_tires'].pop(0)
        elif service_queue['diagnostic']:
            ticket_id = service_queue['diagnostic'].pop(0)
        else:
            ticket_id = -1
        return redirect(f'/next')


class NextView(View):
    global ticket_id

    def get(self, request, *args, **kwargs):
        if ticket_id == -1:
            return HttpResponse('<div>Waiting for the next client</div>')
        else:
            return HttpResponse(f'<div>Next ticket #{ticket_id}</div>')
