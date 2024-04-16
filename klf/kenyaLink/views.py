from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'base/home.html')

def contact(request):
    return render(request, 'base/contact.html')

def about(request):
    return render(request, 'base/about.html')

def faqs(request):
    return render(request, 'base/faqs.html')

#sevices
def permits(request):
    return render(request, 'services/permits.html')

def passes(request):
    return render(request, 'services/passes.html')

def visas(request):
    return render(request, 'services/visas.html')

def permanentResidency(request):
    return render(request, 'services/permanent-residency.html')

def citizenship(request):
    return render(request, 'services/citizenship.html')

#permits
def classC(request):
    return render(request, 'permits/class-c.html')
def classD(request):
    return render(request, 'permits/class-d.html')
def classG(request):
    return render(request, 'permits/class-g.html')
def classI(request):
    return render(request, 'permits/class-i.html')
def classK(request):
    return render(request, 'permits/class-k.html')
def classM(request):
    return render(request, 'permits/class-m.html')

#passes
def dependantPass(request):
    return render(request, 'passes/dependant-pass.html')
def extensionPass(request):
    return render(request, 'passes/extension-pass.html')
def reEntryPass(request):
    return render(request, 'passes/re-entry-pass.html')
def specialPass(request):
    return render(request, 'passes/special-pass.html')
def studentPass(request):
    return render(request, 'passes/student-pass.html')

#permanet residency
def categoryA(request):
    return render(request, 'permanent-residency/category-a.html')
def categoryB(request):
    return render(request, 'permanent-residency/category-b.html')
def categoryC(request):
    return render(request, 'permanent-residency/category-c.html')
def categoryD(request):
    return render(request, 'permanent-residency/category-d.html')




