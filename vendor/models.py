from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg, F, ExpressionWrapper, DurationField
from django.utils import timezone
from django.db.models import Count
from .vendor_metrics import (
    calculate_on_time_delivery_rate,
    calculate_quality_rating_avg,
    calculate_average_response_time,
    calculate_fulfillment_rate,
    hp_calculate_on_time_delivery_rate,
    hp_calculate_fulfillment_rate
)

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)


class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchase_orders')
    po_number = models.CharField(max_length=50, unique=True)
    order_date = models.DateTimeField()
    expected_delivery_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def calculate_vendor_metrics(self):
        # Calculate metrics related to this purchase order's vendor
        self.vendor.on_time_delivery_rate = calculate_on_time_delivery_rate(self.vendor,self)
        self.vendor.quality_rating_avg = calculate_quality_rating_avg(self.vendor,self)
        self.vendor.average_response_time = calculate_average_response_time(self.vendor,self)
        self.vendor.fulfillment_rate = calculate_fulfillment_rate(self.vendor,self)
        self.vendor.save()

        historical_performance = HistoricalPerformance.objects.create(
            vendor=self.vendor,
            date=timezone.now(),
            on_time_delivery_rate=hp_calculate_on_time_delivery_rate(self.vendor,self),
            quality_rating_avg=calculate_quality_rating_avg(self.vendor,self),
            average_response_time=calculate_average_response_time(self.vendor,self),
            fulfillment_rate=hp_calculate_fulfillment_rate(self.vendor,self)
        )


    def save(self, *args, **kwargs):
        # Calculate metrics before saving the purchase order instance
        if self.status == 'Delivered':
            self.calculate_vendor_metrics()
        super().save(*args, **kwargs)


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='historical_performance')
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)