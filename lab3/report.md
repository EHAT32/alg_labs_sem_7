# ЛР 3. Алгоритм работы с графами (моделирование транспортной системы)

## Цель

Познакомить студента с инструментами, направленными на решение задач, использующих графовые модели.

## Задача 

Моделирование сложных транспортных процессов города, выявление узких участков, а также
формирование предложений по оптимизации.

## Транспортная модель города

Перекрёстки задаются графом:

Для каждой вершины (перекрёстка) известны её координаты (x, y), а также номера вершин, с которыми они имеют дороги. Заметим, что граф является направленным: из вершины 1 в 2 может идти дорога, а из 2 в 1 необязательно.

Все объекты в модели реализованы отдельными классами.

Класс ```Road``` задаёт объект дороги, каждая дорога хранит в себе автомобили, которые едут по ней.

Класс ```Vehicle``` задаёт объект машины. Машина имеет координату, скорость и маршрут.

Класс ```VehicleGenerator``` позволяет генерировать автомобили с заданной частотой и маршрутом.

Класс ```TrafficSignal``` реализует светофоры. У светофоров есть свой цикл красного и зелёного цветов.

Класс ```Simulator``` создаёт саму симуляцию, внутри которой обновляются параметры всех созданных объектов каждые ```dt``` секунд.
Внутри класса реализован метод ```createRoadsFromGraph```. На вход подаётся граф из перекрёстков. Из них создаются все дороги.

Класс ```Window``` отрисовывает симуляцию.

## Задача 1 

Определить ТОП-10 самых загруженных участков между перекрёстками, а также время на "рассасывание" этого затора

## Решение

Для удобства было решено просто вывести загруженность всех дорог. Может возникнуть ситуация, что на некоторых дорогах будет +/- одинаковое число автомобилей, если их количество на этих дорогах будет постоянно меняться, то и дороги будут быстро перемещаться в топе, из-за чего информация становится менее читаемой.

В данной модели рассасывание определяется легко. Машины разгоняются и останавливаются практически мгновенно, так что нужно рассчитать время, когда последняя машина в ряду проедет через дорогу.