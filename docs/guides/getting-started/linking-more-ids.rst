#############################
Linking additional identities
#############################

.. jinja:: rsp

   {% if env.is_primary %}

   Linking additional identities
   =============================

   You can associate additional identities with your account.
   It's a good idea in case your provider is down, or you lose access to your primary account for some reason.
   You can only do this once your account has been approved with the first identity you chose.

   Step-by-step
   ============

   1. Go to id.lsst.cloud and log on with your first identity.

   2. Once you are logged in:

      .. grid:: 1 2 2 2

         .. grid-item::

            - From the top right menu (with your name) click down to see more options
            - Click on "Link another account"
            - Chose another institution/provider with whom you have an established account.
            - Follow the prompts to complete the login process with that provider

         .. grid-item::

            .. image:: images/acc_more_ids.png

   3. You can use any of your linked identities to log on from now on.


   {% else %}
   .. important::

      This |rsp-at| is for internal Rubin Observatory engineering and testing.

      If you are a science community member, switch to the main documentation at {{all_envs.primary.ltd_url_prefix}}.

   {% endif %}
