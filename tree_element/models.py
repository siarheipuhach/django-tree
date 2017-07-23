from django.db import models
from django.template.defaultfilters import slugify


class TreeElement(models.Model):

    name = models.CharField(max_length=30)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    slug = models.SlugField(blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        url = "/%s/" % self.slug
        page = self
        while page.parent:
            url = "/%s%s" % (page.parent.slug, url)
            page = page.parent
        return url

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.url = self.get_absolute_url()
        super(TreeElement, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Tree element'
        verbose_name_plural = 'Tree elements'
