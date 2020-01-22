from django.db import models
from django.utils import timezone


# Create your models here.
class Main(models.Model):
    # generates room numbers to choose from:
    fillRooms = []
    generateRooms = range(1, 418)
    for room in generateRooms:
        fillRooms.append((room, (str(room))))
        ROOMS = fillRooms

    PRINTER = [
    ('BIXOLON SRP-350plusIII', 'BIXOLON SRP-350plusIII'),
    ('Brother QL-820NWB', 'Brother QL-820NWB'),
    ('Canon iR-ADV 4025i', 'Canon iR-ADV 4025i'),
    ('Canon iR-ADV C3530 III', 'Canon iR-ADV C3530 III'),
    ('Canon iR-ADV C5030', 'Canon iR-ADV C5030'),
    ('Canon IRA3', 'Canon IRA3'),
    ('EPSON L1800', 'EPSON L1800'),
    ('EPSON WF-C5710', 'EPSON WF-C5710'),
    ('EPSON WP-M4095', 'EPSON WP-M4095'),
    ('KONICA MINOLTA bizhub C224e', 'KONICA MINOLTA bizhub C224e'),
    ('Kyocera ECOSYS M2040dn', 'Kyocera Ecosys M2040dn'),
    ('Kyocera ECOSYS M6235cidn', 'Kyocera ECOSYS M6235cidn'),
    ('Kyocera ECOSYS M6526cdn', 'Kyocera ECOSYS M6526cdn'),
    ('Kyocera ECOSYS M6526cidn', 'Kyocera ECOSYS M6526cidn'),
    ('Kyocera ECOSYS M6526dn', 'Kyocera ECOSYE M6526dn'),
    ('Kyocera ECOSYS P6035cdn', 'Kyocera ECOSYS P6035cdn'),
    ('Kyocera M2035dn', 'Kyocera M2035dn'),
    ('Kyocera TASKalfa 3252ci', 'Kyocera TASKalfa 3252ci'),
    ('Kyocera TASKalfa 356ci', 'Kyocera TASKalfa 356ci'),
    ('RICOH Aficio MP 2852', 'RICOH Aficio MP 2852'),
    ('RICOH Aficio SP 3410DN', 'RICOH Aficio SP 3410DN'),
    ('RICOH Aficio SP 3510dn', 'RICOH Aficio SP 3510dn'),
    ('RICOH MP 2501', 'RICOH MP 2501'),
    ('RICOH SP 3600DN', 'RICOH SP 3600DN'),
    ('Xerox Phaser 3300MFP', 'Xerox Phaser 3300MFP'),
    ('Xerox Phaser 3435', 'Xerox Phaser 3435'),
    ('Xerox Workcentre 5225', 'Xerox Workcentre 5225'),
    ]

    TONER_COLOR = [
    ('C', 'Cyan'),
    ('M', 'Magenta'),
    ('Y', 'Yellow'),
    ('K', 'Black')
    ]

    roomNumber = models.DecimalField(max_digits=3, decimal_places=0, verbose_name=('Číslo místnosti'), choices=ROOMS)
    printerName = models.CharField(max_length=30, verbose_name=('Typ tiskárny'), choices=PRINTER)
    tonerColor = models.CharField(max_length=1, verbose_name=('Barva toneru'), choices=TONER_COLOR, default="K") # CMYK

    # this doesn't need to be here:
    def __str__(self):
        return self.roomNumber, self.printerName, self.tonerColor

    def submit(self):
        self_submitted_date = timezone.now()
        self.save()
