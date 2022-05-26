from django.urls import path

from users.views import profiles, userAccount, userProfile, loginUser, logoutUser, registerUser, editAccount, createSkill, updateSkill, deleteSkill, inbox, viewMessage, createMessage

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser, name='register'),
    path('register/', registerUser, name='register'),




    path('', profiles, name='profiles'),
    path('profile/<str:pk>/', userProfile, name='user-profile'),
    path('account/', userAccount, name='user-account'),
    path('edit-account/', editAccount, name='edit-account'),
    path('createSkill/', createSkill, name='create-skill'),
    path('updateSkill/<str:pk>/', updateSkill, name='update-skill'),
    # path('updateSkill/<str:pk>/', updateSkill, name='update-skill'),
    path('deleteSkill/<str:pk>/', deleteSkill, name='delete-skill'),
    path('inbox/', inbox, name='inbox'),
    path('message/<str:pk>/', viewMessage, name='message'),
    path('create-message/<str:pk>/', createMessage, name='create-message'),
]
