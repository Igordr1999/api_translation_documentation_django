from django.db import models
from django.utils.translation import ugettext_lazy as _


class Article(models.Model):
    """
    Documentation for a class.
    """
    title = models.CharField(max_length=100, verbose_name=_('Title'))


class Blog(models.Model):
    """
        @brief Краткое описание

        Полное описание

        Attributes:
            id: achievement identifier
            type: type of achievement
            n: amount of elementary actions enough to get achievement

    """
    section = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    text = models.CharField(max_length=100)

    def __str__(self):
        """!
        @brief Documentation for a function.

        Данная функция реализует алгоритм Евклида, при помощи которого
        находится наибольшее общее кратное у двух чисел.

        @author Igor
        @warning Необходимо тестирование
        @bug Описание бага
        @version 1.0
        @date 14.10.2018
        @pre Предварительное условие
        @todo Дописать пару функций
        @todo Протестить

        @param a Параметр 1
        @param b Параметр 2
        @return Сумму двух чисел, переданных в качестве аргументов

        Код функции выглядит следующим образом:
        @code
            int gcd(int a, int b) {
                int r;
                while (b) {
                    r = a % b;
                    a = b;
                    b = r;
                }
                return r;
            }
        @endcode
        """
        return self.title
