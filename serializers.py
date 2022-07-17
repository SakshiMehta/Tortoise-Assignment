from rest_framework import serializers
from .models import Plan

class PlanSerializer(serializers.ModelSerializer):
    plan_id = serializers.PositiveIntegerField()
    plan_name = serializers.CharField(max_length=200)
    amount_options = serializers.PositiveIntegerField(required=True, default=100)
    tenure_options= serializers.CharField(max_length=200)
    benefitPercentage=serializers.PositiveIntegerField(required=False, default=0)
    benefitType= serializers.CharField(max_length=200)
    product_type=serializers.CharField(max_length=200)

    class Meta:
        model = Plan
        fields = ('__all__')

class PromotionSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = Plan
        fields = ('__all__')
