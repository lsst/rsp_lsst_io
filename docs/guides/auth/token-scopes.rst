.. These scopes and descriptions are based on Gafaelfawr's Phalanx configuration:
.. https://github.com/lsst-sqre/phalanx/blob/master/services/gafaelfawr/values.yaml
.. admin: scopes are excluded.

############
Token scopes
############

Tokens enable you to access data and perform specific actions on the Rubin Science Platform.
Each token is associated with *scopes* that provide specific capabilities when you use that token.
This page describes those scopes.
To learn how to create a token, see :doc:`creating-user-tokens`.

``exec:notebook``
    Use the :doc:`Notebook Aspect <../notebooks/index>`.

``exec:portal``
    Use the :doc:`Portal Aspect <../portal/index>`.

``read:alertdb``
    Retrieve alert packets and schemas from the Alert archive database.

``read:image``
    Retrieve images from project datasets.

``read:tap``
    Execute SELECT queries in the TAP interface on project datasets.

``write:files``
    Write files in the user's directories (eg via WebDAV)

``user:token``
    Create and modify user tokens.
