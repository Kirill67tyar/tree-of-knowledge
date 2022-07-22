"""

# -------------------------------------------------------- BRAINTREE settings
# docs:
# https://github.com/braintree/braintree_python
# https://developers.braintreepayments.com/start/hello-server/python
# https://pypi.org/project/braintree/
# https://sandbox.braintreegateway.com/merchants/ykjkq6s94qszsyb9/home
# страница 232 книга

import braintree

BRAINTREE_MERCHANT_ID = os.getenv('BRAINTREE_MERCHANT_ID')
BRAINTREE_PUBLIC_KEY = os.getenv('BRAINTREE_PUBLIC_KEY')
BRAINTREE_PRIVATE_KEY = os.getenv('BRAINTREE_PRIVATE_KEY')

#                     v----v----v

# gateway = braintree.BraintreeGateway(
#     braintree.Configuration(
#         braintree.Environment.Sandbox,
#         merchant_id=BRAINTREE_MERCHANT_ID,
#         public_key=BRAINTREE_PUBLIC_KEY,
#         private_key=BRAINTREE_PRIVATE_KEY
#     )
# )
# #                   ^----^----^ OR v----v----v
braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    # Environment.Production,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)
#                                   ^----^----^
# Важно! - для боевого режима нужен аккаунт полноценный https://www.braintreegateway.com/
# Merchant ID, Public key и Private key там нужно получать другие
# и заменить их соответсвенно

# И вместо braintree.Environment.Sandbox нужно использовать braintree.Environment.Production

# Sandbox - для тренировки, или отладке, проверке что все рабтает
# Production - для продакшн) Для боевого режима

# если интересует версия для локального сервера (не продакшн), то:
# https://sandbox.braintreegateway.com/merchants/nv5dfpjh7jv353hc/home

# для пробного варианта используй карту:
# № 4111 1111 1111 1111
# CVV - 123
# date - 12/24
# -------------------------------------------------------- BRAINTREE settings
"""