from extensions import RequestError, LogisticError
from shop import Shop
from store import Store
from request import Request

shop = Shop(
    {
        'печенька': 5,
        'гитара': 2,
    }
)
store = Store(
    {
        'печенька': 20,
        'гитара': 10,
        'барабаны': 5,
        'кофе': 10,
    }
)

locations = {
    "склад": store,
    "магазин": shop,
}


def main():
    print('\nПриветствуем и добро пожаловать в управление логистикой\n')

    while True:
        for location in locations:
            print(f'В {location} храниться:')
            print(f'{locations[location].get_items()}\n')

        print(f'Введите запрос такого типа:\n')
        print('Доставить 3 печенька из склад в магазин')
        user_input = input('Или напишите "стоп" для завершения работы\n')

        if user_input.lower() == "стоп":
            print('До свидания, хорошего дня')
            break

        try:
            request = Request(user_input)
        except RequestError as e:
            print(e.message)
            continue

        try:
            locations[request.store].remove(request.product, request.amount)
            print('Нужное количество есть на складе')
            print(f'Курьер забрал {request.amount} {request.product} со {request.store}')
            print(f'Курьер везет {request.amount} {request.product} со {request.store} в {request.shop}')
        except LogisticError as e:
            print(e.message)
        try:
            locations[request.shop].add(request.product, request.amount)
            print(f'Курьер доставил  {request.amount} {request.product} в {request.shop}')
        except LogisticError as e:
            print(e.message)
            locations[request.store].add(request.product, request.amount)
            print(f'Курьер вернул{request.amount} {request.product} в {request.store}')


main()
