# Docker

## Цель
Разработать Docker-образ на базе Ubuntu 22.04, содержащий:
- Bash-скрипт/pуthon-скрипт (из первого раздела)
- Все необходимые зависимости для его корректного выполнения.


## Описание
- Dockerfile использует образ ubuntu:22.04
- Обновляем пакеты, скачиваем python3, python3-pip для работы скрипта
- Копируем скрипт в контейнер
- Через pip устанавливаем библиотеку requests для работы с http-запросами
- Даем доступ к исполнению скрипта
- При старте контейнера скрипт автоматически запустится через entrypoint
- Проверяем работоспособность скрипта через docker logs

## Тестирование
Собираем образ:
```bash
sudo docker build -t httpstat .
```

Запускаем контейнер на фоне:
```bash
sudo docker run -d --name httpstat_test httpstat
```

Смотрим логи через docker logs:
```bash
sudo docker logs httpstat_test
```

```
└─$ sudo docker logs httpstat_test                                                   
[2025-05-02 16:14:26,385] - INFO - URL: https://httpstat.us/101 | Status: 101 | Body: 
[2025-05-02 16:14:27,625] - INFO - URL: https://httpstat.us/200 | Status: 200 | Body: 200 OK
[2025-05-02 16:14:28,764] - INFO - URL: https://httpstat.us/300 | Status: 300 | Body: 300 Multiple Choices
[2025-05-02 16:14:29,943] - ERROR - Exception error https://httpstat.us/404: 404 Client Error: Not Found for url: https://httpstat.us/404
[2025-05-02 16:14:31,191] - ERROR - Exception error https://httpstat.us/500: 500 Server Error: Internal Server Error for url: https://httpstat.us/500
```
