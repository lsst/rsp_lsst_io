WebDAV
======

.. note::

    The WebDAV service is in beta. Details of how or whether this capability is offered may change.

RSP users have the option of starting a WebDAV server within the RSP.
This allows you to connect to your RSP home space from your latop.
With this capability, you can use your favorite editor locally to edit files on your RSP home, or move files easily between your RSP home and your laptop.

Start your WebDAV server
------------------------

One-time setup:
^^^^^^^^^^^^^^^

1. Create a token with ``exec notebook`` scope. See :doc:`../auth/creating-user-tokens` on how to do this. Copy the generated token

2. (optionally) save your token in a password manager

When you need your server:
^^^^^^^^^^^^^^^^^^^^^^^^^^


3. Navigate to |webdav-app| and wait for the page to load (the delay is the time it takes to start your personal WebDAV server if it's not running already).

4. You can now connect to your WebDAV server with the tool of your choice. While there are dedicated clients, most operating systems support WebDAV in their file browsing built-in tools:

* Mac users can use Finder
* Linux users can use a file manager such as Nautilus or Dolphin
* Windows users can use File Explorer

Use |webdav-server| as the server address, and the token you generated in the first step as the password.

To conserve resources for all users, your WebDAV server is shut down after a period of inactivity. To start it again, simply repeat step 3.
