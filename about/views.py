from django.shortcuts import render
from django.contrib import messages
from .models import About

from .forms import CollaborateForm

# Create your views here.


def about_me(request):
    """
    Renders the most recent info on the website author
    and allows user collaboration requests
    displays an individual instance of :model: `about.About`.
    **Context**
    ``about``
        The most recent instance of  :model: `about.About`.
    ``collaborate_form``
        An instance of :form: `about.CollaborateForm`.
    **Template:**
    :template: `about/about.html`.

    """

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Collaboration request received! I endeavour to respond within 2 working days."
            )

    about = About.objects.all().order_by("-updated_on").first()

    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )

#print('clean_time Admin starts--')
#print('clean_time:', time_obj, 'with', tt, 'equal:', time_obj == tt)

"""
print('---------------------------------')
print('1--data:', reservation_form.data)
print('1--cleaned-data:', reservation_form.cleaned_data)
print('1--date: ', reservation_form.cleaned_data['date'], 'type', type(reservation_form.cleaned_data['date']))
print('1--time: ', reservation_form.cleaned_data['time'], 'type', type(reservation_form.cleaned_data['time']))
print('---------------------------------')


print('---------------------------------')
print('2--data:', reservation_form.data)
print('2--cleaned-data:', reservation_form.cleaned_data)
print('---------------------------------')
print("------Errors", reservation_form.errors)
print("------Errors>>", reservation_form.errors.as_json())



"""

# class ReservationListView(ListView):

"""""

from django.views.generic import ListView, CreateView, TemplateView

class ReservationList(ListView):
    # model = Reservation
    context_object_name = 'reservations'
    # queryset = Reservation.objects.all()
    # queryset = Reservation.objects.filter(name='jamal')
    queryset = Reservation.objects.all().order_by("-date")
    template_name = "booking/index.html"
    #paginate_by = 6
    

"""
"""
class ResevationCreateView(CreateView):
    model = Reservation
    fields = ["name", "date", "time", "time", "notes", "user"]
"""

"""
<!--
        {% for field in reservation_form %}
          {% if field.errors %}
            <div class="error">{{ field.errors }}</div>
          {% endif %}
        {% endfor %}
        
        <p>Errors: {{ reservation_form.errors }}</p>
      -->



from datetime import timezone, timedelta
from django.utils import timezone
s=timezone.now().date() + timedelta(days=1)
n1= (timezone.now() + timedelta(days=1)).date().isoformat()
n2= (timezone.now() + timedelta(days=1)).date()
print('res1:', n1)
print('res2:', n2)

"""

