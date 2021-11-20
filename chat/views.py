from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'chat/index.html', {'title': 'ChatServer'})

def group(request, group_name):
    return render(request, 'chat/group.html', {
        'group_name': group_name,
        'title': f'ChatServer | { str.upper(group_name) }'
    })