# BIM Viewer (Flask + IFC.js)

## Быстрый старт

1. Установите зависимости (вариант с virtualenv):

```bash
cd /workspace/bim_viewer
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Если `venv` недоступен, используйте user-режим:

```bash
python3 -m pip install --user -r /workspace/bim_viewer/requirements.txt
```

2. Запуск сервера:

```bash
python3 /workspace/bim_viewer/app.py
```

Сервис слушает на `0.0.0.0:5000`. Откройте с телефона: `http://<IP_сервера>:5000`.

## Использование
- На главной странице загрузите `.IFC` файл.
- После загрузки откроется страница просмотра; модель рендерится в браузере (IFC.js).
- Кнопка «Скачать PNG» сохранит скриншот текущего вида.

## Где лежат файлы
- Загруженные IFC: каталог `uploads/` в корне проекта.
- PNG снимаются на клиенте (браузер) — сохраняются локально на устройство.

## Заметки
- Проект предназначен для демо/локального использования и не содержит аутентификации.
- Для prod-режима используйте reverse-proxy (nginx), HTTPS и ограничьте размер/upload MIME-типы.
