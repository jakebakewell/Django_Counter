from django.shortcuts import render, redirect

def index(request):
    if 'number_counter' not in request.session:
        request.session['number_counter'] = 0
    if 'visit_counter' not in request.session:
        request.session['visit_counter'] = 0
    else:
        request.session['visit_counter'] += 1
        print("Key named counter exists")
    return render(request, 'index.html')
def destroy(request):
    del request.session['visit_counter']
    del request.session['number_counter']
    return redirect('/')
def add_number(request):
    request.session.number = request.POST['increment_number']
    context = {
        "add_number_on_template" : request.session.number
    }
    request.session['number_counter'] += int(request.session.number)
    return redirect('/', context)