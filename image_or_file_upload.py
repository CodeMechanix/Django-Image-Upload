# Step-01: settings.py

#media files uploaded by user
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Step-02: urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Step-03: views.py

if request.FILES['upload_image']:
    upload_image = request.FILES['upload_image']
    fs = FileSystemStorage()
    image_name = fs.save(upload_image.name, company_image)
    # uploaded_file_url = fs.url(image_name)
    user.image = image_name # save into DB
else:
    pass


# Step-04: home.html
<td>
    <img style="border-radius: 50%;" id="blah"
         src="{{ data.image.url }}" alt="Company Image"
         height="80px" width="80px"/>
</td>

<form id="cityArea" action="{% url '' %}" method="POST" enctype="multipart/form-data">
<div class="row">
    <div class="col-sm-6">
        <div class="form-group">
            <label for="image" class="control-label">Image</label>
            <input type="file" name="upload_image" class="form-control" id="imgInp"
                   accept=".jpeg,.png,.jpg,.gif,.svg">
            <img style="border-radius: 50%;" id="blah" src="" alt="Upload Image"
                 height="80px" width="80px"/>
        </div>
    </div>
</div>
</form>

<script>
    document.getElementById("imgInp").onclick = function () {
        document.getElementById("blah").style.visibility = "visible";
    };
    function readURL(input) {
        if (input.files && input.files[0]) { var reader = new FileReader();
            reader.onload = function (e) { $('#blah').attr('src', e.target.result); }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imgInp").change(function(){ readURL(this); });
</script>