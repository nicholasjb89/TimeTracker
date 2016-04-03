/**
 * Created by Bailey on 4/2/2016.
 */

window.addEvent('domready',function() {

    //You may will need to change category, id_subject, and id_selected_cat
    //to match the names of the fields that you are working with.
    var category = $('category');
    var subject = $('id_subject');

    var update_subcat = function() {
        var cat_id = $('id_selected_cat').value;
        if (cat_id) {
            $('id_selected_cat').value='';
            category.value=cat_id;
        } else {
            cat_id = category.getSelected()[0].value;
        }
        //cat_id = category.getSelected()[0].value;
        var subcat_id = subject.getSelected()[0].value;
        var request = new Request.JSON({
            url: "/product/subject/"+cat_id+"/",
            onComplete: function(subcats){
                subject.empty();
                if (subcats) {
                    subcats.each(function(subcat) {
                        var o = new Element('option', {
                            'value':subcat.pk,
                            'html':subcat.fields.name
                        });
                        if (subcat.pk == subcat_id) {
                            o.set('selected','selected');
                        }
                        o.inject(subject);
                    });
                } else {
                    var o = new Element('option', {
                        'value':'',
                        'html':'Please Choose A Category First'
                    });
                    o.inject(subject);
                }
            }
        }).get();
    };
    update_subcat();

    category.addEvent('change', function(e){
        e.stop();
        update_subcat();
    });

});