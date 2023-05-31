import base64
from django.conf import settings

def b64_image(filepath):
    try:
        with open(f'{settings.BASE_DIR}{filepath}', 'rb') as f:
            b64 = base64.b64encode(f.read())
            data = {
                "success": True,
                "base64": b64.decode('utf-8'),
                'extension': f.name.split('.')[-1][0],
            }
            f.close();
            return data;
    except:
        return {
            "success": False
        }
