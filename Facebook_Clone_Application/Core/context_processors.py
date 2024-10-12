from .models import UserProfile
from django.shortcuts import get_object_or_404

# The method will take the profile info of current user
def user_profile(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        return {
            'profile': profile
        }
    return {}