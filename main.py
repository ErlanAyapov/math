from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

# Глобальные настройки
Window.size = (420, 500)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = "Product by: Erlan Ayapov"

def int_or_float(integer, array):
	for x in range(1, integer + 1, 1):
		if integer % x == 0:
			array.append(x)

def int_valid(int_1b, int2b):
	array_1 = []
	array_2 = []
	error = ''
	res = []
	int_1 = int(int_1b)
	int_2 = int(int2b)

	if int_1 > 1 and int_2 > 1:
		int_or_float(integer = int_1, array = array_1)
		int_or_float(integer = int_2, array = array_2)

		for i_1 in range(0, len(array_1)):
			for i_2 in range(0, len(array_2)):
				if array_1[i_1] == array_2[i_2]:
					res.append(array_2[i_2])
	else:
		error = '1 ден үлкен сан енгіз!'

	return res 


def eyob(int1, int2):
	int1 = int(int1)
	int2 = int(int2)
	res = 0
	for i in range(1, int2 + 1, 1):
		res = int1 * i 
		if res % int2 == 0:
			break
	return res


class MyApp(App):
	
	# Создание всех виджетов (объектов)
	def __init__(self):
		super().__init__()
		self.cols = 2
		self.label = Label(text='')
		self.miles = Label(text='Ортақ бөлім', size_hint=(1, .1),)
		self.metres = Label(text='Қысқарады', size_hint=(1, .1),)
		
		self.input_data = TextInput(hint_text='Бірінші мәнді енгіз', size_hint=(1, .1), multiline=False)
		self.input_data_1 = TextInput(hint_text='Екінші мәнді енгіз', size_hint=(1, .1), multiline=False)
		self.input_data_1.bind(text=self.on_text) # Добавляем обработчик события

	# Получаем данные и производит их конвертацию
	def on_text(self, *args):
		data = self.input_data.text
		data1 = self.input_data_1.text
		if data1.isnumeric():
			self.miles.text = 'Ортақ бөлім: ' + str(eyob(int1 = data, int2 = data1))
			self.metres.text = 'Қысқарады: ' + str(int_valid(int_1b = data, int2b = data1))
			
		else:
			self.input_data.text = ''

	# Основной метод для построения программы
	def build(self):
		# Все объекты будем помещать в один общий слой
		box = BoxLayout(orientation='vertical', spacing=10)
		# box.add_widget(self.label)
		box.add_widget(self.input_data)
		box.add_widget(self.input_data_1)
		box.add_widget(self.miles)
		box.add_widget(self.metres)
		box.add_widget(self.label)

		# box.add_widget(self.santimetres)

		return box


# Запуск проекта
if __name__ == "__main__":
	MyApp().run()