from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
import random

# یک کلاس ساده برای شبیه‌سازی متد get_order_type_display در مدل‌های جنگو
class MockPendingOrder:
    def __init__(self, id, symbol, order_type, order_type_display, volume, entry_price, sl, tp, created_at):
        self.id = id
        self.symbol = symbol
        self.order_type = order_type
        self.order_type_display = order_type_display
        self.volume = volume
        self.entry_price = entry_price
        self.stop_loss = sl
        self.take_profit = tp
        self.created_at = created_at

    def get_order_type_display(self):
        return self.order_type_display

def dashboard_demo_view(request):
    now = timezone.now()

    # ۱. شبیه‌سازی اطلاعات حساب کاربر (Account)
    account = {
        'balance': 10500.50,
        'equity': 10620.75,
        'margin_used': 450.00,
        'win_rate': 68.5,
    }

    # ۲. شبیه‌سازی لیست قیمت نمادها (Price List)
    symbols = ['US30', 'XAUUSD', 'EURUSD', 'AUDUSD', 'NZDUSD', 'USDJPY', 'NAS100', 'USOIL', 'ETHUSDT']
    price_list = []
    for sym in symbols:
        base_price = random.uniform(1.0, 35000.0) if sym != 'EURUSD' else random.uniform(1.05, 1.10)
        price_list.append({
            'symbol': sym,
            'price': base_price,
            'spread': random.uniform(0.1, 2.5),
            'commission': random.uniform(1.0, 5.0),
            'swap_long': random.uniform(-5.0, -1.0),
            'swap_short': random.uniform(0.1, 2.0),
        })

    # ۳. شبیه‌سازی پوزیشن‌های باز (Open Positions)
    open_positions = [
        {
            'id': 101,
            'symbol': 'XAUUSD',
            'type': 'buy',
            'volume': 0.50,
            'open_price': 2340.50,
            'stop_loss': 2330.00,
            'take_profit': 2360.00,
            'open_time': (now - timedelta(hours=2)).strftime('%Y-%m-%d %H:%M:%S'),
            'unrealized_pl': 120.25  # این مقدار توسط JS در فرانت هم آپدیت می‌شود
        },
        {
            'id': 102,
            'symbol': 'EURUSD',
            'type': 'sell',
            'volume': 1.00,
            'open_price': 1.08500,
            'stop_loss': 1.09000,
            'take_profit': 1.07500,
            'open_time': (now - timedelta(minutes=45)).strftime('%Y-%m-%d %H:%M:%S'),
            'unrealized_pl': -15.50
        }
    ]

    # ۴. شبیه‌سازی اوردرهای پندینگ (Pending Orders)
    pending_orders = [
        MockPendingOrder(
            id=201, symbol='US30', order_type='buy_limit', order_type_display='Buy Limit',
            volume=0.20, entry_price=38500.0, sl=38400.0, tp=38800.0,
            created_at=now - timedelta(minutes=10)
        )
    ]

    # ۵. شبیه‌سازی تاریخچه معاملات (History)
    history = [
        {
            'position': {
                'id': 98,
                'symbol': 'USOIL',
                'type': 'buy',
                'open_price': 82.50,
                'stop_loss': 81.00,
                'take_profit': 85.00,
                'open_time': now - timedelta(days=1),
            },
            'volume_closed': 1.00,
            'close_price': 84.20,
            'pl': 170.00,
            'total_commission': -5.00,
            'close_time': now - timedelta(hours=5),
        },
        {
            'position': {
                'id': 99,
                'symbol': 'NAS100',
                'type': 'sell',
                'open_price': 18000.00,
                'stop_loss': 18100.00,
                'take_profit': 17800.00,
                'open_time': now - timedelta(days=2),
            },
            'volume_closed': 0.50,
            'close_price': 18050.00,
            'pl': -50.00,  # ضرر
            'total_commission': -2.50,
            'close_time': now - timedelta(days=1, hours=2),
        }
    ]

    # ۶. شبیه‌سازی اطلاعات آنالیز حساب (Analysis)
    analysis = {
        'status': 'فعال (Active)',
        'daily_limit': 500.00,
        'overall_limit': 1500.00,
        'floating_risk_limit': 300.00,
    }

    # در صورتی که کاربر لاگین نکرده باشد و بخواهید دستی اطلاعاتش را بسازید (اگر از سیستم Auth پیش‌فرض استفاده نمی‌کنید):
    # request.user.account_number = 'PRP-987654'
    # request.user.first_name = 'کاربر'
    # request.user.last_name = 'دمو'

    context = {
        'account': account,
        'price_list': price_list,
        'open_positions': open_positions,
        'pending_orders': pending_orders,
        'history': history,
        'analysis': analysis,
    }

    return render(request, 'dashboard.html', context)