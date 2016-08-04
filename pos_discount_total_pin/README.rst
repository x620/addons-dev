===========================================
 Restrict set discounts for all POS Orders
===========================================

The module depends on the pos_pin module. Before POS order validation the module checks whether the order with discount. If it does then a cashier get popup with users which belong to the group selected in the "Total Discount Group" field. When you select user then you must type security PIN in the popup.

Credits
=======

Contributors
------------
* Pavel Romanchenko <romanchenko@it-projects.info>

Sponsors
--------
* `IT-Projects LLC <https://it-projects.info>`_

Further information
===================

Demo: http://runbot.it-projects.info/demo/pos-addons/9.0

HTML Description: https://apps.odoo.com/apps/modules/9.0/pos_discount_total_pin/

Usage instructions: `<doc/index.rst>`_

Changelog: `<doc/changelog.rst>`_

Tested on Odoo 9.0 b9bca7909aee5edd05d1cf81d45a540b7856f76e
