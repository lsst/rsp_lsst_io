##########################
Recover from access issues
##########################

.. jinja:: rsp

   {% if env.is_primary %}
   .. include:: user-recovery.primary.in.rst


   {% else %}
   .. important::

      This |rsp-at| is for internal Rubin Observatory engineering and testing.

      If you are a science community member, switch to the main documentation at {{all_envs.primary.ltd_url_prefix}}.

   To recover a staff account, contact one of the RSP environment's administrators or your manager.
   {% endif %}
