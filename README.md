## Описание

*Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).
Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.
Авторизация осуществляется посредством JSON Web Token – это открытый стандарт (RFC 7519).*

## Установка

Клонировать репозиторий и перейти в него в командной строке:
````
git clone https://github.com/VanishSun/api_yamdb/
cd api_yamdb
````
Cоздать и активировать виртуальное окружение:
````
python -m venv env
source env/bin/activate
````
Установить зависимости из файла requirements.txt:
````
python -m pip install --upgrade pip
pip install -r requirements.txt
````
Выполнить миграции:
````
python manage.py migrate
````
Запустить проект:
````
python manage.py runserver
````

## URL's list

```/redoc/``` - docs проекта в формате redoc с примерами запросов и ответов API;

```/admin/``` - администрирование;

```/api/v1/``` - API;

```/api/v1/users/``` - список всех пользователей;

```/api/v1/users/<username>/``` - доступ к карточке пользователя;

```/api/v1/users/me/``` - доступ к личной карточке пользователя;

```/api/v1/auth/signup/``` - запрос confirmation code на email;

```/api/v1/auth/token/``` - получение JWT токена;

```/api/v1/categories/``` - список всех жанров; создание нового жанра;

```/api/v1/categories/<slug>/``` - удаление указанной категории;

```/api/v1/genres/``` - список всех категорий; создание новой категории;

```/api/v1/genres/<slug>/``` - удаление указанного жанра;

```/api/v1/titles/``` - список всех объектов; создание нового объкта;

```/api/v1/titles/<title_id>/``` - информация о произведении по id; изменение и удаление;

```/api/v1/titles/<title_id>/reviews/``` - список всех отзывов; добавление отзыва;

```/api/v1/titles/<title_id>/reviews/<review_id>/``` - отзыв по id для указанного произведения; изменение и удаление;

```/api/v1/titles/<title_id>/reviews/<review_id>/comments/``` - список всех комментариев к отзыву по id; добавление комментария;

```/api/v1/titles/<title_id>/reviews/<review_id>/comments/<comment_id>/``` - комментарий для отзыва по id; изменение и удаление;


## Project's authors

[Верозуб Иван](https://github.com/VanishSun)
[Шакертов Руслан](https://github.com/shakertov)
[Королева Валентина](https://github.com/Valentina-Koroleva)
