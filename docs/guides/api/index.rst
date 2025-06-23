##########
API aspect
##########

.. jinja:: rsp

   {% if env.is_primary %}
   .. include:: api.primary.in.rst
   {% else %}
   .. include:: api.primary.in.rst
   {% endif %}

   {% if env.api_webdav_url %}
   .. include:: api.webdav.in.rst
   {% endif %}
