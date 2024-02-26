import stripe
from config.settings import STRIPE_SECRET_KEY


def get_session(instance):
    """ Функция возвращает сессию для оплаты """
    stripe.api_key = STRIPE_SECRET_KEY
    title_product = instance.name

    product = stripe.Product.create(
        name=f'{title_product}'
    )

    price = stripe.Price.create(
        unit_amount=instance.price,
        currency='rub',
        product=f'{product.id}',
    )

    session = stripe.checkout.Session.create(
        success_url=f"http://localhost:8000/item/{instance.id}/",
        line_items=[
            {
                'price': f'{price.id}',
                'quantity': 1,
            }
        ],
        mode='payment',
        customer_email='test@test.com'

    )
    return session
