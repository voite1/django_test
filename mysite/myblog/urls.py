from django.conf.urls import patterns, url

urlpatterns = patterns('myblog.views',

	# URL for the default page
    url(r'^$',
        'list_view',
        name="blog_index"),

    # Named regular epxression - puts argument in kwargs - named capture group
    url(r'^posts/(?P<post_id>\d+)/$',
    	'stub_view',
    	name="blog_detail"),
)