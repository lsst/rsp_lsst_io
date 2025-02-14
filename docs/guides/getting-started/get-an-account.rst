#############################
Getting an account on the RSP
#############################

.. jinja:: rsp

   {% if env.is_primary %}
   .. include:: user-step-by-step.primary.in.rst


   {% else %}
   .. important::

      This |rsp-at| is for internal Rubin Observatory engineering and testing.

      If you are a science community member, switch to the main documentation at {{all_envs.primary.ltd_url_prefix}}.

   To get an account, request one from the RSP environment's administrators or your manager.
   {% endif %}
