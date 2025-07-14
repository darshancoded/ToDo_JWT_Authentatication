from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    profile_image = serializers.ImageField(required = False,allow_null = True)
    
    class Meta:
        model = User
        fields = ['id', 'email', 'password','profile_image']
        extra_kwargs = {
            'email': {'required': True},
        }
    def validate_profile_image(self, image):
        if image:
            max_size = 3 * 1024 * 1024 #3MB 
            if image.size > max_size:
                raise serializers.ValidationError("Image size should be less then 3MB")
            valid_extensions = ['jpeg','jpg','png']
            extension = image.name.split('.')[-1].lower()
            if extension not in valid_extensions:
                raise serializers.ValidationError("The image format should be in jpeg or jpg or png format")
        return image    
        

    def create(self, validated_data):
        profile_image = validated_data.pop('profile_image',None)
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        if profile_image:
            user.profile_image = profile_image
            user.save()
        return user
    

class LoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField(write_only= True)
    
    def validate(self, data):
        email = data.get('email'),
        password = data.get('password')    
        #authenticate the user
        user = authenticate(email=email, password=password)
        
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        
        refresh = RefreshToken.for_user(user)
        
        return {
            "message":"Login Successfull",
            "refresh": str(refresh),
            "access": str(refresh.access_token),     
        }
