# FixedFloatApi

A Python wrapper for interacting with the FixedFloat API to exchange cryptocurrencies.

## Installation

```bash
pip install FixedFloatApi
```

## Usage

```bash
from fixedfloatapi import FixedFloatApi
```

# create a new API client
```bash
api = FixedFloatApi(key='YOUR_API_KEY', secret='YOUR_API_SECRET')
```

# Get a list of supported currencies
```bash
ccies = api.ccies()
print(ccies)
```

# Get the current price for an exchange
```bash
price = api.price({
    'fromCcy': 'BTC',
    'toCcy': 'ETH',
    'amount': 1.0,
    'direction': 'from',
    'type': 'fixed' # or 'float'
})
print(price)
```

# Create a new exchange order
```bash
order = api.create({
    'fromCcy': 'BTC',
    'toCcy': 'ETH',
    'amount': 1.0,
    'direction': 'from',
    'type': 'fixed', # or 'float'
    'toAddress': '0x123...'
})
print(order)
```

# Place an order for an existing exchange
```bash
order_status = api.order({
    'id': '12345',
    'token': 'TESTTOKENvRB90NOtr397kHY3PJ1VRy2p29HHaN7'
})
print(order_status)
```

# Request emergency assistance for an exchange
```bash
emergency = api.emergency({
    'id': '12345',
    'token': 'TESTTOKENvRB90NOtr397kHY3PJ1VRy2p29HHaN7',
    'choice': 'EXCHANGE'
})
print(emergency)
```

# set email address for order notifications
```bash
set_email = api.setEmail({
    'id': 'TESTID',
    'token': 'TESTTOKENvRB90NOtr397kHY3PJ1VRy2p29HHaN7',
    'email': 'notifyme@gmail.com',
})
print(set_email)
```

# get a QR code for a trade
```bash
qr_code = api.qr({
    'id': 'TESTID',
    'token': 'TESTTOKENvRB90NOtr397kHY3PJ1VRy2p29HHaN7',
})
print(qr_code)
```

For more information, see the [API documentation](https://fixedfloat.com/api).
