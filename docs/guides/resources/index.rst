#########
Resources
#########

Learn about the storage space and computational resources included with your account.

.. jinja:: rsp

   {% if env.is_primary %}

   .. include:: user-account-resources.primary.in.rst


   {% else %}
   .. important::

      This |rsp-at| is for internal Rubin Observatory engineering and testing.

      If you are a science community member, switch to the main documentation at {{all_envs.primary.ltd_url_prefix}}.

   {% endif %}