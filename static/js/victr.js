if (typeof(Victr) == 'undefined'){var Victr = {};Victr.widgets = {};Victr.utils = {};}

Victr.init = function() {
    var self = this;

    // grab the current page
    self.page_id = $('.main').attr('id');
    self.$page = $('#'+this.page_id);
    self.$nav = $('nav');

    // kick off this page's js
    if (self.hasOwnProperty(self.page_id)) {
        self[self.page_id]();
    }
    
    if(self.page_id.indexOf('impress') === -1) {
        self.widgets.auth('#auth', '#register', self.url.register_modal);
    }
   
}

Victr.project_new = function() {
    var self = this,
        $form = self.$page.find('form');
    self.widgets.form($form);
    self.widgets.tagger(self.$page);
    self.widgets.autocomplete(self.$page);
    $("select:not(.tagger)").chosen({no_results_text: "No results matched"});
    $("select.tagger").chosen({allow_option_creation: true});
}
Victr.project_edit = Victr.project_new;

Victr.impress_present = function() {
    $('a').click(function(e) {
        window.open($(this).attr('href'), '_blank');
        return false;
    });
}
    
Victr.archive = function() {
    var self = this;
    self.widgets.expand(self.$page, '.event .info', '.projects');
    self.widgets.goTo(self.$page, self.$nav, 'now', $('.navbar').height());
}

/* WiDgEtS oMg! */
    
Victr.widgets.goTo = function($page, $nav, label, padding) {
    var $w = $(window), $body = $('body'), $el, offset, duration;
    
    var getItem = function() {
        $el = $($page.find('[data-label]="'+label+'"').get(0));
    },
    getOffset = function() {
        offset = Math.floor($el.offset().top) - padding
        duration = offset/2;
    },
    scrollTo = function(e) {
        $body.animate({
            scrollTop: offset
        }, duration, function() {
            window.location.hash = label;
        });
        if (e)
            e.preventDefault();
    },
    attachToLink = function() {
        $nav.find('a[data-goto]').each(function() {
            var $this = $(this),
                data = $this.data('goto');
            if (data === label) {
                $this.on('click', scrollTo);
            }
        })
    };
    
    $(function() {
        getItem();
        getOffset();
        attachToLink();
        $w.on('resize', getOffset);
        $('a.btn-navbar').on('click',function() {
            setTimeout(function() {
                getOffset();
            }, 300);
        });
        setTimeout(function() {
            scrollTo()
        }, 100);
    })
}

Victr.widgets.form = function($form) {
    var self = this;
    $form.on('keypress', ':input:not(type=submit)', function(e) {
        if (e.which != 13) return;
        if (e.currentTarget.nodeName == 'TEXTAREA') {
            var $ta = $(this);
            $ta.val($ta.val()+"\n");
        }
        e.preventDefault();
    });
    $form.submit(function(){
        $('#submit').prop('disabled', true);
    })
}

Victr.widgets.tagger = function($page) {
    var self = this;

    var $fields = $page.find("[data-role='tagger']");

    $fields.each(function() {
        var $field = $(this),
            _id =  $field.find('input').attr('id'),
            $ul = $field.find('#'+_id+'_list');
        if (!$ul.length) {
            $field.append('<ul id="'+_id+'_list"></ul>')
        }
        $field.addClass('tagger');
    });
    
    $fields
    .on('keyup', 'input', function(e) {
        if (e.which != 13) return;
        var _icon = $(e.delegateTarget).data('icon'),
            $input = $(this),
            _id = $input.attr('id'),
            _val = Victr.utils.escape($.trim($input.val()));
        if (_val.length == 0) return;
        var li = '<li class="label label-info"><i class="icon-remove icon-white"></i><i class="icon-white icon-'+_icon+'"></i>'+_val+'<input type="hidden" name="'+_id+'[]" value="'+_val+'" /></li>';
        $input.siblings('ul').append(li);
        $input.val('');
        return false;
    });

    $fields.on('click', "li", function(e) { var
        $li = $(this),
        _val = $li.text(),
        _id = $li.parent().siblings("input").attr('id');
        $li.remove();
    });

}

//handles customizations of dropdown and modal from Bootstrap.
Victr.widgets.auth = function(id, modal, modal_url) {
    var self = this,
        $auth = $(id),
        $wrapper = $auth.find('.login-wrapper'),
        $modals = $('#modals');
    
    $auth.find('a.dropdown-toggle').on('click', function(e) {
        e.preventDefault();
    	var current_path = encodeURIComponent(window.location.pathname.slice(Victr.url.login.length)),
    	    login_url = Victr.url.login_nav + '?next=' + current_path;
        
        if($wrapper.hasClass('loading')) {
            $wrapper.load(login_url + ' form', function() {
                $wrapper.removeClass('loading');
                $modals.load( modal_url );
                $(this).find('a.register').attr({
                    'data-toggle': 'modal',
                    'data-target': '#register'
                }).on('click', function(e) {
                    e.preventDefault();
                });
            });
        }
    });
    
    $modals
    .on('click', modal+' .modal-footer *:submit', function(e) {
        $(this).closest('form').submit();
    })
    .on('keyup', modal+' :input', function(e) {
        if (e.which != 13) return;
        $(this).closest('form').submit();
    });
}

Victr.widgets.autocomplete = function($page) {
    var self = this,
        cache = {};
    
    var $fields = $page.find("[data-type]");
    $fields.each(function() {
        $field = $(this);
        var $input = $field.find('input'),
            type = $field.data('type');
        cache[type] = {};
        $input.typeahead({
            source: function(typeahead, query) {
                if (!query) return;
                var data = cache[type][query];
                if (data) return data;
                return $.ajax({
                    url: '/api/'+type+'/search/'+query,
                    success: function(data) {
                        cache[type][query] = data;
                        return typeahead.process(data);
                    },
                    dataType: 'json'
                })
            },
            property: 'name',
            onselect: function() {
                var e = $.Event('keyup');
                e.which = 13;
                e.delegateTarget = e.target = $input.get(0);
                $fields.trigger(e);
            }
        })
    })
}
    
    
Victr.widgets.expand = function($page, click, area) {
    $page.on('click', click, function() {
        var $parent = $(this).parent().toggleClass('closed');
        $parent.find(area).slideToggle();
    });
}


Victr.utils.escape = function(str) {
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');
}