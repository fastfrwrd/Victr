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

    var $inputs = $('.tagger');

    $inputs.keyup(function(e) {
        if (e.which != 13) return;
        var $me = $(this);
        var val = $me.val();
        $me.siblings('.tag_list').append('<li><i class="icon-tag"></i>'+val+'</li>');
        $me.val('');
    });
}