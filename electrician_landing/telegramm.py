import telepot as telepot

from django.shortcuts import redirect

from apps.landing.forms import TelegrammForm


token = ''
my_id = 
telegramBot = telepot.Bot(token)


def handle(request):
    if request.method == 'POST':
        form = TelegrammForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            name = form.cleaned_data['name']
            message = "*ЗАЯВКА С САЙТА*:" + "\n" + \
                      "*ТЕЛЕФОН*: " + str(phone) + "\n" + \
                      "От " + str(name)
            telegramBot.sendMessage(my_id, message, parse_mode="Markdown")
            return redirect('/')
        return redirect('/')
