from django.shortcuts import render, get_object_or_404, reverse
# from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from django.contrib.messages import get_messages
from django.http import HttpResponseRedirect
from .models import Post, Comment

from .forms import CommentForm

# Create your views here.


class PostList(generic.ListView):
    # model = Post

    # queryset = Post.objects.all()
    # queryset = Post.objects.filter(author=3)
    # queryset = Post.objects.order_by('created_on')
    queryset = Post.objects.order_by('-created_on')
    # queryset = Post.objects.filter(status=1)
    # template_name = "post_list.html"
    template_name = "blog/index.html"
    paginate_by = 10


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post..
    ``comment_form``
        an instance of :form: blog.CommentForm
    **Template:**

    :template:`blog/post_detail.html`
    """
    # print(slug+'-'+str(1))

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        print("Received a POST request:", request.POST)
        text = request.POST.get('body')
        print('comment_text= ', text)
        print("User:", request.user)
        comment_form = CommentForm(data=request.POST)
        if text.isdigit():
            messages.add_message(request, messages.INFO, 'digits')
        elif comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            #messages.success(request, f'Removed {product.name} from your bag')
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
        else:
            messages.add_message(request, messages.ERROR, 'Error')
        print('messages.SUCCESS: ', messages.SUCCESS)
        print('messages.SUCCESS: ', messages.success)
        storage = get_messages(request)
        for message in storage:
            print('message.level>>>>', message.level)
            print('message.tags>>>>', message.tags)
    #print('messages.SUCCESS-------->', messages.SUCCESS)
    comment_form = CommentForm()
    #print("About to render template:", request.GET)
    #print("User:", request.user)
    #print("User2:", request.user.email)
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "coder": "kas",
        },
    )


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit
    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    **Context**

    ``comment``
        A single comment related to the post
    ``comment_form``
        an instance of :form: blog.CommentForm


    """
    # print('slug: '+slug)
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.
    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
