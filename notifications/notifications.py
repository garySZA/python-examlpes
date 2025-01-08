from plyer import notification

def notify():
    notification.notify(
        title = 'Alerta!',
        message = 'Esta es una notificación',
        timeout = 10
    )

def main():
    notify()

main()
