# LetsPlayMaze Bot
***Цель:*** написать игру-прохождение лабиринтов с интерфейсом телеграм бота

***Функционал:***
- Интерфейс в виде телеграм бота
- Генерация с помощью поиска в глубину(DFS) или минимального остовного дерева(MST)
- Возможность выбрать параметры генерации 
- Возможность задать размеры лабиринта 
- Графическое отображение лабиринта
- Решение лабиринтов и отображение пути
- Возможность прохождения лабиринта
#
***Использование:***  
- Начать взаимодействие с ботом
> /start
- Начать игру
> PLAY
- Задать параметры лабиринта
> /params width height type
- Далее появляются кнопки для движения по лабиринту
- Начать прохождение лабиринта
> SOLVE
- Показать путь прохождения
> SHOW PATH
- Закончить игру
> EXIT
#
***Запуск***  
- Запуск
```bash
git clone git@github.com:cgsg99RF3/LetsPlayMaze_bot.git &&
cd LetsPlayMaze_bot &&   
git checkout development &&  
pip install -r requirements.txt &&  
python3 run_bot.py 
```
В телеграм открыть @LetsPlayMaze_bot
#
***Архитектура:***

**1) Class Params**
```python
self.width  # Высота лабиринта

self.height  # Ширина лабиринта

self.type  # Тип генерации - DFS(1)/MST(2) 

```
```python
def __init__(self, glob_sz)  
```  

**2) Class Cell**
```python
self.type # Является позицией игрока или нет

self.x # Позиция x

self.y # Позиция y

self.is_checked # Флаг, был ли алгоритм в клетке 

self.walls # List([bool]) - лист, показывает есть стена или нет

self.in_path # Принадлежит ли клетка пути прохождения
```
```python
def __init__(self, x : int, y : int)

def get_neighbours(self) -> list # Поиск непроверенных соседей

def get_used_neighbours(self, grid: list) -> list # Поиск проверенных соседей
    
def check(self) -> bool # Проверка, нужно ли идти в клетку

@staticmetod
def is_passage(first : Cell, second : Cell) # Проверка, есть ли путь между клетками

@staticmetod
def is_wall(first : Cell, second : Cell) # Проверка, есть ли стена между клетками

@staticmetod
def set_path(first, second, is_wall) # Создание/Удаление стены между клетками

```
**3) Class Maze**
```python
self.params # Параметры лабиринта

self.grid # Поле лабиринта, List[width * height * cell()]
```
```python
def __init__(self, params : Params) # Инициализация
    
@abstractmetod
def generate(self) # Генерация лабиринта (абстрактный метод)
```
**4) Class DFS_Maze(Maze)**
```python
def generate(self) # Реализация абстрактного метода
```
**5) Class MST_Maze(Maze)**
```python
def generate(self) # Реализация абстрактного метода
```

**6) Class Path**
```python
self.used # Массив проверенных вершин

self.counter # Кол-во проверенных вершин
```
```python
def __init__(self, maze : Maze) # Инициализация

def find(self) # Поиск пути
```
#
**7)Class Player** 
```python
self.id # ID игрока

self.maze # Лабиринт

self.pos # Позиция игрока

self.param # Параметры лабиринта

def __init__(self) # Инициализация

def move(self, delta) # Движение игрока

def create_maze(self, width, height, maze_type) # Генерация лабринта (интерфейс)

def check(self) # Проверка, пройден ли лабиринт

def draw(self) # Отрисовка графики для пользователя
```
#
**8) Class BotInterface**
```python
self.bot # Бот

dp # Диспечер

key_words # Сообщения для соответсвующих клеток

move_keyboard # Кнопки для движения по лабиринту

users_id = [] # Идентификаторы игроков
users = dict() # Все игроки

def __init__(self, token:str) # Инициализация по токену

@staticmethod
@dp.message(CommandStart())
async def process_start_command(message: Message) # Начать взаимодействие с ботом

@staticmethod
@dp.message(F.text == 'PLAY')
async def process_play_command(message: Message) # Начать игру  

@dp.message(F.text.startswith('/params'))  
async def process_params_command(message: Message) # Задать параметры лабиринта  
    
@staticmethod  
@dp.message(F.text == 'SOLVE')  
async def process_play_command(message: Message) # Пройти лабиринт

@staticmethod
@dp.message(F.text == '⬇️')
async def process_play_command(message: Message) # Движение вниз

@staticmethod
@dp.message(F.text == '⬆️')
async def process_play_command(message: Message) # Движение вверх

@staticmethod
@dp.message(F.text == '➡️')
async def process_play_command(message: Message) # Движение вправо
        
@staticmethod
@dp.message(F.text == '⬅️')
async def process_play_command(message: Message) # Движение влево
    
@staticmethod
@dp.message(F.text == 'SHOW PATH')
async def process_play_command(message: Message) # Показать путь
    
@staticmethod
@dp.message(F.text == 'EXIT')
async def process_play_command(message: Message) # Остановить игру

def run(self) # Запустить бота
```
#
***Использованный библиотеки:***  
- aiogram
- abc

