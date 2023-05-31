from PIL import Image
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO


def cropImage(request):
    img = request.data.get('avatar', "0");
    left = request.data.get('left', "0");
    top = request.data.get('top', "0");
    right = request.data.get('right', "100");
    bottom = request.data.get('bottom', "100")
    area = [int(left), int(top), int(right), int(bottom)];
    pillowImg = Image.open(img)
    cropped_img = pillowImg.crop(area);
    buffer = BytesIO()
    cropped_img.save(fp=buffer, format=pillowImg.format);
    file = ContentFile(buffer.getvalue())
    result = InMemoryUploadedFile(
        file,
        None,
        img.name,
        img.content_type,
        cropped_img.tell,
        None
    )
    return result;