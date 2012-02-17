if (typeof(Victr) == 'undefined'){var Victr = {}}


Victr.init = function() {
    var self = this;

    // grab the current page
    self.page_id = $('.container').attr('id');
    self.$page = $('#'+this.page_id);

    // kick off this page's js
    self[self.page_id]();

}

Victr.project_new = function() {
    var self = this;
    self.widgets.tagger(self.$page);
    $('#submit').click(function(){

        $(this).prop('disabled', true)

        var data = {};
        self.$page.find('[name]').each(function() {
            var $input = $(this);
            data[$input.attr('name')] = $input.val();
        })
        $.extend(data, self.widgets.tagger_data);

        $.post( 'new', data, function( result ) {
            window.location.pathname = result.location;
        }, 'json');
    })
}

Victr.impress_present = function() {
    $('a').click(function(e) {
        window.open($(this).attr('href'), '_blank');
        return false;
    });
}


Victr.widgets = {};

Victr.widgets.tagger = function($page) {
    var self = this;
    self.tagger_data = {};

    var $fields = $page.find("[data-role='tagger']");

    $fields.each(function() {
        var $field = $(this),
            _id =  $field.find('input').attr('id');
        $field.addClass('tagger').append('<ul id="'+_id+'_list"></ul>')
        self.tagger_data[_id] = [];
    });

    $fields.on('keyup', 'input', function(e) {
        if (e.which != 13) return;
        var _icon = $(e.delegateTarget).data('icon'),
            $input = $(this),
            _val = $.trim($input.val());
        if (_val.length == 0) return;
        $input.siblings('ul').append('<li><i class="icon-remove"></i><i class="icon-'+_icon+'"></i>'+_val+'</li>');
        self.tagger_data[$input.attr('id')].push(_val);
        $input.val('');
    })

}