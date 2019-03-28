from django.shortcuts import render
from .google import googleimagesdownload
from .models import Gallery, SavedGallery
from TangoBlogger import settings
from django.db.models import Q
from .forms import GalleryForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from gallery.models import SavedGallery
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from TangoBlogger import settings
import os
import shutil


def test(request):
    if request.method == 'POST':
        print(request.POST)

    return render(request, 'gallery/test_gallery.html', {})


def test_api(request):
    return render(request, 'gallery/api.html', {})


@login_required
def home_gallery(request):
    gallery_form = GalleryForm()
    return render(request, 'gallery/home_gallery.html', {'gallery':gallery_form})


@login_required
def update_gallery(request, **kwargs):
    print(kwargs)

    object = SavedGallery.objects.get(pk=kwargs['pk'])
    pic_cnt = object.gallery_set.count()

    gallery_form = GalleryForm()
    return render(request, 'gallery/update_gallery.html', {
        'gallery_obj':object,
        'gallery'    :gallery_form,
        'pic_cnt'    :pic_cnt
    })


@login_required
def update_gallery_util(request, **kwargs):
    print(kwargs)

    saved_gallery = SavedGallery.objects.get(pk=kwargs['pk'])
    output_dir = 'media/downloads/' + saved_gallery.user_gallery

    if request.method == 'POST':
        print(request.POST)
        keywords = request.POST['keywords']
        size = request.POST['size']
        limit = request.POST['limit']
        specific_site = request.POST['specific_site']

        response = googleimagesdownload()  # class instantiation

        arguments = {"keywords": keywords, "limit": limit, "size": size,
                     "specific_site": specific_site, "output_directory":output_dir, "print_urls": True}  # creating list of arguments
        paths = response.download(arguments)  # passing the arguments to the function
        print(paths)  # printing absolute paths of the downloaded images
        images = response.image_names

        for i in range(len(images)):
            gallery_obj = Gallery()
            gallery_obj.owner = request.user
            gallery_obj.gallery_name = saved_gallery
            gallery_obj.image_name = images[i]
            gallery_obj.save()

        base_dir = settings.BASE_DIR
        media_dir = os.path.join(base_dir + '\\media\\downloads\\' + saved_gallery.user_gallery)
        move_dir = os.path.join(base_dir + '\\media\\downloads\\' + saved_gallery.user_gallery + '\\' +
                                str(arguments["keywords"]))

        files = os.listdir(move_dir)

        for f in files:
            shutil.move(move_dir + '\\' + f, media_dir)
        os.rmdir(move_dir)

        return HttpResponseRedirect(reverse_lazy('gallery:detail-gallery', kwargs={'pk':saved_gallery.pk}))


@login_required
def create_gallery(request):
    if request.method == 'POST':
        print(request.POST)
        keywords = request.POST['keywords']
        size = request.POST['size']
        limit = request.POST['limit']
        specific_site = request.POST['specific_site']

        response = googleimagesdownload()  # class instantiation

        arguments = {"keywords": keywords, "limit": limit, "size": size,
                     "specific_site": specific_site, "print_urls": True}  # creating list of arguments
        paths = response.download(arguments)  # passing the arguments to the function
        print(paths)  # printing absolute paths of the downloaded images
        images = response.image_names

        saved_gallery = SavedGallery()
        saved_gallery.user = request.user
        saved_gallery.user_gallery = arguments['keywords']
        saved_gallery.save()

        for i in range(len(images)):
            gallery_obj = Gallery()
            gallery_obj.owner = request.user
            gallery_obj.gallery_name = saved_gallery
            gallery_obj.image_name = images[i]
            gallery_obj.save()

        return HttpResponseRedirect(reverse_lazy('gallery:detail-gallery', kwargs={'pk':saved_gallery.pk}))


class GalleryView(LoginRequiredMixin, ListView):
    model = SavedGallery
    template_name = 'gallery/user_gallery.html'

    def get_queryset(self):
        qs = SavedGallery.objects.filter(Q(user=self.request.user))
        return qs


class GalleryDetail(LoginRequiredMixin, DetailView):
    model = SavedGallery
    template_name = 'gallery/detail_gallery.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryDetail, self).get_context_data(**kwargs)
        context['all_pics'] = Gallery.objects.filter(gallery_name_id=self.kwargs['pk'])
        context['media_url'] = 'http://127.0.0.1:8000/media/'

        context['effects'] = ['fade-up', 'fade-down', 'fade-right', 'fade-left', 'fade-up-right', 'flip-left',
                       'flip-right', 'flip-up', 'flip-down', 'zoom-in-up', 'zoom-in-down']

        return context


def delete_gallery(request):
    print(request.GET)
    return render(request, 'gallery/test_gallery.html', {})