# максимальная и минамальная цена часов
MIN_PRICE = 1
MAX_PRICE = 10000000

# есть ли упаковка/документы?
YES_OR_NO = (
    ('Нет', 'Нет'),
    ('Да', 'Да'),
)

# статус обработки заявки из формы
PROCESSED = (
    ('Только поступил', 'Только поступил'),
    ('В работе', 'В работе'),
    ('Завершено', 'Завершено'),
    ('Клиент отказался', 'Клиент отказался'),
)

# список из марок часов
MARK_CHOIСE = [
    ('Element', 'Element'),
    ('Adriatica', 'Adriatica'),
    ('Alfa', 'Alfa'),
    ('Alfex', 'Alfex'),
    ('AM:PM', 'AM:PM'),
    ('Anne Klein', 'Anne Klein'),
    ('Appella', 'Appella'),
    ('Armani Exchange', 'Armani Exchange'),
    ('Atlantic', 'Atlantic'),
    ('Aviator', 'Aviator'),
    ('Balmain', 'Balmain'),
    ('Baume & Mercier', 'Baume & Mercier'),
    ('Bering', 'Bering'),
    ('Beverly Hills Polo Club', 'Beverly Hills Polo Club'),
    ('Bigotti', 'Bigotti'),
    ('Blancpain', 'Blancpain'),
    ('Breguet', 'Breguet'),
    ('Breitling', 'Breitling'),
    ('Bulova', 'Bulova'),
    ('Calvin Klein', 'Calvin Klein'),
    ('Candino', 'Candino'),
    ('Cartier', 'Cartier'),
    ('Casio', 'Casio'),
    ('Casio Premium', 'Casio Premium'),
    ('Cerruti 1881', 'Cerruti 1881'),
    ('Certina', 'Certina'),
    ('Chanel', 'Chanel'),
    ('Charm', 'Charm'),
    ('Chopard', 'Chopard'),
    ('Citizen', 'Citizen'),
    ('Claude Bernard', 'Claude Bernard'),
    ('Continental', 'Continental'),
    ('Corum', 'Corum'),
    ('Cover', 'Cover'),
    ('D&G', 'D&G'),
    ('Daniel Klein', 'Daniel Klein'),
    ('Danish Design', 'Danish Design'),
    ('Diesel', 'Diesel'),
    ('Dior', 'Dior'),
    ('DKNY', 'DKNY'),
    ('Ebel', 'Ebel'),
    ('Elixa', 'Elixa'),
    ('Emporio Armani', 'Emporio Armani'),
    ('Epos', 'Epos'),
    ('Essence', 'Essence'),
    ('F.Gattien', 'F.Gattien'),
    ('Festina', 'Festina'),
    ('Flik Flak', 'Flik Flak'),
    ('Fossil', 'Fossil'),
    ('Frederique Constant', 'Frederique Constant'),
    ('Grand Seiko', 'Grand Seiko'),
    ('Gucci', 'Gucci'),
    ('Guess', 'Guess'),
    ('Hamilton', 'Hamilton'),
    ('Hublot', 'Hublot'),
    ('IWC', 'IWC'),
    ('Jacques Lemans', 'Jacques Lemans'),
    ('Jacques Philippe', 'Jacques Philippe'),
    ('Jaeger-LeCoultre', 'Jaeger-LeCoultre'),
    ('Jaguar', 'Jaguar'),
    ('Just Cavalli', 'Just Cavalli'),
    ('Kenneth Cole', 'Kenneth Cole'),
    ('Lee Cooper', 'Lee Cooper'),
    ('Longines', 'Longines'),
    ('Maurice Lacroix', 'Maurice Lacroix'),
    ('Michael Kors', 'Michael Kors'),
    ('MIDO', 'MIDO'),
    ('Montblanc', 'Montblanc'),
    ('Moschino', 'Moschino'),
    ('Nina Ricci', 'Nina Ricci'),
    ('Omax', 'Omax'),
    ('Omega', 'Omega'),
    ('Orient', 'Orient'),
    ('Oris', 'Oris'),
    ('Philipp Plein', 'Philipp Plein'),
    ('Piaget', 'Piaget'),
    ('Pierre Lannier', 'Pierre Lannier'),
    ('Pilot time', 'Pilot time'),
    ('Platinor', 'Platinor'),
    ('Prestige', 'Prestige'),
    ('Privilege', 'Privilege'),
    ('Q&Q', 'Q&Q'),
    ('Quantum', 'Quantum'),
    ('Qwill', 'Qwill'),
    ('Rado', 'Rado'),
    ('Ranger', 'Ranger'),
    ('Raymond Weil', 'Raymond Weil'),
    ('Roamer', 'Roamer'),
    ('Rodania', 'Rodania'),
    ('Romanoff', 'Romanoff'),
    ('Romanson', 'Romanson'),
    ('Seiko', 'Seiko'),
    ('Sekonda', 'Sekonda'),
    ('Skagen', 'Skagen'),
    ('SOKOLOV', 'SOKOLOV'),
    ('Swarovski', 'Swarovski'),
    ('Swatch', 'Swatch'),
    ('Swiss Military Chrono', 'Swiss Military Chrono'),
    ('Swiss Military Hanowa', 'Swiss Military Hanowa'),
    ('Tag Heuer', 'Tag Heuer'),
    ('Thomas Earnshaw', 'Thomas Earnshaw'),
    ('Timex', 'Timex'),
    ('Tissot', 'Tissot'),
    ('U.S. Polo Assn', 'U.S. Polo Assn'),
    ('Ulysse Nardin', 'Ulysse Nardin'),
    ('Union Glashütte', 'Union Glashütte'),
    ('Vacheron Constantin', 'Vacheron Constantin'),
    ('Versace', 'Versace'),
    ('Versus', 'Versus'),
    ('Wainer', 'Wainer'),
    ('Zenith', 'Zenith'),
    ('Маяк', 'Маяк'),
    ('Ника', 'Ника'),
    ('Победа', 'Победа'),
    ('Подарочный сертификат', 'Подарочный сертификат'),
    ('Полет', 'Полет'),
    ('Президент', 'Президент'),
    ('Престиж', 'Престиж'),
    ('Радуга', 'Радуга'),
    ('Русское время', 'Русское время'),
    ('Слава', 'Слава'),
    ('Смешарики', 'Смешарики'),
    ('Спецназ', 'Спецназ'),
    ('Спутник', 'Спутник'),
    ('ШТУРМ', 'ШТУРМ'),
    ('Штурманские', 'Штурманские')
]

