from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact

def add_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        Contact.objects.create(name=name, phone_number=phone, email=email)
        return redirect('view_contacts')
    return render(request, 'contactapp/add_contact.html')
def view_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contactapp/view_contacts.html', {'contacts': contacts})
def edit_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        contact.name = request.POST.get('name')
        contact.phone_number = request.POST.get('phone')
        contact.email = request.POST.get('email')
        contact.save()
        return redirect('view_contacts')
    return render(request, 'contactapp/edit_contact.html', {'contact': contact})
def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    return redirect('view_contacts')
