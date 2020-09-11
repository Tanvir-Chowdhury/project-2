# Method 1
'''def week(i):
    switch = {
        1 : "Sat",
        2 : "sun"      
    }
    return switch.get(i, "Invalid day")

print(week(6))'''


# Method 2

class Switcher(object):
    def indirect(self,i):
        method_name='number_'+str(i)
        method=getattr(self,method_name,lambda :'Invalid')
        return method()
    def number_0(self):
        return 'zero'
    def number_1(self):
        return 'one'
    def number_2(self):
        return 'two'

s=Switcher()
print(s.indirect(2))



