odoo.define('pos_discount_total_pin.pos', function (require) {
    "use strict";

    var screens = require('point_of_sale.screens');
    var models = require('point_of_sale.models');
    require('pos_discount_total.OrderWidget');
    var core = require('web.core');
    var _t = core._t;

    screens.OrderWidget.include({
        set_value: function(val){
            var self = this;
            var _super = this._super;
            if (this.summary_selected && this.numpad_state.get('mode') == 'discount'){
                var order = this.pos.get_order();
                self.gui.sudo_custom({
                    'title': _t('Insert security PIN:'),
                    'special_group': this.pos.config.discount_total_group_id[0]
                }).done(function(){
                    _super.call(self, val);
                });
            } else {
                self._super(val);
            }
        }
    });
});
