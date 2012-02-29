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
        Victr.widgets.scroller(self.$nav,self.$page);
        Victr.widgets.auth('#auth', '#register', Victr.url.register_modal);
    }
   
}

Victr.project_new = function() {
    var self = this,
        $form = self.$page.find('form');
    self.widgets.form($form);
    self.widgets.tagger(self.$page);
    self.widgets.autocomplete(self.$page);
    $("select").chosen({no_results_text: "No results matched"});
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
}

/* WiDgEtS oMg! */

Victr.widgets.scroller = function($nav,$page) {
    var data, $w = $(window);
    
    var snip = function(url) {
        return url.split('#')[1];
    },
    getItems = function(){
        var items = {},
            links = $nav.find('.nav a[href*="#"]');
        links.each(function() {
            
            var hash = snip($(this).attr('href'));
            if (hash)
                items[hash] = {};
        });
        return items
    },
    getElements = function() {
        for( var id in data ) {
            data[id].$ = $page.find('#'+id);
        }
    },
    getOffsets = function() {
        for( var id in data ) {
            var item = data[id];
            if (!item.$.length) continue;
            item.off = Math.floor(item.$.offset().top);
        }
    },
    scrollTo = function(id) {
        if (!id) return;
        var offset = data[id].off,
            duration = Math.abs($w.scrollTop() - offset);
        $('body').animate({
            scrollTop: offset
        }, duration, function() {
            window.location.hash = id;
        });
    },
    setListeners = function() {
        $nav.on('click','a[href*="#"]', function(e) {
            var hash = snip($(this).attr('href'));
            if (!hash) return;
            e.preventDefault();
            scrollTo(hash);
        })
    };
    
    $(function(){
        data = getItems();
        getElements();
        getOffsets();
        setListeners();
        $w.on('resize', function() {
            getOffsets();
        });
        $('a.btn-navbar').on('click',function() {
            setTimeout(function() {
                getOffsets();
            },300);
        });
        setTimeout(function() {
            scrollTo(snip(window.location.href));
        }, 100);
    });

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