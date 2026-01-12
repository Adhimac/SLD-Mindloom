from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *

# Create your views here.



def userreg(request):
    if request.method=="POST":
        ParentName=request.POST.get("ParentName")
        email=request.POST.get("Email")
        password=request.POST.get("password")
        ConfirmPassowrd=request.POST.get("ConfirmPassowrd") 
        phoneNumber=request.POST.get("phoneNumber")
        ChildName=request.POST.get("ChildName")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        standard=request.POST.get("standard")
        syllabus=request.POST.get("syllabus")
        if password==ConfirmPassowrd:
            if  user_registration.objects.filter(email=email).exists():
                messages.info(request,'This Email is already exists')
            elif  user_registration.objects.filter(phoneNumber=phoneNumber).exists():
                    messages.info(request,'This Phone Number is already exists')
            else:
                userdata=user_registration(ParentName=ParentName,email=email,password=password,phoneNumber=phoneNumber,ChildName=ChildName,age=age,gender=gender,standard=standard,syllabus=syllabus)
                userdata.save()
                return redirect("userlogin")
        else:
            messages.info(request,"Password are not matching")
    return render(request,"User/userreg.html")
def userlogin(request):
    if request.method=="POST":
           try:
               ParentName=request.POST.get("Username")
               email=request.POST.get("email")
               password=request.POST.get("password")
               log=user_registration.objects.get(email=email,password=password,ParentName=ParentName)
               request.session['firstname']=log.ParentName
               request.session['id']=log.id
               return redirect("userhome")
           except user_registration.DoesNotExist:
               messages.info(request,'Invalid Login')
    return render(request,"User/userlogin.html")
def userhome(request):

    return render(request,"User/userhome.html")


