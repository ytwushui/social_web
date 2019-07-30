from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        # field is needed to specify what field we want
        # just need to name it (if this is exist in the model)
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # late the laber of the key words
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
