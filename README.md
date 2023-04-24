# Examination-Portal
This is an Examination Portal Designed using Python Framework (Django)

There are two types of users: Students and Admin;<br>
The Admin is the only user that can **upload**, **delete** or **edit** Objective Questions and Answers.
And the Students are only able to Take Exams, and see their results instantly

After each student takes the exam; the Percentage, Date and GP is saved in two places(Models); temporary(StudentsTrial) and permanent(StudentsProgress).
![image](https://user-images.githubusercontent.com/101975553/234072429-55c75463-2400-49cf-876d-6311ab402991.png)


The function of the StudentsTrial is to save Students that have taken the exam for the particular session.
And the function of the StudentsProgress is to save Scores of the students and other informations.

Using TinyMce, Admin can uploaded formatted texts, images and others;
![image](https://user-images.githubusercontent.com/101975553/234071970-13c958d2-c30e-4e27-b8a1-8e697bd3e27b.png)

To run project;
1. Create a Virtual Environment on your computer
2. Go to the root directory of the Project, where you'll find **manage.py** file and run: pip install -r requirements.txt. 
This will download the dependencies of the Project into your environment
3. Run **python manage.py makemigrations**, then **python manage.py makemigrations** to create the database start working.
4. You'll need to create an Admin Profile too, so as to be able to upload questions; run **python manage.py createsuperuser** to create an account.
5. Run **python manage.py runserver** and go to **http://127.0.0.1:8000/database** to go to the admin Page or **http://127.0.0.1:8000/** to go to the home page.

In the **StartExam** model, create just one Object. There's a Checkbox there that will be used by the admin. Students can only take exam if Checkbox is active.

**Warning**: Don't upload too many images per Exam session.


