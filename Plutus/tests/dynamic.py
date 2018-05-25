from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes



print(urlsafe_base64_encode(force_bytes(-1)).decode())