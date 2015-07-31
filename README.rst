Django_assets angular template filter.
========================================================

What's that?
-------------
Is a filter for generating html templates as javascript includes in your bundles of django_assets

How to use
----------
Add the application to your INSTALLED_APPS

.. code-block:: python
                
   INSTALLED_APPS = (
     ...
     'assets_angular',
     'django_assets',
     ...
   )
                



Using it
---------------

.. code-block:: python
                
   from django_assets import Bundle, register                

   templates = Bundle(
     'tpl/template1.html',
     'tpl/template1.html',   
     filters='angular',
     output="templates.js"
   )

   app_js = Bundle(
    models,
    controllers,
    directives,
    filters,
    services,
    templates,
    filters='uglifyjs',
    output='gen/app.js')

    register('app', app_js)