QUESTIONS = {
    "dysgraphia": [
        {
            "q": "__pple",
            "options": ["B", "A", "D"],
            "answer": "A",
            "image": "sld_qimages/dysgraphia_q1_apple.png"
        },
        {"q": "Choose the correct sentence", "options": ["i like apples", "I like apples", "i like Apples"], "answer": "I like apples"},
        {
            "q": "__ose",
            "options": ["F", "G", "N"],
            "answer": "N",
            "image": "sld_qimages/dysgraphia_q3_nose.png"
        },
        {"q": "Which word has an extra letter added", "options": ["Cat", "Catt", "Cut"], "answer": "Catt"},
        {"q": "Choose correct capital letter.", "options": ["my name is ram.", "My name is Ram.", "My name is ram."], "answer": "My name is Ram."},
        {"q": "Rewrite as a question : You are ready", "options": ["Are you ready", "You are ready?", "Ready you are?"], "answer": "Are you ready"},
        {"q": "Choose the correct spelling.", "options": ["Separate", "Separate ", "Seprate"], "answer": "Separate "},  # keeping as in pdf
        {"q": "Which one is a vowel", "options": ["B", "C", "A"], "answer": "A"},
        {"q": "Which is a fruit?", "options": ["Car", "Mango", "Ball"], "answer": "Mango"},
        {"q": "Which sentence uses punctuation correctly?", "options": ["what is your name", "What is your name?", "What is your name."], "answer": "What is your name?"},
    ],

    "discalculia": [
        {"q": "What is 5 + 3?", "options": ["7", "8", "9"], "answer": "8"},
        {"q": "What is 10 – 4?", "options": ["5", "7", "6"], "answer": "6"},
        {"q": "Which number is bigger?", "options": ["12", "9", "6"], "answer": "12"},
        {"q": "What comes after 19?", "options": ["18", "20", "21"], "answer": "20"},
        {"q": "How many tens are there in 30?", "options": ["2", "3", "4"], "answer": "3"},
        {"q": "Find the next five series of number after 12.", "options": ["18,19,20,21,22", "13,14,15,16,17", "6,7,8,9,10,11"], "answer": "13,14,15,16,17"},
        {
            "q": "Which shape is round?",
            "options": ["Square", "Triangle", "Circle"],
            "answer": "Circle",
            "image": "sld_qimages/discalculia_q7_shape.png"
        },
        {
            "q": "Count the apple shown in the picture and choose the correct answer.",
            "options": ["9", "5", "6"],
            "answer": "6",
            "image": "sld_qimages/discalculia_q8_apples.png"
        },
        {"q": "Choose the number format of seventeen.", "options": ["17", "70", "7"], "answer": "17"},
        {"q": "Choose the correct number name of the digit 9.", "options": ["ten", "nine", "seven"], "answer": "nine"},
    ],

    # Dyslexia: we are taking 10 questions from your pdf pages 1-2 :contentReference[oaicite:6]{index=6}
    "dyslexia": [
        {"q": "Which one is a letter?", "options": ["7", "@", "A"], "answer": "A"},
        {"q": "Which word is correct?", "options": ["frend", "friend", "freind"], "answer": "friend"},
         {
            "q": "Identify the picture.",
            "options": ["Bat", "Ball", "log"],
            "answer": "Ball",
            "image": "sld_qimages/dyslexia_q3_ball.png"
        },
        {"q": "Which word starts with /b/ sound?", "options": ["cat", "ball", "sun", "pen"], "answer": "ball"},
        {"q": "Visiting the Zoo: a) Yash went to the ____", "options": ["zoo", "park"], "answer": "park"},
        {"q": "Visiting the Zoo: b) At the zoo, Yash saw many ____", "options": ["cars", "animals"], "answer": "animals"},
        {"q": "Visiting the Zoo: c) The elephants were very ____", "options": ["big", "small"], "answer": "big"},
         {
            "q": "Identify the picture below.",
            "options": ["van", "fan", "can"],
            "answer": "fan",
            "image": "sld_qimages/dyslexia_q8_fan.png"
        },
        {"q": "Choose the correct spelling", "options": ["Bicycal", "Bicycle", "Bycycle"], "answer": "Bicycle"},
        {
            "q": "Identify the action",
            "options": ["run", "ran", "running"],
            "answer": "running",
            "image": "sld_qimages/dyslexia_q9_kid.png"
        },
    ],
}

DISORDER_ORDER = ["dysgraphia", "discalculia", "dyslexia"]


# -----------------------------
# AUTH HELPERS
# -----------------------------
def get_logged_user(request):
    uid = request.session.get("id")
    if not uid:
        return None
    try:
        return user_registration.objects.get(id=uid)
    except user_registration.DoesNotExist:
        return None



# -----------------------------
# NEW: Screening Flow
# -----------------------------
def start_screening(request):
    user = get_logged_user(request)
    if not user:
        return redirect("userlogin")

    # reset attempt flow
    request.session["screening_index"] = 0
    return redirect("take_test", disorder_name=DISORDER_ORDER[0])



def take_test(request, disorder_name):
    user = get_logged_user(request)
    if not user:
        return redirect("userlogin")

    if disorder_name not in QUESTIONS:
        messages.info(request, "Invalid test selected.")
        return redirect("userhome")

    # ✅ If already attempted, go to next test (not summary immediately)
    if TestResult.objects.filter(user=user, disorder=disorder_name).exists():
        index = DISORDER_ORDER.index(disorder_name)
        next_index = index + 1

        if next_index < len(DISORDER_ORDER):
            return redirect("take_test", disorder_name=DISORDER_ORDER[next_index])

        return redirect("screening_summary")

    qs = QUESTIONS[disorder_name]
    return render(request, "User/take_test.html", {
        "disorder_name": disorder_name,
        "questions": qs,
    })


