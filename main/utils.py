from django.core.mail import send_mail

def send_welcome_email(email):
    url = 'http://localhost:8000/'
    message = f'<h1>Спасибо за региструцию на нашем сайте PyShop12: </h1>{url}'
    send_mail(
        'Sweetness Welcome!!!',
        message,
        'pyshopadmin@gamil.com',
        [email,],
        fail_silently=False)

