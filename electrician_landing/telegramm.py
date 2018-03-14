import telepot as telepot

from django.shortcuts import redirect

from apps.landing.forms import TelegrammForm


token = '469723110:AAEewGk34x63M7tzKYiIQhohvx86ykR6tfU'
my_id = 521853533
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
            telegramBot.sendMessage(521853533, message, parse_mode="Markdown")
            return redirect('/')
        return redirect('/')