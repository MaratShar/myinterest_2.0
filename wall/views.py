from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Image, Like
from django.core.mail import send_mail

def wall_view(request):
    content = {}
    all_images = Image.objects.all()
    content["images"] = all_images
    if request.user.is_authenticated:
        likes = Like.objects.filter(user = request.user)
        liked_images = []
        for like in likes:
            liked_images.append(like.image)
        content["likes"] = liked_images
    return render(request, 'wall/wall.html', content)


@login_required
def upload_view(request):
    if request.method == "POST":
        image = request.FILES["image"]
        discription = request.POST["discription"]
        new_image = Image.objects.create(author = request.user, image = image, discription = discription)
        return HttpResponseRedirect(reverse("upload_image"))
    return render(request, 'wall/upload_image.html')

@login_required
def like_request(request, image_id):
    if request.method == "GET":
        user = request.user
        image = Image.objects.get(pk=image_id)
        Like.objects.create(user = user, image = image)
        image.likes += 1
        image.save()
        return JsonResponse({'response': 'like'})


@login_required
def unlike_request(request, image_id):
    if request.method == "GET":
        user = request.user
        image = Image.objects.get(pk=image_id)
        like = Like.objects.get(user = user, image = image)
        like.delete()
        image.likes -= 1
        image.save()
        return JsonResponse({'response': 'unlike'})



def send_me_a_message(request):
    send_mail("Test message", "Test", None, ["maratshar2@gmail.com"], fail_silently=False)
    return JsonResponse({'response': 'mail_send'})