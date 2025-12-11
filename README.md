# OS Assignment - Threads, Deadlock, Semaphore
هذه الملفات توضح أمثلة مبسطة لمفاهيم المادة: threading, deadlock, semaphore.

**المحتويات**
- `threading.py`  : مثال على استخدام `threading.Thread` مع وبدون قفل (Lock) لعرض race condition.
- `deadlock.py`   : مثال يوضح كيف يحدث deadlock عند الحصول على أقفال بترتيب متعاكس.
- `semaphore.py`  : مثال على استخدام `threading.Semaphore` للحد من عدد الخيوط المتزامنة.

**ملاحظة مهمة**
- ملف `deadlock.py` قد يؤدي إلى تعليق التنفيذ (deadlock). في الكود قمت بإضافة `join` ب timeout للكشف عن تعليق بدلاً من الانتظار إلى الأبد.

## كيفية إنشاء الريبو على جهازك (خطوة بخطوة) مع 5 commit messages المطلوبة
المطلوب: 5 رسائل commit بالترتيب التالي:
1. `Initial commit`
2. `Add threading.py`
3. `Add deadlock.py`
4. `Add semaphore.py`
5. `Completion`

اتبع الخطوات التالية في التيرمينال (مفترض لديك git مثبت وحساب GitHub):

1) انسخ المجلد إلى جهازك أو افتحه هنا (مثال: ~/projects/os_assignment)

2) افتح التيرمينال داخل المجلد ثم نفذ:

    git init
    git branch -M main

3) Commit 1 - Initial commit (نضيف README فقط أولاً):

    git add README.md
    git commit -m "Initial commit"

4) Commit 2 - Add threading.py:

    git add threading.py
    git commit -m "Add threading.py"

5) Commit 3 - Add deadlock.py:

    git add deadlock.py
    git commit -m "Add deadlock.py"

6) Commit 4 - Add semaphore.py:

    git add semaphore.py
    git commit -m "Add semaphore.py"

7) Commit 5 - Completion (نجمّل كل شيء ثم نعمل commit نهائي):

    git add -A
    git commit -m "Completion"

8) إنشاء مستودع جديد على GitHub:
   - اذهب إلى https://github.com وادخل على حسابك
   - اضغط "New repository" ثم اكتب اسم (مثلاً `os-assignment`) واختر "Public" أو "Private" ثم اضغط "Create repository"

9) ربط الريبو المحلي بالريبو على GitHub ودفع (push):

    git remote add origin https://github.com/<your-username>/<repo-name>.git
    git push -u origin main

10) الآن انسخ رابط المستودع من صفحة GitHub وألصقه في المكان المطلوب (مثلاً هنا: "Upload your repo link here").

## تشغيل الأمثلة
- لتشغيل كل ملف جرب:
    python3 threading.py
    python3 deadlock.py
    python3 semaphore.py

