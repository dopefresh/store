website: https://ecommerce-by-popov-vasilii-app.ru.com/

## Использованные технологии:
1. Django
2. Django-allauth(с Google Oauth Provider)
3. Django translation framework
4. Yookassa(вебхуком мне приходит уведомление об оплате)
5. Postgresql
6. PgBouncer
7. Nginx(letsencrypt с помощью certbot)
8. Gunicorn
9. Celery
10. Bootstrap
11. AJAX

В верхнем правом углу есть кнопки смены языка, до конца я не довёл перевод
(описания и названия товаров только на русском), так как у меня нет на это времени в данный момент

Сервер с одним ядром и с 1гб оперативы на reg.ru.
Nginx, Gunicorn, PostgreSQL, Celery Worker делят 1 ядро, поэтому сайт может сильно тормозить,
так как это пет проект, то сильно затрачиваться на сервер я не собираюсь, поэтому не судите строго. 
Пожалуйста сообщите если этот проект действительно не дотягивает на уровень джуна, так как
мой счёт на облачных серверах через ~2 месяца дойдёт до нуля. 
Вёрстка действительно проста и ужасна, так как я не желаю быть фронтэндером на каком либо проекте
и не имею тут никаких особых умений, также очень буду рад роли DBA и девопс и имею огромное желание попробовать кластеризацию бд
а также микросервисы(скорее всего ими я займусь в свободное время).
