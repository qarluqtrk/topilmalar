from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.forms.postform import PostModelForm
from app.models import Item


@login_required(login_url='signin')
def post_view(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to a success page or any other desired page
            return redirect('index')
    else:
        # If it's a GET request, display the form
        form = PostModelForm()
    context = {
        'form': form
    }
    return render(request, 'app/post.html', context)
