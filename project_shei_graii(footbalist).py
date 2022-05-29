import random
index_tasadofi = random.sample(range(22), 22)
class ensan:
    def __init__(self,name):
        self.name = name




class footbalist(ensan):
    A = []
    B = []
    def sakht_tim(self):
        if len(footbalist.A) < 11:
            footbalist.A.append(self.name)
        else:
            footbalist.B.append(self.name)


bazikonan = ['حسین', 'مازیار', 'اکبر', 'نیما', 'مهدی', 'فرهاد', 'محمد', 'خشایار', 'میلاد', 'مصطفی', 'امین', 'سعید', 'پویا', 'پوریا', 'رضا', 'علی', 'بهزاد', 'سهیل', 'بهروز', 'شهروز', 'سامان', 'محسن']
for i in index_tasadofi:
    n = footbalist(bazikonan[i])
    n.sakht_tim()
    

for i in footbalist.A:
    print(i + '-A')

for i in footbalist.B:
    print(i + '-B')





