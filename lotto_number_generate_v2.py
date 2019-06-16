import random
from datetime import date


class LottoGenerator:

	count = 0
	lotto_number = ''
	
	def __init__(self,draw_number):
		self.draw_number = draw_number

	def generate_number_lotto(self):
		print('')
		print('Your Lucky pick for PCSO Lotto 6/' + str(self.draw_number))
		for x in range(1,6):
			self.lotto_number = ''
			self.count = 0
			while (self.count < 6):
				self.number_lotto = str(random.randint(1,self.draw_number))
				if self.lotto_number.find(self.number_lotto) == -1:
					self.lotto_number = self.lotto_number + ' ' + self.number_lotto
					self.count = self.count + 1
			print('Bet # {} : {}'.format(str(x),self.lotto_number))

class GetDrawNumber:
	
	days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
	
	def __init__(self,day_number):
		self.day_number = day_number
		self.day = self.days[self.day_number]

	def get_draw_number(self):

		print('Today is {}'.format(self.day))

		# Monday and Wednesday Draw
		if (self.day_number == 0) or (self.day_number  == 2):
			self.draw_number = [45,55]		

		# Tuesday Draw
		if self.day_number == 1:
			self.draw_number = [42,49,58]		

		# Thursday Draw
		if self.day_number  == 3:
			self.draw_number = [42,49]		

		# Friday
		if self.day_number  == 4:
			self.draw_number = [45,58]		

		# Saturday
		if self.day_number  == 5:
			self.draw_number = [42,55]		

		# Sunday
		if self.day_number  == 6:
			self.draw_number = [49,58]

		return self.draw_number


# #
today = date.today()
today_day = GetDrawNumber(today.weekday())
today_day_number = today_day.get_draw_number()

for number in today_day_number:
	lucky_pick = LottoGenerator(number)
	lucky_pick.generate_number_lotto()

print('')
print('Goodluck!!!!')
