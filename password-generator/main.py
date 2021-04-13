import random

chars = 'qwertyuıopğüasdfghjklşizxcvbnmöçQWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ!@#$%^&*().,?1234567890'

number = input('Kaç adet şifre oluşturulsun: ')
number = int(number)

length = input('Şifre kaç basamak uzunluğunda olsun: ')
length = int(length)

print('Şifreleriniz: ')

for pwd in range(number):
  passwords = ''
  for c in range(length):
    passwords += random.choice(chars)
  print(passwords)
