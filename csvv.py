
# # 1. Какова общая выручка от всех продаж?  
# # 2. Какой покупатель совершил больше всего покупок?  
# # 3. Какой самый дорогой проданный товар и сколько единиц было продано?  
# # 4. В какой день были наибольшие продажи?  
# # 5. Какова средняя стоимость всех проданных товаров?  
# # 6. Какой товар принес наибольшую выручку?  
# # 7. Сколько разных товаров купил каждый покупатель?  
# # 8. Какие покупатели потратили больше всего денег?  
# # 9. Кто потратил больше всего денег?  
# # 10. Какова средняя сумма покупки для каждого покупателя?  
# # 11. Сколько раз был продан каждый товар?  
# # 12. Какова минимальная и максимальная стоимость проданных товаров?  
# # 13. Какой месяц был самым прибыльным?  
# # 14. Сколько покупок было совершено в каждый день недели?  
# # 15. Какой товар покупали чаще всего?  
# # 16. Какова средняя стоимость покупки по каждому товару?  
# # 17. Какое количество уникальных товаров было продано за весь период?  
# # 18. Какова медианная стоимость всех проданных товаров?  
# # 19. Сколько покупателей совершили более 10 покупок?  
# # 20. В каком месяце покупатели тратили больше всего денег?  
# # 21. Какое количество товаров было продано на сумму более 1000?  
# # 22. Сколько покупателей купили каждый товар хотя бы один раз?  
# # 23. Какое количество покупок было совершено за последний год?  
# # 24. Какое количество покупателей купило товары более чем на 5000?  
# # 25. Какой процент от всех продаж приходится на самых активных 10% покупателей?  
# # 26. Какой товар покупали реже всего?  
# # 27. Сколько раз каждый товар был продан на сумму более 500?  
# # 28. Какова средняя стоимость покупки по каждому месяцу?  
# # 29. Сколько покупок было совершено за последние 6 месяцев?  
# # 30. Какой товар приносил наибольшую выручку каждый месяц?



# # _name = 'Emil Bilgazyev'
# # from csv import reader
# # def get_average_score(filename):
# #     result = []
# #     with open(filename) as fid:
# #         r = reader(fid)
# #         header = next(r)
# #         id_index = header.index('id')
# #         name_index = header.index('names')
# #         midterm_index = header.index('10/14/2024') 
# #         taken = [id_index, name_index, midterm_index]
# #         for i in r:
# #             try:
# #                 midterm = int(i[midterm_index])
# #             except:
# #                 midterm = 0
# #             id = i[id_index]
# #             name = i[name_index]
# #             quizzes = []
# #             for inx, j in enumerate(i):
# #                 if inx not in taken:
# #                     quizzes.append(j)
# #             quiz_scores = []
# #             for j in quizzes:
# #                 try:
# #                     score = int(j)
# #                     quiz_scores.append(score) 
# #                 except:
# #                     quiz_scores.append(0)
# #             quiz_sorted = sorted(quiz_scores, reverse=True)
# #             avg_quiz = sum(quiz_sorted[:7])/7
# #             avg = round((0.7 * avg_quiz + 0.075*midterm ) / 0.775)
# #             result.append((name, avg))
# #     return result



# from collections import defaultdict
# from csv import reader

# with open("csvv.csv") as file:
#     dat = reader(file)
#     header = next(dat)
#     data = list(dat)
    
#     customers = header.index("customer_name")
#     date = header.index("date")
#     product_name = header.index('product_name')
#     cost = header.index('cost')

#     arr = [customers, date]

#     def findSum():
#         dic = defaultdict(int)
#         for i in data:
#             dic[i[product_name]] += float(i[cost])

#         return dic
    
    
    
#     def totalSum():
#         sm = 0
#         for i in data:
#             sm+=float(i[cost])
#         return sm
#     print(totalSum())


#     def product_times():
#         dic = defaultdict(int)
#         for i in data:
#             dic[i[product_name]] += 1
#         return dic
#     print(product_times())

           


# class Animal:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     def bark(self):
#         return "the animal is barking"

# class Aibek(Animal):
#     def __init__(self, name, age, origin):
#         super().__init__(name, age)
#         self.origin = origin

#     def bark(self):
#         return "human doen't bark at all"


# a = Animal("aibek", 34)
# print(a.name)
# b  = Aibek("hello", 45, 'rusha')
# print(b.bark())
# print(b.origin)


lines = lines = ["Hello, world!\n", "Python is awesome.\n", "Line by line.\n"]


with open("abc.txt", 'w') as file:
    file.write("hello")
    file.write("world")


with open("abc.txt", "r") as file2:
    print(file2.read())