from django.db import models
from django.utils import timezone


# Create your models here.
class Main(models.Model):
    # makes tuples from room list
    tupleRooms = []
    normalRooms = [1,2,3,4,5,6,7,8,9,10,11,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,
            102,104,105,106,107,108,109,110,111,112,113,114,115,116,118,119,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,
            201,202,203,204,205,206,207,208,209,210,211,212,215,216,217,218,219,221,222,223,224,226,227,228,229,290,232,233,234,235,236,237,238,239,240,241,242,
            301,306,307,308,309,310,311,312,313,314,315,316,317,318,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,349,
            406,407,410,411]
    for room in normalRooms:
        tupleRooms.append((room, (str(room))))
        ROOMS = tupleRooms

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
    ('Kyocera ECOSYS M2040dn', 'Kyocera ECOSYS M2040dn'),
    ('Kyocera ECOSYS M6235cidn', 'Kyocera ECOSYS M6235cidn'),
    ('Kyocera ECOSYS M6526cdn', 'Kyocera ECOSYS M6526cdn'),
    ('Kyocera ECOSYS M6526cidn', 'Kyocera ECOSYS M6526cidn'),
    ('Kyocera ECOSYS M6526dn', 'Kyocera ECOSYS M6526dn'),
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
    ('Cyan', 'Cyan'),
    ('Magenta', 'Magenta'),
    ('Yellow', 'Yellow'),
    ('Black', 'Black')
    ]

    roomNumber = models.DecimalField(max_digits=3, decimal_places=0, verbose_name=('Číslo místnosti'), choices=ROOMS)
    printerName = models.CharField(max_length=30, verbose_name=('Typ tiskárny'), choices=PRINTER)
    tonerColor = models.CharField(max_length=7, verbose_name=('Barva toneru'), choices=TONER_COLOR, default="Black") # CMYK

    # this doesn't need to be here:
    def __str__(self):
        return self.roomNumber, self.printerName, self.tonerColor

    def submit(self):
        self_submitted_date = timezone.now()
        self.save()