"""def take_test(request, disorder_name):
    user = get_logged_user(request)
    if not user:
        return redirect("userlogin")

    if disorder_name not in QUESTIONS:
        messages.info(request, "Invalid test selected.")
    return redirect("userhome")

    # if already attempted
    if TestResult.objects.filter(user=user, disorder=disorder_name).exists():
        messages.info(request, f"You already attempted {disorder_name}. Showing summary.")
        return redirect("screening_summary")

    if TestResult.objects.filter(user=user, disorder=disorder_name).exists():
    # move to next test instead of summary
    index = DISORDER_ORDER.index(disorder_name)
    next_index = index + 1

    if next_index < len(DISORDER_ORDER):
        return redirect("take_test", disorder_name=DISORDER_ORDER[next_index])

    return redirect("screening_summary")

    qs = QUESTIONS[disorder_name]
    return render(request, "User/take_test.html", {
        "disorder_name": disorder_name,
        "questions": qs,
    })

"""
def submit_test(request, disorder_name):
    user = get_logged_user(request)
    if not user:
        return redirect("userlogin")

    if request.method != "POST":
        return redirect("take_test", disorder_name=disorder_name)

    if disorder_name not in QUESTIONS:
        return redirect("userhome")

    qs = QUESTIONS[disorder_name]
    total = len(qs)

    answered = 0
    correct = 0
    wrong = 0

    # store user answers (optional)
    user_answers = {}

    for i, item in enumerate(qs):
        key = f"q{i}"
        selected = request.POST.get(key)  # None if not selected
        user_answers[key] = selected

        if selected is None:
            continue

        answered += 1
        if selected == item["answer"]:
            correct += 1
        else:
            wrong += 1

    unanswered = total - answered
    score = correct * 5

    # YOUR RULE:
    # Normal if correct >= 8 of 10
    # Problem if unanswered >= 3
    # Otherwise borderline
    # (If total is not 10 in future, still using 8 as default target is not fair,
    # so we convert: 80% of total, minimum 8 if total==10)
    required_correct = 8 if total == 10 else int(round(total * 0.8))

    # if correct >= required_correct:
    #     status = "NORMAL"
    # elif unanswered >= 3:
    #     status = "PROBLEM"
    # else:
    #     status = "BORDERLINE"
    if correct >= 8:
        status = "NORMAL"
    elif correct <= 5 or unanswered >= 3:
         status = "PROBLEM"
    else:
        status = "BORDERLINE"

    # Save result (1 per disorder)
    TestResult.objects.update_or_create(
        user=user,
        disorder=disorder_name,
        defaults={
            "total_questions": total,
            "answered_count": answered,
            "correct_count": correct,
            "wrong_count": wrong,
            "unanswered_count": unanswered,
            "marks_per_question": 5,
            "score": score,
            "status": status,
        }
    )

    # redirect to next test
    index = request.session.get("screening_index", 0)
    index += 1
    request.session["screening_index"] = index

    if index < len(DISORDER_ORDER):
        return redirect("take_test", disorder_name=DISORDER_ORDER[index])

    return redirect("screening_summary")


def screening_summary(request):
    user = get_logged_user(request)
    if not user:
        return redirect("userlogin")

    results = TestResult.objects.filter(user=user).order_by("created_at")

    # which disorders are problem
    problem_disorders = [r.disorder for r in results if r.status == "PROBLEM"]

    return render(request, "User/screening_summary.html", {
        "results": results,
        "problem_disorders": problem_disorders,
    })



def reset_attempts(request):
    user = get_logged_user(request)
    if not user:
        return redirect("userlogin")

    # delete all 3 disorder results for this logged-in user
    TestResult.objects.filter(user=user).delete()

    # reset screening flow index
    request.session["screening_index"] = 0

    messages.success(request, "Your test attempts have been reset. You can take the screening again.")
    return redirect("userhome")












def doctors(request):
    return render(request,"User/doctors.html")
def doctor1(request):
    return render(request,"User/doctor1.html")
def booking(request):
    return render(request,"User/booking.html")
def appointment(request):
    return render(request,"User/appointment.html")
def About(request):
    return render(request,"User/About.html")