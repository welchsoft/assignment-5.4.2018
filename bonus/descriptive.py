#set up the dictionary
number_names = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }

#take user input
try:
    num = int(input("Enter a number between 1 and 100: "))
except ValueError:
    print("not a valid number")

#parse through the values and select the right names from the dictionary
if int(num) > 100 or int(num) < 0:
    print("you swindled me, now results may not be accurate")

if num<20:
    print(number_names[num])
if (num < 100):
        if num % 10 == 0:
            print(number_names[num])
        else:
            print( number_names[num // 10 * 10] + ' ' + number_names[num % 10])
