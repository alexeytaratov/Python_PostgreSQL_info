host = 'localhost' # сюда пишем сервак
user = 'postgres' # сюда пишем имя пользователя в PostgreSQL
password = 'aboba1488' # сюда пишем типа пароль от пользователя баз данных
db_name = 'test2' # сюда пишем имя базы данных
port = 5432 # сюда пишем порт по дефолту
connection = None # Это переменная, которая будет хранить информацию для подключения к базе данных. (значение обязательно)
cursor = None # Это переменная, которая может помочь выполнить любую операцию из СКЛ. (значение обязательно)
              # Он как бы хранит значения, которые будут возвращены из этих операций СКЛ (делается с помощью метода cursor())