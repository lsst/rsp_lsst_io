#################################
Getting an account and logging in
#################################

.. jinja:: rsp

   {% if env.is_primary %}
   You need an account to use the |rsp-at|.
   Accounts are available to DP0.2 delegates.
   To learn more about DP0.2 and how to become a delegate and receive a Rubin Science Platform account, visit the `DP0.2 Guide`_.
   {% else %}
   .. important::

      This |rsp-at| is for internal Rubin Observatory engineering and testing.

      If you are a DP0 delegate, switch to the main documentation at {{all_envs.primary.ltd_url_prefix}}.

   To get an account, request one from the RSP environment's administrators or your manager.

   {% endif %}

Logging in
==========

Visit the homepage for the |rsp-at| in your web browser (|rsp-url|).

If you see your username in the top right corner, you're already logged in.
If not, click the :guilabel:`Log in` button in the top right corner.

Next steps
==========

Once you have an account, start exploring with our quick-start tutorials:

- :doc:`portal-first-steps`
- :doc:`notebook-first-steps`
