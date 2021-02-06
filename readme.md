# D2.10 Домашнее задание

Необходимо написать простой веб-сервер с помощью фреймворка Bottle. Все ошибки приложения должны попадать в вашу информационную панель Sentry. Приложение должно размещаться на Heroku, иметь минимум два маршрута:

1.    /success, который должен возвращать как минимум HTTP ответ со статусом 200 OK
2.    /fail, который должен возвращать "ошибку сервера" (на стороне Bottle это может быть  просто RuntimeError), то есть HTTP ответ со статусом 500


## использование
локальный запуск 

```poetry run gunicorn -w 2 -b 127.0.0.1:8080 bootle_sentry.run:app```

## развертывание (деплой) 


по инструкции https://devcenter.heroku.com/articles/getting-started-with-python#prepare-the-app

необходимо установить heroku config:set SENTRY_DSN={SENTRY_DSN}

bottle.postman_collection.json - коллекция postman

api.md - api документация

адрес моего приложения https://stark-coast-45680.herokuapp.com/

