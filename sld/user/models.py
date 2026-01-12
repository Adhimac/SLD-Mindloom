from django.db import models

# Create your models here.
class user_registration(models.Model):
    ParentName=models.CharField(max_length=25)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=75)
    phoneNumber=models.CharField(max_length=15)
    ChildName=models.CharField(max_length=25)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    standard=models.IntegerField()
    syllabus=models.CharField(max_length=10)

    def __str__(self):
        return self.ParentName


class TestResult(models.Model):
    DISORDER_CHOICES = (
        ("dysgraphia", "Dysgraphia"),
        ("discalculia", "Discalculia"),
        ("dyslexia", "Dyslexia"),
    )

    user = models.ForeignKey(user_registration, on_delete=models.CASCADE)
    disorder = models.CharField(max_length=20, choices=DISORDER_CHOICES)

    total_questions = models.IntegerField(default=10)
    answered_count = models.IntegerField(default=0)
    correct_count = models.IntegerField(default=0)
    wrong_count = models.IntegerField(default=0)
    unanswered_count = models.IntegerField(default=0)

    marks_per_question = models.IntegerField(default=5)
    score = models.IntegerField(default=0)  # correct_count * 5

    # NORMAL / PROBLEM / BORDERLINE
    status = models.CharField(max_length=20, default="BORDERLINE")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "disorder")  # ✅ only 1 attempt per disorder

    def __str__(self):
        return f"{self.user.ParentName} - {self.disorder} - {self.status}"




































        


# user/models.py


'''class Disorder(models.Model):
    name = models.CharField(max_length=100)  # e.g., Dysgraphia, Dyscalculia, Dyslexia

    def __str__(self):
        return self.name

class Question(models.Model):
    disorder = models.ForeignKey(Disorder, on_delete=models.CASCADE)
    text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1)  # 'a', 'b', or 'c'

    def __str__(self):
        return f"{self.disorder.name}: {self.text[:50]}..."

class UserAnswer(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=1)  # 'a', 'b', or 'c'
    is_correct = models.BooleanField()

class TestResult(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE)
    disorder = models.ForeignKey(Disorder, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    result = models.CharField(max_length=50)  # Normal / At Risk / etc.
    date_taken = models.DateTimeField(auto_now_add=True)'''