# список из стран-производителей
COUNTRY_CHOIСE = [
    ('Австрия', 'Австрия'),
    ('Великобритания', 'Великобритания'),
    ('Германия', 'Германия'),
    ('Гонконг', 'Гонконг'),
    ('Дания', 'Дания'),
    ('Испания', 'Испания'),
    ('Италия', 'Италия'),
    ('Китай', 'Китай'),
    ('Россия', 'Россия'),
    ('США', 'США'),
    ('Турция', 'Турция'),
    ('Франция', 'Франция'),
    ('Швейцария', 'Швейцария'),
    ('Южная Корея', 'Южная Корея'),
    ('Япония', 'Япония')
]

# список из механизмов часов
MECHANISM_CHOIСE = [
    ('автокварц (кинетик)', 'автокварц (кинетик)'),
    ('кварцевый', 'кварцевый'),
    ('кварцевый с солнечной подзарядкой', 'кварцевый с солнечной подзарядкой'),
    ('механические с автоподзаводом', 'механические с автоподзаводом'),
    ('механические с ручным заводом', 'механические с ручным заводом'),
    ('смарт-часы', 'смарт-часы')
]

# список из водозащитных характеристик часов
RESISTANCE_CHOIСE = [
    ('WR (минимальная защита)', 'WR (минимальная защита)'),
    ('WR20 (2 атм)', 'WR20 (2 атм)'),
    ('WR30 (3 атм)', 'WR30 (3 атм)'),
    ('WR50 (5 атм)', 'WR50 (5 атм)'),
    ('WR60 (6 атм)', 'WR60 (6 атм)'),
    ('WR100 (10 атм)', 'WR100 (10 атм)'),
    ('WR150 (15 атм)', 'WR150 (15 атм)'),
    ('WR200 (20 атм)', 'WR200 (20 атм)'),
    ('WR300 (30 атм)', 'WR300 (30 атм)'),
    ('WR330 (33 атм)', 'WR330 (33 атм)'),
    ('WR500 (50 атм)', 'WR500 (50 атм)'),
    ('WR600 (60 атм)', 'WR600 (60 атм)'),
    ('WR1000 (100 атм)', 'WR1000 (100 атм)')
]

