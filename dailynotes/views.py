from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import DailyNote
from .serializers import DailyNoteSerializer

# ViewSet untuk API dailynote
class DailyNoteViewSet(ModelViewSet):
    queryset = DailyNote.objects.all().order_by('-created_at')
    serializer_class = DailyNoteSerializer

# Fungsi untuk menangani tampilan halaman depan (home)

def home(request):
    return render(request, 'dailynotes/index.html')  # pastikan path sesuai dengan lokasi template
