####################
Log of major updates
####################

.. jinja:: rsp

   {% if env.is_primary %}
   .. include:: log.primary.in.rst

   {% else %}
   The RSP is under continuous development.

   {% endif %}
