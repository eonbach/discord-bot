## Виртуальное окружение и установка зависимостей
Для более подробного объяснения: https://docs.python.org/3/library/venv.html

**Создание виртуального окружения:**
```
py -3.8 -m venv .venv
```
Эта команда используется для создания виртуальной среды Python с использованием модуля venv для версии Python 3.8.

`-3.8` - ключ командной строки, который указывает требуемую версию Python 3.8 в случае, когда у вас установлено несколько версий Python, и вы хотите явно указать, какую версию использовать. В данном случае минимальная требуемая версия - 3.8.

`-m venv` - это часть команды, которая вызывает стандартный модуль Python `venv` для создания виртуального окружения.

`.venv` - указывает, что виртуальное окружение будет созданно в текущей рабочей директории в папке с именем `.venv`. Вы можете выбрать любое другое имя для вашей виртуальной среды.


**Активация виртуального окружения:**
  - Для Windows:
```
.venv\Scripts\activate.bat
```
  - Для Unix или MacOS:
```
source .venv/bin/activate
```
После активации вы увидите, что ваша командная строка теперь начинается с `(.env)`.


**Деактивация виртуального окружения:**
```
deactivate
```


## Установка зависимостей:
```
pip install -r requirements.txt
```
Эта команда установит все зависимости, перечисленные в файле `requirements.txt`, в созданное вами виртуальное окружение.

Теперь у вас есть виртуальное окружение, и все зависимости проекта установлены в нем.


## Настройка токена
Для успешного запуска бота потребуется использование токена при его запуске. Этот токен принадлежит созданному вами боту, его можно найти [здесь](https://discord.com/developers/applications/) (https://discord.com/developers/applications/). 

В проекте используется переменная окружения `TOKEN`, которая выгружается в виртуальное окружение из файла `.env` при помощи модуля `python-dotenv`.
Ваш файл с переменными окружения (в том числе токеном) не должен выгружаться на GitHub т.к. он указан в файле `.gitignore`, что значит каждый участник команды отвечает за его создание самостоятельно. 

1. Создайте файл (не папку, это важно!) с именем `.env` в корневой папке вашего проекта.
    - Для Windows:
    ```
    cd . > .env
    ```
    - Для Unix или MacOS:
    ```
    touch .env
    ```

3. Внутри файла `.env` добавьте строку с вашим токеном в формате `TOKEN=my-token` без каких-либо кавычек.

Теперь при запуске бота будет автоматически использован указанный вами токен. Ура!
