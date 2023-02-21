#############################
Getting an account on the RSP
#############################

.. jinja:: rsp

   {% if env.is_primary %}

   Signing up for an RSP account on data.lsst.cloud
   ================================================

   Things to know before you get started:
   --------------------------------------

   -  You can sign up for an account, however, your account will have to be approved by Rubin Observatory before becoming active and is subject to confirmation that you fulfill the criteria for being granted access.
      *At this time, this means having been invited to the pre-operations Data Preview program.*
      Visit the `DP0.2 Guide`_ for more information.

   -  For |rsp-at|, the RSP uses the CILogon service (operated by NCSA) in order to allow you to gain RSP access with your institutional identity (via the InCommon federation) or certain other participating providers (such as Github or Orcid).
      Simply put, our system asks your institution’s system if you are who you say you are.
      You *must* have an account with one of the supported institutions or organizations to use the RSP and if you have account issues such as needing to reset your password, you should follow up with your institution as you would normally.
      Rubin staff *do not have access to your password or any other data from your institutional account besides your name.*
   -  Our `Acceptable Use Policy <https://data.lsst.cloud/terms>`__ is in plain language - you should review it; your access is contingent on abiding by it.

   .. vimeo:: 800911530

   Getting started
   ---------------

   1. RSP landing page:

      -  Go to the RSP at |rsp-url| in your browser
      -  Click **Log In** at the upper right

   2. Identity provider choice page:

      -  Chose an institution/provider with whom you have an established identity
      -  You will be able to link additional identities later (if you have more than one)
      -  Remember who you pick!

   3. Institution login page(s)

      -  You are forwarded to your selected institution
      -  Log on as you normally would
      -  If your institution has additional authentication steps (eg. 2FA) you will have to complete those too

   4. RSP login page:

      -  Chose whichever institution you picked above (should be set already - this is not the time to change your mind!).
         This looks deceptively like Step 2.

   5. Self signup pages:

      -  You can now start the self-signup
      -  You are asked for given and family name. *We do not require your legal name*; the reason you are being asked is to allow us to establish you are entitled to our data products.
         You should supply whichever name you use for publications or are known to your colleagues as; for example, if you go by your middle name, supply your middle name as the given name; if you publish as Lady Gaga signing up as \****Stefani Joanne Angelina Germanotta would be just confusing to everybody.
      -  You can provide any email you want provided you can immediately access it (for the confirmation).
         Additionally, using your institutional email address (instead of say, a gmail account) helps our verification process; please do so if you can.

   6. Email confirmation step:

      -  You will receive an email to the address you provided. Please look out for it and click on the link inside it to complete the process.

   7. Finishing steps:

      -  Clicking on the link in your email will take you to a page where you can accept your invitation

      -  Your final job is to select a username; this has to be a valid unix username
      -  This completes the account petition process; you will receive an email at the address you provided when your account access has been approved by the project.




   {% else %}
   .. important::

      This |rsp-at| is for internal Rubin Observatory engineering and testing.

      If you are a DP0 delegate, switch to the main documentation at {{all_envs.primary.ltd_url_prefix}}.

   To get an account, request one from the RSP environment's administrators or your manager.

   {% endif %}

