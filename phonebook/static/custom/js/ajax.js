/**
 * Created by smartankur4u on 26/3/18.
 */

    function contact_save() {
        var name = document.getElementById("name").value;
        var email = document.getElementById("email").value;
        var password = document.getElementById("password").value;

        var csrf = document.getElementById("password").value;

        var form=$("#add-contact-form");

// AJAX code to submit form.
            $.ajax({
                type: "POST",
                url: "/contacts/",
                data: form.serialize(),
                cache: false,

                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                },


                success: function(data){
                        console.log('success');
                        console.log(JSON.stringify(data));
                        },
                failure: function(errMsg) {
                    console.log('failure');
                    console.log(errMsg);
                    }

            });
        return false;
    }

