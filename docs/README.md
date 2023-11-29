Проект создан для вычисление площади и периметра различных геометрических фигур.

## square.py

- def area(a)

    Возвращает площадь квадрата

    	Параметры:
    		a (int): сторона квадрата

    	Возвращаемое значение:
    		(int): площадь квадрата

    Example: Параметр a = 5; Возвращаемое значение: 25. 

- def perimiter(a)

    Возвращает периметр квадрата

    	Параметры:
    		a (int): сторона квадрата

    	Возвращаемое значение:
    		(int): периметр квадрата

    Example: Параметр a = 7; Возвращаемое значение: 28. 

## circle.py

- def area(r)

    Возвращает площаль окружности

    	Параметры:
    		r (int): радиус окружности

    	Возвращаемое значение:
    		(float): площадь окружности

    Example: Параметр r = 3; Возвращаемое значение: 28.26. 


- def perimiter(r)

    Возвращает периметр окружности

    	Параметры:
    		r (int): радиус окружности

    	Возвращаемое значение:
    		(float): Периметр окружности

    Example: Параметр r = 4; Возвращаемое значение: 25.12. 

## rectangle.py

- def area(a, b)

    Возвращает площадь прямоугольника

    	Параметры:
    		a (int): длина прямоугольника
    		b (int): ширина прямоугольника

    	Возвращаемое значение:
    		(int): площадь прямоугольника

    Example: Параметр a = 2, b = 3; Возвращаемое значение: 6. 

- def perimiter(a, b)

    Возвращает периметр прямоугольника

    	Параметры:
    		a (int): длина прямоугольника
    		b (int): ширина прямоугольника

    	Возвращаемое значение:
    		(int): периметр прямоугольника

    Example: Параметр a = 2, b = 3; Возвращаемое значение: 10. 

## triangle.py

- def area(a, h)

    Возвращает площадь треугольника

    	Параметры:
    		a (int): сторона треугольника, к которой проведена высота
    		h (int): высота треугольника

    	Возвращаемое значение:
    		(float): площадь треугольника

    Example: Параметр a = 5, h = 7; Возвращаемое значение: 17.5. 

- def perimiter(a, b, c)

    Возвращает периметр треугольника

    	Параметры:
    		a (int): первая сторона треугольника
    		b (int): вторая сторона треугольника
    		c (int): третья сторона треугольника

    	Возвращаемое значение:
    		(int): периметр треугольника

    Example: Параметр a = 2, b = 3, c = 4; Возвращаемое значение: 9. 

## Tests

   SquareTestCase:

      test_zero_area(): area(0)
      test_area1(): area(5)
      test_area2(): area(70)
      test_zero_perimeter(): perimeter(0)
      test_perimeter1(): perimeter(6)
      test_perimeter2(): perimeter(8)

   CircleTestCase:

      test_zero_area(): area(0)
      test_area1(): area(5)
      test_area2(): area(98)
      test_zero_perimeter(): perimeter(0)
      test_perimeter1(): perimeter(8)
      test_perimeter2(): perimeter(24)

   RectangleTestCase:

      test_zero_area(): area(10, 0)
      test_area1(): area(12, 10)
      test_area2(): area(5, 12)
      test_zero_perimeter1(): perimeter(10, 0)
      test_zero_perimeter2(): perimeter(0, 0)
      test_perimeter1(): perimeter(16, 4)
      test_perimeter2(): perimeter(4, 6)

   TriangleTestCase:

      test_zero_area(): area(0, 5)
      test_area1(): area(5, 2)
      test_area2(): area(70, 4)
      test_zero_perimeter(): perimeter(0, 0, 0)
      test_perimeter1(): perimeter(4, 5, 8)
      test_perimeter2(): perimeter(59, 62, 6)

## History

commit f5b9d35c9be44713a1e5963a5a39a3fce3405b23 (HEAD -> new_features_409657, origin/new_features_409657)
Author: Marylague <sytinamaria1@gmail.com>
Date:   Wed Nov 22 12:56:31 2023 +0300

    update tests

commit 1677671bd066ed8d5ec6b92eb980ed83c14304a4
Author: Marylague <sytinamaria1@gmail.com>
Date:   Sun Nov 19 15:01:43 2023 +0300

    add file in tests/

commit b593707b69b6e07d2a1d4b23be0e4e25ee48875a
Author: Marylague <sytinamaria1@gmail.com>
Date:   Sun Nov 19 14:58:51 2023 +0300

    tests were added

commit 8f1b09fc603830c6920e9dec7d3e91d4a00ab81a
Author: MaryLague <sytina-m06@mail.ru>
Date:   Mon Oct 9 21:27:28 2023 +0300

    fix docs 4

commit d42246e0f824256c7b912f0bccbd08bf06e1979e
Author: MaryLague <sytina-m06@mail.ru>
Date:   Mon Oct 9 21:23:01 2023 +0300

    fix docs 3

commit 163e4a08378aafb0b9ae54935224287d1b0a5324
Author: MaryLague <sytina-m06@mail.ru>
Date:   Sun Oct 8 18:36:58 2023 +0300


commit a4c5b6f78ccc8f250ed0484ea067e936ae2e0e12
Author: MaryLague <sytina-m06@mail.ru>
Date:   Thu Sep 28 15:49:57 2023 +0300

    errors were fixed

commit b62685ef6215d77a21212cc730a084e38dbffed5
Author: MaryLague <sytina-m06@mail.ru>
Date:   Thu Sep 28 15:44:39 2023 +0300

    new file was added

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added

