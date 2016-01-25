django-stackoverflow-trace
================

A custom Django technical error template that puts a related stackoverflow search link under the exception message.

### Installation

```bash
$ (sudo) pip install django_stackoverflow_trace
```

### Setting it up

Add the custom middleware to your ```MIDDLEWARE_CLASSES``` in the **settings.py**.


```python
if DEBUG: 
	MIDDLEWARE_CLASSES += ('django_stackoverflow_trace.DjangoStackoverTraceMiddleware', )
```

Next time you hit an error in your app, you will see an external link to a custom google search.

<img src="http://s8.postimg.org/xu0kb8m2t/Screen_Shot_2016_01_23_at_11_10_11.png">

### Using google search instead of stackoverflow

Add this into your settings.py

```DJANGO_STACKOVERFLOW_TRACE_SEARCH_SITE = "googlesearch"```

