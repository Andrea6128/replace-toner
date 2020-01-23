from django.shortcuts import render
from django.utils import timezone
from .models import Main
from .forms import MainForm
from django.core.mail import send_mail
from . import forms # new
from django.http import HttpResponse


# Create your views here.
def main_view(request):
    form = MainForm()
    return render(request, 'printers/main_view.html', {'form': form})

def subscribe(request):
    # set variables from dict sent in POST by pressing button
    viewsRoomNumber = request.POST['roomNumber']
    viewsPrinterName = request.POST['printerName']
    viewsTonerColor = request.POST['tonerColor']

    # set additional variables like printer assignment and time
    viewsRequestDate = timezone.now().strftime('%Y-%m-%d, %H:%M:%S')

    PRINTER_SETS = {
    'BIXOLON SRP-350plusIII': ['Thermal', 'Black&White', 'SRP 350 (roll)'],
    'Brother QL-820NWB': ['Dot-Matrix', 'Black&White', 'DK-22205 (label roll)'],
    'Canon iR-ADV 4025i': ['Laser', 'Color', '4792'],
    'Canon iR-ADV C3530 III': ['Laser', 'Color', 'C-EXV-49 family'],
    'Canon iR-ADV C5030': ['Laser', 'Color', 'C-EXV-49 family'],
    'Canon IRA3': ['Laser', 'Color', 'CRG-828'],
    'EPSON L1800': ['Ink', 'Color', 'T6641'],
    'EPSON WF-C5710': ['Ink', 'Color', 'T9441'],
    'EPSON WP-M4095': ['Ink', 'Black&White', '7441XL-P'],
    'KONICA MINOLTA bizhub C224e': ['Laser', 'Color', 'TN-321K'],
    'Kyocera ECOSYS M2040dn': ['Laser', 'Black&White', 'TK-1160'],
    'Kyocera ECOSYS M6526cdn': ['Laser', 'Color', 'TK-5xx family'],
    'Kyocera ECOSYS M6526cidn': ['Laser', 'Color', 'TK-5xx family'],
    'Kyocera ECOSYS M6235cidn': ['Laser', 'Color', 'TK-5xx family'],
    'Kyocera ECOSYS M6526dn': ['Laser', 'Color', 'TK-5xx family'],
    'Kyocera ECOSYS P6035cdn': ['Laser', 'Color', 'TK-5xx family'],
    'Kyocera M2035dn': ['Laser', 'Black&White', 'TK-1170'],
    'Kyocera TASKalfa 3252ci': ['Laser', 'Color', 'TK-8335'],
    'Kyocera TASKalfa 356ci': ['Laser', 'Color', 'Tk-5205'],
    'RICOH Aficio MP 2852': ['Laser', 'Color', '84024 (válec)'],
    'RICOH Aficio SP 3410dn': ['Laser', 'Black&White', '4510'],
    'RICOH Aficio SP 3510dn': ['Laser', 'Color', '4500'],
    'RICOH MP 2501': ['Laser', 'Black&White', '841925 (válec)'],
    'RICOH SP 3600DN': ['Laser', 'Black&White', '407340'],
    'Xerox Phaser 3300MFP': ['Laser', 'Color', '108 R 00796'],
    'Xerox Phaser 3435': ['Laser', 'Black&White', '186 R 01415'],
    'Xerox Workcentre 5225': ['Laser', 'Black&White', 'R 01306'],
    }

    # compare printer name got by POST with PRINTER_SETS dict and assign corresponding values
    for getKeyValue in PRINTER_SETS:
        if getKeyValue == viewsPrinterName:
            value = PRINTER_SETS.get(viewsPrinterName)
            viewsPrinterType = value[0]
            viewsPrinterColor = value[1]
            viewsTonerName = value[2]

    # if POST happened (button pressed), send email filled by data provided
    if request.method == 'POST':
        subject = 'ReplaceToner: místnost ' + str(viewsRoomNumber)
        message = """
            <html>
            <p>
              <strong>Požadavek na výměnu toneru</strong>
            </p>
              <ul>
                <li>Číslo místnosti: <strong>""" + str(viewsRoomNumber) + """</strong></li>
                <li>Název tiskárny: <strong>""" + str(viewsPrinterName) + """</strong></li>
                <li>Typ tiskárny: """ + str(viewsPrinterType) + """</li>
                <li>Barva: """ + str(viewsPrinterColor) + """</li>
                <li>Název toneru: <strong>""" + str(viewsTonerName) + """</strong></li>
                <li>Barva toneru: <strong>""" + str(viewsTonerColor) + """</strong></li>
              </ul>
              Požadavek vygenerován """ + str(viewsRequestDate) + """ aplikací ReplaceToner.
            </html>
        """
        from_email = 'replace-toner@company.com'
        recepient = ['--ENTER--YOUR--EMAIL--HERE--']
        send_mail(subject, message, from_email, recepient, fail_silently=False, html_message=message)
        return render(request, 'printers/success.html', {'viewsRoomNumber': viewsRoomNumber, 'viewsPrinterName': viewsPrinterName, 'viewsTonerColor': viewsTonerColor })
    else:
        return HttpResponse('Not sent :(')
