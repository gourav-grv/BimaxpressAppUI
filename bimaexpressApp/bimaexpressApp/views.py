from django.http import HttpResponse
from django.shortcuts import render
import os.path
from .settings import BASE_DIR
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

context = {
    'bottom_card': [{'name': 'Gourav', 'email': 'grvshrivastava@gmail.com', 'contact': '7247020941', 'status': 'single',
                     'admission_date': '18', 'email': 'grvshrivastava456@gmail.com', 'claim_amount': '12', 'tpa': '50'},
                    {'name': 'guru', 'email': 'grvshrivastava456@gmail.com', 'contact': 'xxxxxxxx', 'status': 'single',
                     'admission_date': '18', 'claim_amount': '12', 'tpa': '50'},
                    {'name': 'harsh', 'email': 'grvshrivastava456@gmail.com', 'contact': '123135135315', 'status': 'single',
                     'admission_date': '18', 'claim_amount': '12', 'tpa': '50'},
                    {'name': 'Lokesh Singhai Jain', 'email': 'grvshrivastava456@gmail.com', 'contact': '213135658', 'status': 'single',
                     'admission_date': '18', 'claim_amount': '12', 'tpa': '500000'},
                    {'name': 'Lokesh Singhai Jain', 'email': 'grvshrivastava456@gmail.com', 'contact': '213135658', 'status': 'single',
                     'admission_date': '18', 'claim_amount': '12', 'tpa': '500000'},
                    {'name': 'Lokesh Singhai Jain', 'email': 'grvshrivastava456@gmail.com', 'contact': '213135658', 'status': 'single',
                     'admission_date': '18', 'claim_amount': '12', 'tpa': '500000'},
                    {'name': 'Lokesh Singhai Jain', 'email': 'grvshrivastava456@gmail.com', 'contact': '213135658', 'status': 'single',
                     'admission_date': '18', 'claim_amount': '12', 'tpa': '500000'},
                    {'name': 'Lokesh Singhai Jain', 'email': 'grvshrivastava456@gmail.com', 'contact': '213135658', 'status': 'single',
                     'admission_date': '18', 'claim_amount': '12', 'tpa': '500000'}],
    'upper_card': [{'num': 2, 'type': 'Drafts','color':'rgb(167, 47, 67)'},
                             {'num': 3, 'type': 'Unprocessed','color':'rgb(167, 47, 67)'},
                             {'num': 1, 'type': 'NMI','color':'rgb(167, 47, 67)'},
                             {'num': 5, 'type': 'Approved','color':'rgb(167, 47, 67)'},
                             {'num': 7, 'type': 'Rejected','color':'rgb(167, 47, 67)'},
                             {'num': 3, 'type': 'Enhance Discharge','color':'rgb(167, 47, 67)'},
                             {'num': 2, 'type': 'Discharge Approved','color':'rgb(167, 47, 67)'},
                             {'num': 33, 'type': 'All Processed','color':'rgb(167, 47, 67)'}]
}


def index(request):
    return render(request, 'index.html', context)



def pageAccordian(request):
    return render(request, 'pageAccordian.html', context)