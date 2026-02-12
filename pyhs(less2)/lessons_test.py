# brick_lwh = (250, 120, 65)  # Размеры кирпича: длина, ширина, высота (мм)


# def get_area_and_volume(
#     length: int | float, width: int | float, /, *, height: int | float | None = None
# ) -> tuple[float, float | None]:
#     """Вычисляет площадь и (опционально) объём прямоугольной поверхности.

#     Аргументы:
#         length (int | float): Длина поверхности (мм).
#         width (int | float): Ширина поверхности (мм).
#         height (int | float | None): Высота поверхности (мм), опционально.

#     Возвращает:
#         tuple[float, float | None]: Кортеж из площади (мм²) и объёма (мм³, если height задан).

#     Примечание:
#         Значения округляются до 2 знаков после запятой, используется abs().
#     """
#     area = round(abs(length) * abs(width), 2)
#     volume = None
#     if height:
#         volume = round(area * abs(height), 2)
#     return area, volume


# # Тут делайте что хотите, если нужно, лишь бы передать аргументы в вызов ниже.
# x = get_area_and_volume(*brick_lwh[:2], height=brick_lwh[2])
# print(x)  # (30000, 1950000) - правильный ответ.
# print(
#     f"Площадь горизонтальной грани {x[0]} квадратных миллиметров, "
#     f"объем {x[1]} мм кубических."
# )
# print(
#     f"Площадь горизонтальной грани {x[0] / 1_000_000} квадратных метров, "
#     f"объем {x[1] / 1_000_000_000} метров кубических."
# )
# text = f'Привет, {} Как дела'


print(tex)
