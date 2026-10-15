# Структура и французские тексты сайта

Дата редакции: 2026-10-06. Редакция сайта салона после уточнений пользователя.

Связанные документы: [проектная документация](PROJECT_DOCUMENTATION.md), [план разработки](DEVELOPMENT_PLAN.md).

Это редакционный исходник для реализации и дальнейших правок. Французские цитаты, подписи и значения в таблицах предназначены для интерфейса; русские пояснения остаются внутри проекта. Тексты подготовлены агентом по подтвержденным источникам и не обозначают отдельное утверждение каждой фразы клиентом. Базовая редакция перенесена в локальный макет `dist/index.html` на этапе 3; сайт не опубликован.

Квалификация «подолог» подтверждена пользователем 2026-10-06; шесть ранее найденных услуг включены в основной раздел. Сайт представляет салон AM Beauty Concept и его услуги. Второе направление — коррекция фигуры, французское название `Remodelage de la silhouette`. Все обращения ведутся от лица салона.

## 1. Порядок блоков и навигация

Один H1 на странице; названия основных разделов — H2, названия карточек — H3. Идентификаторы ниже используются в HTML, а не в якорях этого Markdown-файла.

| Порядок | Блок | ID в HTML | Подпись в навигации |
| --- | --- | --- | --- |
| 1 | Первый экран | `accueil` | Логотип ведет к `#accueil` |
| 2 | Подология и уход за стопами | `soins-des-pieds` | Podologie |
| 3 | Коррекция фигуры | `silhouette` | Remodelage |
| 4 | Салон | `a-propos` | Le salon |
| 5 | Пример работы | `realisations` | Отдельный пункт меню не нужен |
| 6 | Адрес и посещение | `informations-pratiques` | Accès |
| 7 | Практические вопросы | `questions` | Отдельный пункт меню не нужен |
| 8 | Запись и контакты | `contact` | Contact |

В шапке и на мобильном экране основное действие — `Prendre rendez-vous`, ссылка на WhatsApp. Название бренда — `AM Beauty Concept`; подпись — `Salon de beauté · Cluses`. На мобильном меню использовать те же пункты и порядок. Кнопки не должны перекрывать содержание.

## 2. Первый экран

Короткая подпись:

> AM Beauty Concept · Cluses

H1:

> Votre salon de beauté à Cluses

Подзаголовок:

> Podologie & remodelage de la silhouette

Основной текст:

> Des soins des pieds et des ongles aux prestations de remodelage de la silhouette, découvrez les services d’AM Beauty Concept. Votre salon de beauté à Cluses vous accueille sur rendez-vous.

