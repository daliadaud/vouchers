from django.db import models


MAX_VOUCHER_USAGE = 3

VALUE = "VALUE"
PERCENT = "PERCENT"

VOUCHER_TYPE = [
    (VALUE, "Value"),
    (PERCENT, "Percent"),
]

class Voucher(models.Model):
    """

    1. Ideally it be better to have an 'is_active' field thus, deleted instances would be deactivated instead of removed entirely from DB.
    2. One could also tie a certain voucher for either to a certain product or user,
    this design would need us to have an M2M relationship to either User or Product table
    3. Validity of voucher could also be constraint by time
    4. There should be additional check if percentage discount is > 100%
    """


    code = models.CharField(
        max_length=24,
        unique=True,
    )
    value = models.FloatField(
    )

    value_type = models.CharField(
        choices=VOUCHER_TYPE,
        default=VALUE,
        max_length=8
    )
    usage_remainder = models.PositiveSmallIntegerField(
        default=MAX_VOUCHER_USAGE
    )

    def __str__(self):
        if self.value_type == VALUE:
            return f"${self.value}"
        return f" {int(self.value)}%"


    @classmethod
    def get_voucher(cls, code):
        try:
            voucher = Voucher.objects.get(code=code)
            if voucher.usage_remainder <= 0:
                return None
            return voucher
        except cls.DoesNotExist:
            return None

    def use_voucher(self):
        self.usage_remainder = self.usage_remainder - 1
        self.save()
