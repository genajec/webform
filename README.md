# FaceForm AI - Веб-сайт для верификации Stripe

Это минимальная версия веб-сайта FaceForm AI, созданная для верификации бизнеса в Stripe.

## Включенные страницы:
- Главная страница с описанием сервиса
- Условия использования
- Политика конфиденциальности
- Правила возврата

## Инструкции по деплою

### На Render.com:
1. Загрузите этот архив на Render.com или подключите GitHub репозиторий
2. Настройки деплоя:
   - Environment: Python
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn main:app
3. Переменные окружения:
   - STRIPE_SECRET_KEY: Ваш секретный ключ Stripe

### На VPS:
1. Установите Python и необходимые зависимости
2. Настройте Nginx или Apache в качестве прокси
3. Используйте Gunicorn для запуска: `gunicorn main:app -b 0.0.0.0:5000`
