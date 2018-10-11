from django.db import models


class Bbs(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=20, blank=True, default='')
    pw = models.CharField(max_length=12, blank=True, default='')
    content = models.TextField()

    class Meta:
        ordering = ('created',)


class Clients(models.Model):
    name = models.CharField(max_length=20)
    money = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    memo = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    tax_reg_no = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


class Events(models.Model):
    client = models.ForeignKey(Clients, models.DO_NOTHING)
    category = models.IntegerField()
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    unit_price = models.IntegerField()
    score = models.IntegerField()
    status = models.IntegerField()
    status_comment = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255)
    discount_price = models.CharField(max_length=255)
    hospital_name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    banner_image = models.CharField(max_length=255)
    detail_image = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    side_effect = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    view_count = models.PositiveIntegerField()
    first_lived_at = models.DateTimeField(blank=True, null=True)
    last_lived_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'