Основная кнопка: [Prendre rendez-vous](https://wa.me/33629126645).

Вторая кнопка: [Appeler](tel:+33629126645).

Практическая подпись:

> 36 Avenue Paul Béchet · Cluses
>
> Sur rendez-vous uniquement

Рядом с основной кнопкой:

> Contactez le salon sur WhatsApp pour convenir d’un créneau.

## 3. Подология и уход за стопами

H2:

> Podologie & soins des pieds

Краткое представление:

> Des soins dédiés à la peau des pieds et aux ongles.

Текст:

> De l’entretien des pieds aux soins ciblés de la peau et des ongles, découvrez les prestations de podologie proposées au salon.

Подпись:

> Soins des pieds et des ongles · Sur rendez-vous

Кнопка: [Parler de mes besoins](https://wa.me/33629126645).

Шесть карточек основной редакции:

| Заголовок | Описание |
| --- | --- |
| Soin des pieds et des ongles | Un soin consacré à la peau des pieds et à l’entretien des ongles. |
| Callosités | Des soins ciblés pour les zones de peau épaissie sur les pieds. |
| Cors | Un soin localisé des cors du pied. |
| Ongle incarné | Des soins de l’ongle incarné, adaptés à la situation rencontrée. |
| Reconstruction de l’ongle | Une reconstruction pour améliorer l’aspect d’un ongle abîmé. |
| Verrues plantaires | Des soins des verrues plantaires selon la méthode pratiquée au salon. |

Источник перечня — ранее проверенный список услуг клиента; квалификация подтверждена пользователем 2026-10-06. Конкретные методы, цены и длительность не выдумываются. Карточки включены в HTML.

## 4. Коррекция фигуры

H2:

> Remodelage de la silhouette

Вступление:

> Découvrez les prestations de remodelage de la silhouette proposées par le salon. Pour connaître les modalités d’une séance et les zones concernées, contactez-nous.

### Карточка 1

H3:

> Lipocavitation

Описание:

> Une technique utilisant les ultrasons, proposée pour le remodelage de la silhouette.

### Карточка 2

H3:

> Cryolipolyse

Описание:

> Une technique esthétique utilisant le froid pour cibler des amas graisseux localisés.

### Карточка 3

H3:

> Radiofréquence

Описание:

> Un soin esthétique par radiofréquence, proposé pour travailler la fermeté de la peau.

### Карточка 4

H3:

> HIFU

Описание:

> Une technique par ultrasons focalisés de haute intensité, utilisée à visée esthétique.

Общая подпись под карточками:

> Une question sur ces prestations ? Contactez le salon avant de prendre rendez-vous.

Кнопка: [Me renseigner sur le remodelage](https://wa.me/33629126645).

Описаны общие принципы, а не характеристики оборудования клиента. Конкретные зоны, число сеансов, результаты, сроки, цены и подробные протоколы не добавлены. Источники терминологии указаны в проектной документации. Липолазер в текущую редакцию не включен.

## 5. Салон

H2:

> Le salon AM Beauty Concept

Текст:

> Un même lieu pour les soins de podologie et le remodelage de la silhouette. Retrouvez nos prestations à Cluses, au 36 Avenue Paul Béchet, sur rendez-vous.
>
> Une question sur un soin ? Contactez le salon par WhatsApp ou par téléphone pour préparer votre visite.

Кнопка внутри страницы: `Contacter le salon` → `#contact`.

Блок представляет направления салона; личная биография не нужна. Квалификация подтверждена пользователем, но дипломы, стаж, регистрационные номера и состав команды не предоставлены и не добавляются.

## 6. Пример работы

H2:

> Un aperçu des soins des pieds

Подпись к фото:

> Exemple de soin des pieds présenté par AM Beauty Concept.

Изображение: [отобранный пример работы](research/client-assets/foot-care-example.jpg).

Альтернативный текст:

> Deux vues de talons avant et après un soin des pieds.

Использовать одну фотографию с сохранением всего изображения и его порядка; не превращать ее в интерактивный слайдер до/после. Не добавлять статистику, отзывы, универсальные обещания результата или сроки. Разрешение пользователя на этот конкретный файл получено. Блок расположен ниже услуг и представления, не на первом экране.

## 7. Адрес и посещение

H2:

> Votre rendez-vous à Cluses

Название:

> AM Beauty Concept

Адрес:

> 36 Avenue Paul Béchet
>
> 74300 Cluses, France

Режим:

> Sur rendez-vous uniquement

Текст:

> Contactez le salon pour convenir du jour et de l’heure de votre visite.

Кнопка: [Voir l’itinéraire](https://www.google.com/maps/search/?api=1&query=36%20Avenue%20Paul%20B%C3%A9chet%2C%2074300%20Cluses%2C%20France).

Ссылка передает адрес в поиск Google Maps; это не подтвержденная карточка организации и не проверка географической метки. Встроенная карта не требуется. Парковка, доступность для колясок, выезд и часы работы пока неизвестны и в публичный текст не включены.

## 8. Практические вопросы

H2:

> Avant votre visite

### Вопрос 1

> Comment prendre rendez-vous ?

Ответ:

> Écrivez au salon sur WhatsApp ou appelez le +33 6 29 12 66 45 pour convenir d’un créneau. Les visites se font uniquement sur rendez-vous.

### Вопрос 2

> Où se trouve AM Beauty Concept ?

Ответ:

> AM Beauty Concept vous accueille au 36 Avenue Paul Béchet, 74300 Cluses. Le lien « Voir l’itinéraire » vous permet de préparer votre trajet.

### Вопрос 3

> Comment me renseigner sur une prestation ou son tarif ?

Ответ:

> Contactez le salon en précisant la prestation qui vous intéresse. Vous pourrez poser vos questions avant de convenir d’un rendez-vous.

Три ответа опираются на подтвержденные адрес, контакты и способ записи. Медицинский FAQ, обещания консультации или бесплатного обследования, таблица противопоказаний и прогнозы результата не добавляются.

## 9. Контакты и запись

H2:

> Prenons rendez-vous

Текст:

> Pour un soin de podologie ou une prestation de remodelage de la silhouette, contactez notre salon à Cluses pour convenir d’un rendez-vous.

Основная кнопка: [Prendre rendez-vous](https://wa.me/33629126645).

Вторая кнопка: [Appeler](tel:+33629126645).

| Подпись | Видимый текст | Ссылка |
| --- | --- | --- |
| Téléphone / WhatsApp | +33 6 29 12 66 45 | `tel:+33629126645` для номера; отдельная кнопка WhatsApp выше |
| E-mail | ambeautyconcept74@gmail.com | [ambeautyconcept74@gmail.com](mailto:ambeautyconcept74@gmail.com) |
| Facebook | AM Beauty Concept | [Retrouvez AM Beauty Concept sur Facebook](https://www.facebook.com/profile.php?id=61587787724463) |

Подпись:

> Sur rendez-vous uniquement. La date et l’heure sont convenues directement avec le salon.

Сайт открывает канал общения, не отправляет сообщение автоматически и не показывает фиктивное подтверждение брони. Форма, поля персональных данных и чекбоксы для отсутствующей формы не нужны.

## 10. Подвал и служебные подписи

Подвал:

> AM Beauty Concept
>
> Podologie · Remodelage de la silhouette
>
> Cluses, Haute-Savoie
>
> © 2026 AM Beauty Concept

Год при реализации можно получать автоматически. Ссылки `Mentions légales` и `Confidentialité` добавлять вместе с реальными страницами на этапе реализации; пока данных владельца и хостинга нет, не создавать пустые адреса или ссылки `#`.

| Элемент | Французская подпись |
| --- | --- |
| Ссылка пропуска навигации | Aller au contenu |
| Область навигации | Navigation principale |
| Открытие мобильного меню | Ouvrir le menu |
| Закрытие мобильного меню | Fermer le menu |
| Ссылка логотипа к началу | AM Beauty Concept — retour à l’accueil |
| Доступное имя кнопки WhatsApp | Prendre rendez-vous sur WhatsApp |
| Доступное имя кнопки звонка | Appeler AM Beauty Concept |
| Доступное имя почтовой ссылки | Envoyer un e-mail à AM Beauty Concept |
| Альтернативный текст отдельного логотипа | AM Beauty Concept |

Для логотипа, дублирующего соседнее текстовое название внутри одной ссылки, допустим пустой `alt`, чтобы не повторять одно название дважды. Декоративные изображения имеют пустой `alt`. Кнопки с видимым французским текстом не требуют избыточного дублирования через `aria-label`.

### Дополнения интерфейса на этапе 3

Нейтральные подписи для композиции; не добавляют новых услуг или фактов:

| Место | Французская подпись |
| --- | --- |
| Видимая кнопка меню | Menu / Fermer |
| Нумерация направлений | 01 / Podologie; 02 / La silhouette |
| Надпись над фото работы | Les soins en images |
| Надпись над FAQ | Quelques repères |
| Подпись декоративной иллюстрации | Podologie & silhouette |
| Подпись контактов | AM Beauty Concept · Cluses |

На первом экране добавлен декоративный натюрморт, не изображающий кабинет клиента; пустой `alt`. Происхождение и промпт — в [DESIGN.md](DESIGN.md). Переносы строк, курсив и завершающие точки заголовков определяются композицией; смысл основных текстов сохранен.

## 11. Метаданные

| Поле | Значение |
| --- | --- |
| Язык HTML | `fr` |
| Title | AM Beauty Concept · Salon de beauté à Cluses |
| Description | Salon de beauté à Cluses : podologie, soins des pieds et remodelage de la silhouette. Découvrez nos prestations et prenez rendez-vous chez AM Beauty Concept. |
| Open Graph title | AM Beauty Concept · Salon de beauté à Cluses |
| Open Graph description | Salon de beauté à Cluses : podologie, soins des pieds et remodelage de la silhouette. Découvrez nos prestations et prenez rendez-vous chez AM Beauty Concept. |
| Open Graph locale | `fr_FR` |
| Open Graph type | `website` |

Canonical, адрес изображения для соцсетей и URL структурированных данных появятся после выбора домена и подготовки изображения. В метаданных представлены салон и его услуги. Подтверждение «подолог» не означает подтверждения звания врача, государственного диплома, стажа, отзывов или регистрационных номеров. Разметка FAQ не обязательна; видимый блок вопросов должен быть полезен сам по себе.
