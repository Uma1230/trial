from django.contrib import admin
from blog.models import Post

from django.db import models
from tinymce.widgets import TinyMCE
class PostAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
}
admin.site.register(Post, PostAdmin)