def user_group(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            user_group = 'Superuser'
        elif request.user.is_staff:
            user_group = 'Staff'
        else:
            user_group = 'Regular User'
    else:
        user_group = None

    return {'user_group': user_group}
