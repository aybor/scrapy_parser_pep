# Scrapy-парсер Python Enhancement Proposals

## Описание

Программа в автоматическом режиме собирает номера, названия и статусы PEP с сайта https://peps.python.org/ , обрабатывает и выводит результат в два `.csv` файла.

## Примеры результата
### Таблица `ststus_summary`
| Статус      | Количество |
|:------------|:----------:|
| Active      |     36     |
| Final       |     253    |
| Withdrawn   |     53     |
| Rejected    |     118    |
| Deferred    |     36     |
| Accepted    |     42     |
| Superseded  |     16     |
| Draft       |     34     |
| April Fool! |     1      |
| Total       |     589    |

### Таблица `pep` (первые 10 строк)
| number |                       name                       |   status  |
|:------:|:-------------------------------------------------|:---------:|
|    1   | PEP 1 – PEP Purpose and Guidelines               |   Active  |
|   247  | PEP 247 – API for Cryptographic Hash Functions   |   Final   |
|   248  | PEP 248 – Python Database API Specification v1.0 |   Final   |
|   243  | PEP 243 – Module Repository Upload Mechanism     | Withdrawn |
|   244  | PEP 244 – The directive statement                | Rejected  |
|   245  | PEP 245 – Python Interface Syntax                | Rejected  |
|   242  | PEP 242 – Numeric Kinds                          | Rejected  |
|   249  | PEP 249 – Python Database API Specification v2.0 |   Final   |
|   246  | PEP 246 – Object Adaptation                      | Rejected  |
|   241  | PEP 241 – Metadata for Python Software Packages  |   Final   |

## Установка
1. Клонировать репозиторий
```
git clone https://github.com/aybor/scrapy_parser_pep.git
```
2. Перейти в папку с проектом
```
cd scrapy_parser_pep
```
3. Установить зависимости
```
pip install -r requirements.txt
```
## Использование
1. Запустить проект
```
python pep_parse/main.py
```
2. Дождаться завершения программы

Результирующие файлы находятся в папке `pep_parse/results`