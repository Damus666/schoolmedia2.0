from .models import Profile, Relationship

def profile_pic(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        pic = profile_obj.avatar
        return {'picture':pic}

    return {}

def invatations_received_no(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        count = Relationship.objects.invatations_received(profile_obj).count()
        return {'count':count}
    return {}