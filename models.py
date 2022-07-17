
# Create your models here.
from django.db import models

class Plan(models.Model):
    plan_id = models.PositiveIntegerField()
    plan_name = models.CharField(max_length=200)
    amount_options = models.PositiveIntegerField()
    tenure_options= models.CharField(max_length=200)
    benefitPercentage=models.PositiveIntegerField()
    benefitType= models.CharField(max_length=200)
    product_type=models.CharField(max_length=200)

class Promotion(models.Model):
    plan = models.ForeignKey('Plan', on_delete=models.RESTRICT, null=True)
    number=models.PositiveIntegerField(required=False,default=1)
    time_period=models.PositiveIntegerField()
    PROMOTION_TYPE = (
        ('n', 'Number'),
        ('tp', 'Time Period'),
    )

    type = models.CharField(
        max_length=1,
        choices=PROMOTION_TYPE,
        blank=True,
        default='n',
        help_text='Type of Promotion',
    )
