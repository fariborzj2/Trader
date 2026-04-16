from django.urls import path
from django.http import JsonResponse
from .views import dashboard_demo_view

# یک ویوی دمو برای درخواست‌های ای‌پی‌آی جاوااسکریپت
def dummy_api_view(request):
    return JsonResponse({'status': 'success', 'message': 'این یک درخواست دموی موفق بود'})

urlpatterns = [
    path('', dashboard_demo_view, name='dashboard'),
    
    # مسیرهای فیک برای جلوگیری از خطای رندر قالب
    path('logout/', dummy_api_view, name='logout'),
    path('new-order/', dummy_api_view, name='new_order'),
    path('create-pending-order/', dummy_api_view, name='create_pending_order'),
]