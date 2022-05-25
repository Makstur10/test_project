ok_soups = [
    'Вегетерианские супы',
    'Супы с крупами',
    'Фруктовые супы',]

ok_bread = [
    'Бессолевой хлеб',
    'Блинчики без соли',
    'Оладьи на дрожжах без соли',]

ok_meat_and_poultry = [
    'Нежирная говядина',
    'Нежирная свинина',
    'Нежирная телятина',
    'Нежирная птица',
    'Язык отварной',
    'Курица',
    'Индейка',
    'Кролик',
    'Отварное мясом',
    'Запеченное мясо',]

ok_fish = [
    'Нежирная (судак, серебристый хек, навага, треска, щука, сазан)',
    'Отварная',
    'Отварная с последующим запеканием',
    'Фаршированная',
    'Заливная после отваривания',]

ok_milk = [
    'Молоко',
    'Сливки',
    'Масло сливочное',
    'Кисломолочные напитки',
    'Творог',
    'Творожные блюда с морковью, яблоками, рисом',
    'Сметана',
    'Яйца до 2 в день при уменьшении мяса, рыбы или творога',]

ok_groats = [
    'Рис',
    'Гречка',
    'Саго',
    'Кукурузная крупа',
    'Перловая крупа',
    'Макаронные изделия',
    'Манная',
    'Пшеничная',
    'Булгур',
    'Полбяная',
    'Овсяная',
    'Ячменная',
    'Амарантовая',]

ok_vegetables_and_fruits = [
    'Картофель',
    'Перец',
    'Помидор',
    'Огурец',
    'Зелень',
    'Любые другие овощи',]

ok_other = [
    'Фрукты и ягоды (сырые, вареные)',
    'Компот',
    'Кисель',
    'Желе натуральное',
    'Мед',
    'Варенье',
    'Фруктовое мороженое',
    'Ванилин',
    'Корица',
    'Лимонная кислота',
    'Уксус',
    'Отвар шиповника',]

ok_food = [
    ok_soups,
    ok_bread,
    ok_meat_and_poultry,
    ok_fish,
    ok_milk,
    ok_groats,
    ok_vegetables_and_fruits,
    ok_other]

stop_soups = [
    'Мясные',
    'Рыбные',
    'Грибные',
    'Бульоны из бобовых',]

stop_bread = [
    'Хлеб обычной выпечки',
    'Мучные изделия с добавлением соли',]

stop_meat_and_poultry = [
    'Жирные сорта',
    'Жареные блюда без отваривания',
    'Тушеные блюда без отваривания',
    'Колбасы',
    'Сосиски',
    'Копчености',
    'Мясные консервы',
    'Свиное сало - ограниченно',]

stop_fish = [
    'Жирные виды',
    'Соленая',
    'Копченая',
    'Икра',
    'Рыбные консервы',]

stop_milk = ['Сыры']

stop_groats = [
    'Фасоль',
    'Горох',
    'Чечевица',
    'Нут',
    'Маш',]

stop_vegetables_and_fruits = [
    'Бобовые',
    'Лук',
    'Чеснок',
    'Редька',
    'Редис',
    'Щавель',
    'Шпинат',
    'Соленые овощи',
    'Маринованные овощи',
    'Квашеные овощи',
    'Грибы',]

stop_other = [
    'Фаст-фуд',
    'Шоколад',
    'Перец',
    'Горчица',
    'Хрен',
    'Кофе',
    'Какао',
    'Минеральная вода, богатая Na',]

stop_food = [
    stop_soups,
    stop_bread,
    stop_meat_and_poultry,
    stop_fish,
    stop_milk,
    stop_groats,
    stop_vegetables_and_fruits,
    stop_other]

breakfast_and_desserts = [
    'Котлеты морковно-яблочные',
    'Каши молочные',
    'Творог со сметаной',
    'Вареные яйца',
    'Печеные яблоки',
    'Печеные груши',
    'Печеная тыква',
    'Морковные котлеты со сметаной',
    'Омлет']

main_dishes = [
    'Овощной суп',
    'Рисовый суп',
    'Гречневый суп',
    'Картофельная запеканка с мясом',
    'Плов с нежирным мясом',
    'Гречневая каша',
    'Рисовая каша',
    'Булгур',
    'Ячменная каша',
    'Пшеничная каша',
        'Овощной суп',
    'Отварная рыба',
    'Отварное мясо',
    'Картофельное пюре',
    'Отварная кукуруза',
    'Рагу с овощами',
    'Соте с овощами',]

drinks = [
    'Отвар шиповника',
    'Чай',
    'Компот',
    'Узвар',
    'Кисель',
    'Кефир',
    'Ряженка',
    'Молоко',]


def dishes():
    input('1. Если хотите узнать список разрешенных блюд, введите цифру "1"\n',
          '2. Если хотите узнать список запрещенных блюд, введите цифру "2"\n')
