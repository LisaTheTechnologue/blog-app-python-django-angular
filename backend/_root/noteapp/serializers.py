from .models import LNote
from .models import File
from rest_framework import serializers

class LNoteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length = 50)
    desc = serializers.CharField(max_length=1000)
    language = serializers.CharField(max_length=7)
    created_on = serializers.DateField()
    is_draft = serializers.BooleanField(default=False)
    image = serializers.ListField(
                       child=serializers.FileField( max_length=100000,
                                         allow_empty_file=True,
                                         use_url=False )
                                )
    class Meta:
        model = LNote
        fields = ('id','title','desc','language','created_on','is_draft','image')
    # def create(self, validated_data):
        #     return LNote.objects.create(**validated_data)
    def create(self, validated_data):
        blogs=Blogs.objects.latest('created_at')
        image=validated_data.pop('image')
        for img in image:
            photo=Photo.objects.create(image=img,blogs=blogs,**validated_data)
        return photo
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
        
