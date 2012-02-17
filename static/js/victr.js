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

    console.log('project_new', this, arguments);
}