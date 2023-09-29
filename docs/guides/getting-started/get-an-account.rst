#############################
Getting an account on the RSP
#############################

.. jinja:: rsp

   {% if env.is_primary %}

   Things to know before you get started
   =====================================

   - Rubin data rights are required in order to hold an account in the Rubin Science Platform.
     All scientists and students affiliated with an institution in the US and Chile have data rights, as well as the international scientists and students whose names appear on the `list of international data rights holders <https://lsst.org/scientists/international-drh-list>`__.
     For more information about data rights, please refer to the `Rubin Observatory Data Policy <https://docushare.lsst.org/docushare/dsweb/Get/RDO-013>`__.
     If you’re not sure if you have Rubin data rights, please contact Heather Shaughnessy at `sheather@slac.stanford.edu <mailto:sheather@slac.stanford.edu>`__.

   - The |rsp-at| (|rsp-url|) uses the CILogon service (operated by NCSA) in order to allow you to gain RSP access with your institutional identity (via the InCommon federation) or certain other participating providers (such as GitHub or ORCiD).
     Simply put, our system asks your institution’s system if you are who you say you are.

     You *must* have an account with one of the supported institutions or organizations to use the RSP
     If you have account issues (such as needing to reset your password) you should follow up with your institution as normal.
     *Rubin staff do not have access to your password or any other data from your institutional account besides your name.*

   - Our `Acceptable Use Policy <https://data.lsst.cloud/terms>`__ is in plain language — you should review it; your access is contingent on abiding by it.

   Video
   =====

   This video shows the steps for creating a new account on |rsp-url|:

   .. vimeo:: 800911530

   Step-by-step
   ============

   1. RSP homepage:

      .. grid:: 1 2 2 2

         .. grid-item::

            - Go to the RSP at |rsp-url| in your browser.
            - Click :guilabel:`Log In` at the upper right.

         .. grid-item::

            .. image:: images/acc_login.png

   2. RSP (via CILogon) login page:

      .. grid:: 1 2 2 2

         .. grid-item::

            - Chose an institution/provider with whom you have an established account.
            - You will be able to link additional identities later (if you have more than one).

         .. grid-item::

            .. image:: images/acc_institution.png

   3. Institution login page(s):

      - You are forwarded to your selected institution.
      - Log on as you normally would.
      - If your institution has additional authentication steps (such as 2FA) you will have to complete those too.
      - At this point the RSP will detect that you do not already have an established account and start the onboarding flow.

   4. Onboarding flow: Identity provider selection

      .. grid:: 1 2 2 2

         .. grid-item::

            - Chose whichever institution you picked above (should be selected on the menu already - this is not the time to change your mind!).
              This looks deceptively like Step 2.

         .. grid-item::

            .. image:: images/acc_institution.png

   5. Onboarding flow: Self signup pages

      - You can now start the self signup.
      - Provide your given and family name.
        *We do not require your legal name*; the reason you are being asked is to allow us to establish you are entitled to our data products.
        You should supply whichever name you use for publications or are known to your colleagues as.

        *Examples.* If you go by your middle name, supply your middle name as the given name.
        If you publish as *Lady Gaga*, don't sign up as *Stefani Joanne Angelina Germanotta*.

      - Provide any email you want provided you can immediately access it (for the confirmation).
        Additionally, using your main institutional email address (instead of say, a Gmail account) helps our verification process; please do so if you can.

   6. Onboarding flow: Email confirmation step

      -  You will receive an email to the address you provided, from registry@cilogon.org.
         Please look out for it in your spam folder, the subject will be "Please verify your LSST Registration".
         Click on the link inside it to complete the process.

   7. Onboarding flow — Finishing steps:

      -  Clicking on the link in your email will take you to a page where you can accept your invitation.
      -  Your final job is to select a username; this has to be a valid Unix username.
      -  This completes the account petition process; you will receive an email at the address you provided when your account access has been approved by the project.
      -  The approval process includes verification of Rubin data rights and is done by a person (not automatic), so may take several days. Thank you for your patience.

   {% else %}
   .. important::

      This |rsp-at| is for internal Rubin Observatory engineering and testing.

      If you are a DP0 delegate, switch to the main documentation at {{all_envs.primary.ltd_url_prefix}}.

   To get an account, request one from the RSP environment's administrators or your manager.
   {% endif %}
