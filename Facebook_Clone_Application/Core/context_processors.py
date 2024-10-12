# Core/context_processors.py
from .models import UserProfile
from django.shortcuts import get_object_or_404

def user_profile(request):
    profile = None
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            profile = None
    return {'user_profile': profile}
