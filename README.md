Инструкция по запуску:
1. Клонировать репозиторий git clone https://github.com/Kaliendos/testovoe.git
2. перейти в рабочую директорию cd testovoe
3. установка зависимостей pip install -r requirements.txt
4. В файле settinfs.py настроить подключение к бд
5. выполнить миграции ./manage.py runserver
part1 - первая часть задания, part2 - вторая
Есть 2 эндпоинта для проверки работы: "" - для проверки присваивания приза игроку и "write_scv/" для проверки записи в scv файл. 
