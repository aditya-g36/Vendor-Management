from django.db.models import Avg, F, ExpressionWrapper, DurationField, Q, Sum, Count
from django.utils import timezone
from django.db.models import Count

def calculate_on_time_delivery_rate(vendor,current_order):
    total_orders = vendor.purchase_orders.count()
    total_orders+=1
    on_time_orders = vendor.purchase_orders.filter(
        delivery_date__lte=F('expected_delivery_date'),
        status='Delivered'
    ).count()

    if current_order.status=='Delivered':
        on_time_orders+=1
    if total_orders > 0:
        return (on_time_orders / total_orders) * 100
    else:
        return 0

def calculate_quality_rating_avg(vendor,current_order):
    total_rating = vendor.purchase_orders.filter(
        status='Delivered'
    ).aggregate(
        total_rating=Sum('quality_rating')
    )['total_rating'] or 0

    total_orders = vendor.purchase_orders.filter(
        status='Delivered'
    ).count()

    if total_orders > 0:
        avg_rating = (total_rating + current_order.quality_rating) / (total_orders + 1)
        return avg_rating
    else:
        return current_order.quality_rating


def calculate_average_response_time(vendor,current_order):
    acknowledged_orders = vendor.purchase_orders.filter(
        acknowledgment_date__isnull=False
    ).annotate(
        response_time=F('acknowledgment_date') - F('issue_date')
    )
    total_response_time = sum(
        (order.response_time.total_seconds() for order in acknowledged_orders),
        0
    )
    total_response_time+=(current_order.acknowledgment_date - current_order.issue_date).total_seconds()

    return total_response_time / (acknowledged_orders.count()+1)

def calculate_fulfillment_rate(vendor,current_order):
    total_orders = vendor.purchase_orders.count()
    total_orders+=1
    fulfilled_orders = vendor.purchase_orders.filter(status='Delivered').count()
    if current_order.status == 'Delivered':
        fulfilled_orders+=1

    if total_orders > 0:
        return (fulfilled_orders / total_orders) * 100
    else:
        return 0

#

def hp_calculate_on_time_delivery_rate(vendor,current_order):
    total_orders = vendor.purchase_orders.count()
    total_orders+=1
    if total_orders == 0:
        return 0

    on_time_orders = vendor.purchase_orders.filter(
        delivery_date__lte=F('expected_delivery_date'),
        status='Delivered'
    ).count()

    if current_order.status=='Delivered':
        on_time_orders+=1
    return on_time_orders / total_orders




def hp_calculate_fulfillment_rate(vendor,current_order):
    total_orders = vendor.purchase_orders.count()
    total_orders+=1
    fulfilled_orders = vendor.purchase_orders.filter(
        status='Delivered'
    ).count()

    if current_order.status=='Delivered':
        fulfilled_orders+=1

    return fulfilled_orders / total_orders

