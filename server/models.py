from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    solutions = models.ManyToManyField('Solutions', blank=True)
    telegram_name = models.CharField(max_length=100, blank=True)


class Course(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='photo/')
    date = models.DateField(auto_now_add=True)
    pupils = models.ManyToManyField(User, blank=True)
    category = models.ForeignKey('Subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курс'
        ordering = ['-date']


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategories(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Solutions(models.Model):
    task = models.ForeignKey('Tasks', on_delete=models.CASCADE)
    solution = models.TextField(blank=True)
    solutBool = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.task}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Tasks(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    solution = models.TextField()
    image = models.ImageField(upload_to='tasks/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    glava = models.IntegerField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-date']


class Theory(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='theory', blank=True)
    date = models.DateField(auto_now_add=True)
    pub_date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    glava = models.IntegerField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Теория'
        verbose_name_plural = 'Теории'
        ordering = ['-date']


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='comments/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    tasks = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-date']


class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='messages/', blank=True)

    def __str__(self):
        return f'{self.content}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-date']


class Tests(models.Model):
    tasks = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    test = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tasks}'

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ['-date']


class Complaints(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='Complaints/', blank=True)
    id_tasks = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    id_User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Reiting(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    reit = models.IntegerField()

    def __str__(self):
        return f'{self.reit}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
