# import time 
# import datetime

##1

# class Clock:
#     time = datetime.datetime.now()
#     print(time.hour)
# class Alarm:
#     def turn_on(self):
#         print("Alarm turned on ")
#     def turn_off(self):
#         print("Alarm turned off")

# class AlarmClock(Clock, Alarm):
#     def set_time(self,hour,minute):
#         self.hour = hour
#         self.minute = minute    
#         if self.hour ==  Clock.time.hour and self.minute == Clock.time.minute:
#             print("Time to get up")
#         else:
#             print("Its early yet")


# alarm = AlarmClock()
# print(alarm.turn_on)
# print(alarm.set_time(int(input("hour: ")),int(input("minute: "))))
# print(alarm.turn_off)

## 2

# class Coder:
#     experience = 0
#     count_code_time=0

#     def get_info(self):
#         print("Info")

#     def coding(self):
#         return NotImplementedError

# class FrontEnd(Coder):
#     def __init__(self,languages_frontend):
#         self.languages_frontend = languages_frontend

#     def get_info(self,name):
#         print(f"{name}, language- {self.languages_frontend}, coding time {self.count_code_time}")

#     def coding(self,time):
#         self.time = time
#         Coder.count_code_time += time
#         print(Coder.count_code_time)
        
        

# class BackEnd(Coder):
#     def __init__(self,languages_backend):
#         self.languages_backend = languages_backend

#     def get_info(self,name):
#         print(f"{name}, language -{self.languages_backend}, coding time {self.count_code_time}")

#     def coding(self,time):
#         self.time = time
#         Coder.count_code_time += self.time
    

# class FullStuck(BackEnd, FrontEnd):
#     def __init__(self,languages_backend,languages_frontend):
#         BackEnd.__init__(self,languages_backend)
#         FrontEnd.__init__(self,languages_frontend)

#     def get_info(self,name):
#         print(f"{name}, language - {self.languages_backend} {self.languages_frontend}, coding time {self.count_code_time}")


# coder1 = FrontEnd('Java')
# coder1.get_info("Jane")
# coder1.coding(5)
# coder1.get_info("Jane")
# coder2 = BackEnd("Python")
# coder2.coding(2)
# coder2.get_info("Tom")
# coder3 = FullStuck('Python', 'Java')
# coder3.coding(5)
# coder3.get_info("Ben")



# import random
# from random import shuffle

# card_suit = ['\u2665', '\u2666', '\u2663', '\u2660']
# card_values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

# class Cards:
#     deck = [x + y for  x in card_suit for y in card_values]

# class Deck(Cards):
#     deck = [x + y for  x in card_suit for y in card_values]
#     def deal(self):
#         shuffle(Deck.deck)
#         random_card = random.choice(Deck.deck)
#         a = Deck.deck.index(random_card)
#         del(Deck.deck[a])
#         print(random_card)
        
        
#     def mix(self):
#         shuffle(Cards.deck)
#         print(len(Cards.deck))
        

# deck = Deck()
# deck.deal()
# deck.mix()

        
# #4

# def hackerrankInString(s):
#     target = 'hackerrank'
#     n = len(target)
    
#     i = 0
    
#     for char in s:
#         if char == target[i]:
#             i += 1
#             if i == n:
#                 return "YES"
#     return "NO"