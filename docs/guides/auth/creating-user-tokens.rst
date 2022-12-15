####################
Creating user tokens
####################

If you want to use a Science Platform API service from a local system, you can create a new user token.

.. At creation time, you can:

.. - give the token a name,
.. - restrict the token's access to only the services you need, and
.. - configure the expiration, including setting it to not expire.

Follow these steps to create a user token.

#. Open the |rsp-at| in a web browser.

#. Select :guilabel:`Security tokens` from the user drop-down menu at the upper right.

   .. image:: images/security-tokens-menu.png
      :alt: Drop-down user menu

#. Click on :guilabel:`Create Token` under User Tokens.

   .. image:: images/create-token-button.png
      :alt: Create token button

#. Choose a token name, scopes, and expiration.
   Usually you will want to name the token after the application you will use it with.

   Which scopes to select depends on what you're doing.
   For example, to query the TAP service the scope you want is ``read:tap``.

   If you know that you'll only be using the token for a limited period of time, you can choose an expiration date.
   Otherwise, you can set the token to never expire.

   .. image:: images/create-token-dialog.png
      :alt: Create token dialog

#. Click on :guilabel:`Create`.
   You will be shown the token, but only once.
   Be sure to copy this token and save it somewhere secure on your local system.

   .. image:: images/create-token-result.png
      :alt: Create token result

.. jinja:: rsp

   {% if env.api_tap_url %}
   Next steps
   ==========

   - Follow :doc:`a tutorial for authenticating TOPCAT to the TAP (table) service <using-topcat-outside-rsp>` from your local computer.
   {% endif %}
