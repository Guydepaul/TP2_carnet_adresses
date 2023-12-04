from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from .models import Contact

def liste_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/liste_contacts.html', {'contacts': contacts})

def details_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'contacts/details_contact.html', {'contact': contact})

def ajout_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:liste_contacts')
    else:
        form = ContactForm()
    
    return render(request, 'contacts/ajout_contact.html', {'form': form})
