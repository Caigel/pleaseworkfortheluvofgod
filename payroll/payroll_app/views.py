from django.shortcuts import render

def payroll_form(request):
    return render(request, 'payroll_form.html')

def calculate_payroll(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rate_of_pay = float(request.POST.get('rate_of_pay'))
        hours_worked = float(request.POST.get('hours_worked'))
        total_pay = rate_of_pay * hours_worked

        context = {
            'name': name,
            'total_pay': total_pay,
        }
        
        return render(request, 'payroll_result.html', context)
    else:
        return render(request, 'payroll_form.html')

