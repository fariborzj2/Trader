import os
import django
from django.conf import settings
from django.template import Context, Template
from django.urls import path

# Mock views for reverse matching
def dummy_view(request): pass

urlpatterns = [
    path('logout/', dummy_view, name='logout'),
    path('new_order/', dummy_view, name='new_order'),
    path('create_pending_order/', dummy_view, name='create_pending_order'),
]

# Set the base directory to the parent directory of scripts
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Configure Django settings
settings.configure(
    DEBUG=True,
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR],
    }],
    STATIC_URL='/static/',
    ROOT_URLCONF=__name__,
)
django.setup()

# Read the template
template_path = os.path.join(BASE_DIR, 'dashboard.html')
with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

template = Template(template_content)

# Provide mock data
context = Context({
    'request': {
        'user': {
            'account_number': '123456789',
            'first_name': 'علی',
            'last_name': 'رضایی'
        }
    },
    'account': {
        'balance': 10000.00,
        'equity': 10150.50,
        'margin_used': 500.00,
        'win_rate': 65.5
    },
    'price_list': [
        {'symbol': 'US30', 'price': 38500.5, 'spread': 1.5, 'commission': 3.0, 'swap_long': -5.0, 'swap_short': 2.0},
        {'symbol': 'XAUUSD', 'price': 2025.30, 'spread': 2.0, 'commission': 3.0, 'swap_long': -10.0, 'swap_short': 4.0},
        {'symbol': 'EURUSD', 'price': 1.0850, 'spread': 0.8, 'commission': 3.0, 'swap_long': -6.0, 'swap_short': 1.0},
        {'symbol': 'AUDUSD', 'price': 0.6540, 'spread': 0.9, 'commission': 3.0, 'swap_long': -4.0, 'swap_short': 0.5},
        {'symbol': 'NZDUSD', 'price': 0.6120, 'spread': 1.0, 'commission': 3.0, 'swap_long': -3.5, 'swap_short': 0.5},
        {'symbol': 'USDJPY', 'price': 150.20, 'spread': 1.2, 'commission': 3.0, 'swap_long': 5.0, 'swap_short': -15.0},
        {'symbol': 'NAS100', 'price': 17800.2, 'spread': 1.5, 'commission': 3.0, 'swap_long': -4.0, 'swap_short': 1.5},
        {'symbol': 'USOIL', 'price': 78.50, 'spread': 2.5, 'commission': 3.0, 'swap_long': -8.0, 'swap_short': 2.5},
        {'symbol': 'ETHUSDT', 'price': 3050.80, 'spread': 1.0, 'commission': 0.0, 'swap_long': -15.0, 'swap_short': -15.0},
    ],
    'messages': [],
    'open_positions': [
        {
            'id': 101, 'symbol': 'US30', 'type': 'buy', 'volume': 0.5,
            'open_price': 38400.0, 'stop_loss': 38000.0, 'take_profit': 39000.0,
            'open_time': '2023-10-27 10:30:00'
        },
        {
            'id': 102, 'symbol': 'XAUUSD', 'type': 'sell', 'volume': 1.0,
            'open_price': 2030.0, 'stop_loss': 2050.0, 'take_profit': 2000.0,
            'open_time': '2023-10-27 11:15:00'
        }
    ],
    'pending_orders': [
        {
            'id': 201, 'symbol': 'EURUSD', 'get_order_type_display': 'Buy Limit',
            'volume': 2.0, 'entry_price': 1.0800, 'stop_loss': 1.0750, 'take_profit': 1.0900,
            'created_at': '2023-10-27 09:00:00'
        }
    ],
    'history': [
        {
            'position': {
                'id': 50, 'symbol': 'US30', 'type': 'buy',
                'open_price': 38000.0, 'stop_loss': 37500.0, 'take_profit': 38500.0,
                'open_time': '2023-10-26 14:00:00'
            },
            'volume_closed': 1.0, 'close_price': 38500.0, 'pl': 500.0,
            'total_commission': 6.0, 'close_time': '2023-10-26 16:30:00'
        },
        {
            'position': {
                'id': 51, 'symbol': 'USDJPY', 'type': 'sell',
                'open_price': 150.00, 'stop_loss': 151.00, 'take_profit': 148.00,
                'open_time': '2023-10-26 15:00:00'
            },
            'volume_closed': 2.0, 'close_price': 150.50, 'pl': -100.0,
            'total_commission': 12.0, 'close_time': '2023-10-26 17:00:00'
        }
    ],
    'analysis': {
        'status': 'Active',
        'daily_limit': 500.00,
        'overall_limit': 2000.00,
        'floating_risk_limit': 1000.00
    }
})

# Render the template
rendered_html = template.render(context)

# Save the output
output_path = os.path.join(BASE_DIR, 'demo_dashboard.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(rendered_html)

print(f"Demo dashboard generated successfully as {output_path}")
