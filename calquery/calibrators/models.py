from djongo import models
# Create your models here.

class BandDetail(models.Model):
    band = models.CharField(max_length=255)
    config_a = models.CharField(max_length=1)
    config_b = models.CharField(max_length=1)
    config_c = models.CharField(max_length=1)
    config_d = models.CharField(max_length=1)
    flux_jy = models.DecimalField(max_digits=10, decimal_places=2)
    uvmin_kl = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    uvmax_kl = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        abstract = True

class Calibrator(models.Model):
    iau_name = models.CharField(max_length=255)
    equinox = models.CharField(max_length=255)
    pc = models.CharField(max_length=255)
    ra = models.CharField(max_length=255)
    dec = models.CharField(max_length=255)
    pos_ref = models.CharField(max_length=255)
    alt_name = models.CharField(max_length=255, null=True, blank=True)
    bands = models.ArrayField(
        model_container=BandDetail,
    )
