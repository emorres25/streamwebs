from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from streamwebs.forms import UserForm, UserProfileForm


# Create your views here.
def index(request):
    return HttpResponse("Hey, you've reached the index.")


def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context.push(
            {
                'user_form': user_form,
                'profile_form': profile_form,
                'registered': registered
            }
    )

    return render_to_response(
            'streamwebs/register.html', context)
