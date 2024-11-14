from flask import render_template, request, redirect, url_for
from cart import cart

posts = []  # пустой список постов

@cart.route("/", methods=["GET", "POST"])  # маршрут "/" поддерживает методы GET и POST
def index():
    # Используем метод POST, так как информация будет отправляться. Request method сравнивает данные с HTTP-запросом.
    if request.method == 'POST':
        # функция request.form извлекает значения из соответствующих полей
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        # создаёт условие для проверки наличия данных в полях title и content
        if name and city and hobby :  # если  есть
            posts.append({'name': name, 'city': city, 'hobby': hobby, 'age': age})  # список заполняем словарями
            # использует для обновления страницы и предотвращения повторной отправки формы.
        return redirect(url_for('index'))  # с помощью фунции redirect перенаправляем пользователя на url, связанный с функцией index
        # возвращаем отрендеренный шаблон с переданными данными постов
    return render_template('blog.html', posts=posts)