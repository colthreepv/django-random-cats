django-random-cats
==================

Django Random Cats is a dummy app to load a random Django Random Cats is a dummy app to load a random **cat** gif from the interwebz gif from the interwebz

It's ridicolously coded, so don't take inspiration from this, you have been warned.

## How to Use
Having a Django project, install this sub-app with:  
```
$ git clone --depth=1 https://github.com/colthreepv/django-random-cats.git cats && rm -rf !$/.git
```

Include in a Django project by editing your `settings.py`:  

```python
INSTALLED_APPS = [
  'cats.apps.CatsConfig',
  ...
]
```

# Credits
Code and inspiration from [sephiroth6/randomcat](https://github.com/sephiroth6/randomcat)

# What to expect

You were warned

![django-random-cats](https://user-images.githubusercontent.com/2657230/38524937-b6eb375a-3c50-11e8-8da0-c3ad4f8cce0b.gif)
