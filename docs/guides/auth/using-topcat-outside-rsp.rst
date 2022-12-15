#################################################################
Tutorial: Authenticating from TOPCat outside the Science Platform
#################################################################

This tutorial shows you how to access the Rubin Science Platform datasets from outside the Science Platform with :doc:`user tokens <creating-user-tokens>`.
This example specifically shows how to access table data from the Science Platform's TAP service with TOPCAT_, a popular viewer and editor for tabular and catalog data.

#. Follow the steps in :doc:`creating-user-tokens` to create a new user token.
   Ensure that the token has ``read:tap`` scope.

   .. image:: images/create-token-dialog.png
      :alt: Create token dialog

   Be sure to copy the token string shown after you click :guilabel:`Create`.
   The Science Platform won't show you the token string again after you dismiss the dialog.

#. On your local machine open up `TOPCAT`_.
   This will require having `Java`_ installed.

#. From TOPCAT, select :menuselection:`VO --> Table Access Protocol (TAP) Query`.

  .. image:: images/topcat-vo-menu.png
     :alt: The VO menue

#. This will bring up a window with a list of available TAP services.
   We want to use a service with a known endpoint.
   Enter |rsp-tap-url-code| in the box at the bottom of the page labeled :guilabel:`TAP URL`.

   .. image:: images/topcat-tap-window.png
      :alt: The TAP service configuration window.

#. Clicking :guilabel:`Use Service` will bring up a username/password dialog.
   Set the :guilabel:`User` to ``x-oauth-basic``.
   Paste the entire access token into the :guilabel:`Password` field.

   .. image:: images/topcat-username-password.png
      :alt: Username and password dialog.

#. If authentication is successful, the window will change to the TAP service window and information about the various tables in the service will appear in the left portion of the upper panes.
   If you select a table, you will see information about the columns in the table to the right of the table listing.

   This example uses the ``wise_00.allwise_p3as_mep`` table.
   Make a query by entering the ADQL in the box at the bottom and click the :guilabel:`Run Query` button.

   The example query selects three magnitudes from a circular region on the sky.

   .. code-block:: SQL

      SELECT w1mpro_ep, w2mpro_ep, w3mpro_ep FROM wise_00.allwise_p3as_mep WHERE CONTAINS(POINT('ICRS', ra, decl), CIRCLE('ICRS', 192.85, 27.13, .2)) = 1

   .. image:: images/topcat-query-window.png
      :alt: Query window

#. Once the query returns, you can make plots like this color-color diagram.
   Create two `synthetic columns`_ from the magnitude to create colors for the plot.

   .. image:: images/topcat-color-color.png
      :alt: A color color plot from wise data.

.. _`TOPCAT`: http://www.star.bris.ac.uk/~mbt/topcat/
.. _`Java`: https://www.java.com/en/
.. _`synthetic columns`: http://www.star.bris.ac.uk/~mbt/topcat/sun253/sun253.html#SyntheticColumnQueryWindow
