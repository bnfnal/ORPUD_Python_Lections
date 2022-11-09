"""
Лекция 7.1.
Виртуальные окружения.
Создание, активация, выход
"""

# чтобы решать проблемы с разными версиями интерпритатора и библиотек используют виртуальные окружения
# до этого мы запускали код через тот интерпритатор, кот установлен в системе
# в настоящих проектах лучше всего создать виртуальное окружение в первую очередь

# до этого мы использовали системное окружение, т.е.
# каждая наша программа обращалась к системному интерпритатору python, кот выполнял наш код
# после того, как мы начнем использовать виртуальное окружение, наша программа будет вызывать
# тот интерпритатор python, кот в этом окружении используется (на пример везде внутри этого окружения будет python 3.9)
# кроме того, все модули, кот будут устанавливаться внутри виртуального окружения
# будут доступны только внутри этого виртуального окружения
# если мы из этого виртуального окружения выйдем либо войдем в какое-то другое
# то там список этих модулей будет отличаться и программа будет использовать только нужные и проверенные нами версии установленных модулей

# чтобы использовать виртуальное окружение:
# его нужно сначала установить командой
# pip install virtualenv
# pithon3 -m venv env - создание виртуального окружения
# через ключ -m образаемся к модулю venv и в папке env создаем виртуальное окружение
# создастся папка env, в кот уже будут интерпритаторы pithon и pip, кот запускают работу этих программ в виртуальном окружении

# разности файлов зависят от окружения, компьютера или сервера, где ваш код запускается, а значит
# они не должны быть в репозитрории и их нужно добавить в .gitignore

# venv - название утилиты
# Утилита — вспомогательная компьютерная программа в составе общего программного обеспечения для выполнения специализированных типовых задач,
# связанных с работой оборудования и операционной системы (ОС). Утилиты предоставляют доступ к возможностям (параметрам, настройкам, установкам),
# недоступным без их применения, либо делают процесс изменения некоторых параметров проще (автоматизируют его).
# env - название окружения

# папка окружения должна быть в .gitignore
# source env/Scripts/activate - вход в окружение
# в командной строке вместо d/PycharmProjects/ORPUD/ORPUD_Python/ORPUD_Python_Lections (master)
# должно появиться (env) d/PycharmProjects/ORPUD/ORPUD_Python/ORPUD_Python_Lections (master)

# как только мы попали в виртуальное окружение, мы можем в командной строке Bash вызвать просто python,
# тк версия здесь та, кот мы исп при создании окружения (можно не указывать версию python3 b pip3, а просто исп python и pip соотв)
# любой вызов команды всегда будет ссылаться на одну и ту же версию python и pip

# выполняем все, что душе угодно
# устанавливаем модули, запускаем проекты и тд
# эти команды будут выполнены в виртуальном окружении и не повлияют на другие окружения и системные настройки
# deactivate - выход из окружения и (env) в командной строке исчезнет
# или просто закрываем терминал, если совсем завершаете работу
# теперь мы можем либо снова войти в наше или какое-то другое окружение

# виртуальные окружения нужны для изоляции версий итерпритатора pithon и версий устанавливаемых библиотек

