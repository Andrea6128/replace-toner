# replace-toner

ReplaceToner app for printer toner replace user request.
A user enters a corresponding room number with a printer, name of printer and an empty toner color (Black is default).
The 'Send Request' button generates an email with additional data about the selected printer like toner name
and type of the printer. The email is sent to a fixed email address (printer admin staff's email address).

To make it work you need to modify settings.py and provide your own smtp server credentials or use free sendgrid ones. Next, you must fill your working email address in the views.py send_mail section. At last,  modify your printer and room data in models.py AND views.py eventually.
