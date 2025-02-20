##########
API aspect
##########

.. jinja:: rsp

   {% if primary %}
   .. include:: api.primary.in.rst

   {% else %}
   Please visit the Rubin Observatory Data Preview 0 (DP0) documentation for an `Introduction to the RSP API Aspect <https://dp0-2.lsst.io/data-access-analysis-tools/api-intro.html>`_.

   {% endif %}
