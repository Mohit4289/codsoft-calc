from django.shortcuts import render

def home(request):
    c = ''
    try:
        if request.method == 'POST':
            n1 = float(request.POST.get('firstValue'))
            n2 = float(request.POST.get('secondValue'))
            n3 = request.POST.get('operator')
            if n3 == "+":
                c = n1 + n2
            elif n3 == "-":
                c = n1 - n2
            elif n3 == "*":
                c = n1 * n2
            elif n3 == "/":
                if n2 != 0:
                    c = n1 / n2
                else:
                    c = "Cannot divide by zero"
            else:
                c = "Invalid operator"
    except ValueError:
        c = "Invalid input"
    except Exception as e:
        c = str(e)

    return render(request, 'home.html', {'c': c})
