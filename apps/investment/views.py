import io

from django.contrib.auth import get_user
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from xhtml2pdf import pisa

from .forms import InvestmentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Investment
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4


#
# class InvestmentListView(ListView):
#     paginate_by = 2
#     model = Investment


@login_required(login_url="/login/")
# def invest(request):
#     data = Investment.objects.filter(investment_user_id=request.user.id)
#     user_name = get_user(request)
#     return render(request, "investment/investments.html", {'investments': data})

@login_required(login_url="/login/")
def invest(request):
    data = Investment.objects.filter(investment_user_id=request.user.id)
    total=0
    for a in data:
        total = total+int(a.investment_amount)
    paginator = Paginator(data, 5)
    user_name = get_user(request)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "investment/investments.html", {'investments': page_obj, 'total': total})


@login_required(login_url="/login/")
def viewclientInvestment(request, pk):
    data = Investment.objects.filter(investment_user_id=pk) & Investment.objects.filter(investment_agent_id=request.user.id)

    total=0
    for a in data:
        total = total + int(a.investment_amount)

    paginator = Paginator(data, 5)
    user_name = get_user(request)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "investment/clientinvestments.html", {'investments': page_obj, 'total': total})


# generate pdf
class UserListView(ListView):
    model = Investment
    template_name = '/invest/'


def user_check(request):
    if (request.user.is_staff == 1):
        return redirect("/agent/")
    else:
        return redirect("/invest/")


def users_investment_pdf_view(request, *args, **kwargs):
    data = Investment.objects.filter(investment_user_id=request.user.id)
    # pk = kwargs.get('pk')
    # user = get_object_or_404(Investment, pk=pk)
    total=0
    for a in data:
        total = total + int(a.investment_amount)

    template_path = 'investment/generate_pdf.html'
    context = {'investments': data, 'total': total}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # to directly download the pdf we need attachment
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # to view on browser we can remove attachment
    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def agent_client_investment_pdf_view(request, *args,pk):
    data = Investment.objects.filter(investment_user_id=pk) & Investment.objects.filter(investment_agent_id=request.user.id)
    total=0
    for a in data:
        total = total + int(a.investment_amount)

    # user = get_object_or_404(Investment, pk=pk)

    template_path = 'investment/generate_pdf.html'
    context = {'investments': data, 'total': total}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # to directly download the pdf we need attachment
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # to view on browser we can remove attachment
    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def venue_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    # venues = Investment.objects.filter(investment_user_id=request.user.id)
    # Finish Up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='venue.pdf')


@login_required(login_url="/login/")
def viewfamilyinvestments(request, pk):
    data = Investment.objects.filter(investment_user_id=pk)
    paginator = Paginator(data, 5)
    user_name = get_user(request)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "investment/familyinvestments.html", {'investments': page_obj})


@login_required(login_url="/login/")
def addclientInvestForm(request, pk):
    if request.method == 'POST':
        user_name = get_user(request)
        form = InvestmentForm(request.POST, user_name)
        if form.is_valid():
            result = form.save(commit=False)
            result.investment_user_id = pk
            print(result.investment_user_id)
            result.investment_agent_id = request.user.id
            result.save()
            return redirect('/agent')
        else:
            print(form.errors)
    else:
        form = InvestmentForm()
    return render(request, "investment/addclientInvestment.html", {'form': form})


@login_required(login_url="/login/")
def addInvestForm(request):
    if request.method == 'POST':
        user_name = get_user(request)
        form = InvestmentForm(request.POST, user_name)
        if form.is_valid():
            result = form.save(commit=False)
            result.investment_user_id = request.user.id
            result.save()
            return redirect('/invest')
        else:
            print(form.errors)
    else:
        form = InvestmentForm()
    return render(request, "investment/addInvestment.html", {'form': form})


@login_required(login_url="/login/")
def updateInvestForm(request, pk):
    article = Investment.objects.get(pk=pk)

    if request.method == 'POST':
        form = InvestmentForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('/invest')
    else:
        form = InvestmentForm(instance=article)
    return render(request, "investment/addInvestment.html", {'form': form})


@login_required(login_url="/login/")
def updateClienytInvestForm(request, pk):
    article = Investment.objects.get(pk=pk)

    if request.method == 'POST':
        form = InvestmentForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('/agent')
    else:
        form = InvestmentForm(instance=article)
    return render(request, "investment/addclientInvestment.html", {'form': form})


@login_required(login_url="/login/")
def deleteInvest(request, pk):
    article = Investment.objects.get(pk=pk)
    article.delete()
    return redirect('/invest')

def agentdeleteInvest(request, pk):
    article = Investment.objects.get(pk=pk)
    article.delete()
    return redirect('/agent')