from django.shortcuts import render,HttpResponse,redirect
from. import forms
from django.contrib.auth.forms import UserCreationForm
from  .import models
from django.contrib.auth.decorators import login_required
import random




# Create your views here.

def all_category(request):
    catData=models.mock_Category.objects.all().order_by('title')
    return render(request,'all_category.html',{'data':catData})

    

@login_required(login_url='login')
def category_question(request,cat_id):
    category=models.mock_Category.objects.get(id=cat_id)
    question=models.mock_Question.objects.filter(category=category).order_by('id').first()
    result=models.User_Submitted.objects.filter(user=request.user).delete()
    return render(request,'category_question.html',{'question':question,'category':category})


#  submit answer ,skip and results
@login_required(login_url='login')
def submit_answer(request,cat_id,question_id):
    if  request.method=='POST':
        category=models.mock_Category.objects.get(id=cat_id)
        question=models.mock_Question.objects.filter(category=category,id__gt=question_id).exclude(id=question_id).order_by('id').first()
        
        # submit_answer=None
        if 'Skip' in  request.POST:
            if question:
                questions=models.mock_Question.objects.get(id=question_id)
                user=request.user
                answer='Not Submitted'
                models.User_Submitted.objects.create(user=user,question=questions,Submitted_Answer=answer)
                return render(request,'category_question.html',{'question':question,'category':category})
            else:
                questions=models.mock_Question.objects.get(id=question_id)
                user=request.user
                answer='Not Submitted'
                models.User_Submitted.objects.create(user=user,question=questions,Submitted_Answer=answer)
        else:
            
            questions=models.mock_Question.objects.get(id=question_id)
            user=request.user
            answer=request.POST['answer']
            models.User_Submitted.objects.create(user=user,question=questions,Submitted_Answer=answer)
        if question:
            return render(request,'category_question.html',{'question':question,'category':category})
        else:
            result=models.User_Submitted.objects.filter(user=request.user)
            Skipped=models.User_Submitted.objects.filter(user=request.user,Submitted_Answer='Not Submitted').count()
            Attemp=models.User_Submitted.objects.filter(user=request.user).exclude(Submitted_Answer='Not Submitted').count()
            right=0
            Percentage=0
            for row in result:
                if row.question.right_opt == row.Submitted_Answer:
                    right+=1       
            # Percentage
            Percentage=(right*100)/result.count()

            return render(request,'results.html',{'result':result,'Total_skipped':Skipped,'Total_Attemp':Attemp,'Right_Ans':right,'Percentage':Percentage})
   
      
@login_required(login_url='login')   
def leaderboard (request): 
    # 
    # user=request.POST.get('user')
    # percent=request.POST.get('Percentage')
    # data=leaderboard(percent=percent,user=user)
    # data.save
    user=models.leaderboard.objects.all()
    percent=models.leaderboard.objects.all().order_by('-percent')[0:10]
    return render(request,'leaderboard.html',{'user':user,'percent':percent})
    # result=models.User_Submitted.objects.all()
    # right=0
    # Percentage=0
    # for row in result:
    #     if row.question.right_opt == row.Submitted_Answer:
    #         right+=1       
    #         # Percentage
    # Percentage=(right*100)/result.count()
    # data={'result':result,'Right_Ans':right,'Percentage':Percentage}    
    # return render(request,'leaderboard.html',data)       
    
  
def home (request):
    return render(request,'home.html')
    # return HttpResponse(request,'home')

def login (request):
    return render(request,'registration/login.html')

def register(request):
    msg=None
    form=forms.RegisterUser 
    if request.method=='POST':
        form=forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            msg="Registered Successful"
        else:
            msg="register not Successful"
    return render(request,'registration/register.html',{'form':form,'msg':msg})
