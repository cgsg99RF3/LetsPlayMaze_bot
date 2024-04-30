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
***Архитектура:***

**1) Class Params**
```python
self.glob_sz # min из высоты и ширины окна

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

self.size # Размер клетки

self.width # Ширина стен

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

def draw(self, display): # Рисовка клетки
```
**3) Class Maze**
```python
self.params # Параметры лабиринта

self.grid # Поле лабиринта, List[width * height * cell()]
```
```python
def __init__(self, params : Params) # Инициализация

def draw(self) # Отрисовка лабиринта

def save(self) # Сохранение лабиринта
    
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

def __init__(self) # Инициализация

def move(direction, grid) # Движение игрока
```
#
**8) Class BotInterface**
```python
self.bot_token # Токен

keyboard # клавиатура

users[] # Все игроки

def __init__(self, token:str) # Инициализация по токену

@router.message(CommandStart())
async def process_start_command(message: Message) # Начать взаимодействие с ботом

@router.message(Command(commands='help'))
async def process_help_command(message: Message) # Помощь

@router.message(Command(commands='lets_play'))
async def process_play_command(message: Message) # Начать игру

@router.message(Command(commands='stop'))
async def process_stop_command(message: Message) # Остановить игру

@router.message(Command(commands='path'))
async def process_path_command(message: Message) # Показать путь

@router.message(Command(commands='new_maze'))
async def process_new_maze_command(message: Message) # Сгенерировать новый лабиринт
```
