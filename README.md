***Stripe_Project***
===

Это веб-приложение на django в котором каждый может 'Купить' любой товар через тестовый режим платежной системы [`Stripe`](stripe.com/docs).
Товар регистрируется в стандартной админке Djando по адресу `http://127.0.0.1:8000/admin/`
Сайт доступен по локальному адресу `http://127.0.0.1:8000/`

---
Для начала работы вам необходимо зарегистрировать администратора для приложения.
Делается это в консоли командой:
````
python manage.py createsuperuser
````
Далее вводятся логин, почта и пароль.

---
После регистрации, по данному логину и паролю вы сможете войти в админку и в ней зарегистрировать товар(ы).
Внимание! Цену товара необходимо указывать в копейках, то бишь умножать на 100, что бы товар был доступен для покупки.

---
Как только товар будет создан, он будет доступен для 'покупки' по адресу `http://127.0.0.1:8000/items/{id_товара}/`
По нажатию на кнопку "Купить", производится запрос по адресу `http://127.0.0.1:8000/buy/{id_товара}/` с получением и переходом по ссылке сессии тестовой покупки.
Для тестовой покупки можно использовать карту `4242 4242 4242 4242`     `02/24`   `000`
После оплаты производится редирект обратно на страницу товара.

---
Для запуска локального сервера с приложением предусмотрена команда 
-
````
python manage.py runserver
````

---
Для работы программы необходима библиотека `requests`, `django` и `django-rest-framework`!
-
Для быстрой установки необходимых зависимостей предусмотрен файл requirements.txt.
В терминал вводится команда:
````
pip install -r requirements.txt
````