# список из материалов корпуса часов
BODY_MATERIAL_CHOIСE = [
    ('Сталь', 'Сталь'),
    ('Платина', 'Платина'),
    ('Золото', 'Золото'),
    ('Остальное', 'Остальное'),
]

# список из материала браслета часов
CIRCLET_CHOIСE = [
    ('Алюминий', 'Алюминий'),
    ('Вольфрам', 'Вольфрам'),
    ('Золото', 'Золото'),
    ('Каучук', 'Каучук'),
    ('Керамика', 'Керамика'),
    ('Кожа', 'Кожа'),
    ('Комбинация золота и стали', 'Комбинация золота и стали'),
    ('Латунь', 'Латунь'),
    ('Нержавеющая сталь без покрытия', 'Нержавеющая сталь без покрытия'),
    ('Нержавеющая сталь с покрытием', 'Нержавеющая сталь с покрытием'),
    ('Полимер', 'Полимер'),
    ('Прочее', 'Прочее'),
    ('Силикон', 'Силикон'),
    ('Текстиль', 'Текстиль'),
    ('Титан без покрытия', 'Титан без покрытия'),
    ('Титан с покрытием', 'Титан с покрытием')
]

# список из возможных цветов часов
COLOR_CHOIСE = [
    ('Бежевый', 'Бежевый'),
    ('Белый', 'Белый'),
    ('Бирюзовый', 'Бирюзовый'),
    ('Бордовый', 'Бордовый'),
    ('Бронзовый', 'Бронзовый'),
    ('Голубой', 'Голубой'),
    ('Желтый', 'Желтый'),
    ('Зеленый', 'Зеленый'),
    ('Золотистый', 'Золотистый'),
    ('Коричневый', 'Коричневый'),
    ('Красный', 'Красный'),
    ('Многоцветный', 'Многоцветный'),
    ('Мятный', 'Мятный'),
    ('Оранжевый', 'Оранжевый'),
    ('Перламутровый', 'Перламутровый'),
    ('Пудровый', 'Пудровый'),
    ('Розовый', 'Розовый'),
    ('Серебристый', 'Серебристый'),
    ('Серый', 'Серый'),
    ('Синий', 'Синий'),
    ('Фиолетовый', 'Фиолетовый'),
    ('Хаки', 'Хаки'),
    ('Черный', 'Черный'),
    ('Шампань', 'Шампань')
]

# список из возможных форм часов
CASE_SHAPE_CHOIСE = [
    ('Бочка', 'Бочка'),
    ('Круг', 'Круг'),
    ('Необычный', 'Необычный'),
    ('Овал', 'Овал'),
    ('Прямоугольник', 'Прямоугольник')
]

# список из "полов"
GENDER_CHOIСE = [
    ('Мужские', 'Мужские'),
    ('Женские', 'Женские'),
    ('Детские', 'Детские')
]

CONDITION_CHOIСE = [
    ('Новые', 'Новые'),
    ('"С пробегом"', '"С пробегом"')
]
