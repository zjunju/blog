$(function () {
    // $menu_span  页面缩小时，头部导航栏出现的菜单。

    // var $all_input = $(':input');
    // $all_input.val('');

    var $menu_span = $('#menu-span');

    $menu_span.click(function () {
        var $menu_ul = $('header .nav .menu');
        $menu_ul.fadeToggle(200);
        $(this).toggleClass('icon-close');

    });

    // end**********************

    var $search_span = $('#search');
    var $search_form = $('.search-box form');
    var $input_wd = $search_form.find('input');
    var $i = $search_span.find('i');

    $search_span.click(function () {
        if ($search_form.css('display') == 'block') {
            $search_form.fadeOut(200);
        }else{
            $search_form.fadeIn(200, function () {
                $i.toggleClass('change-search-color');
                $input_wd.trigger('focus');
            });
        }
    });

    $input_wd.blur(function () {
        if ($search_form.css('display')=='block') {
            $search_form.fadeOut(200);
        }
        $i.removeClass('change-search-color');
    });


    var $go_signup = $('.go-signup');
    var $go_signin = $('.go-signin');
    var $sign_close_btn = $('#sign-close-btn');
    var $change = $('.change');
    var $signin_error_field = $('#signin-error-field');
    var $signup_error_field = $('#signup-error-field');

    /* 显示隐藏mask */
    var $sign_box = $('.sign-box');

    function show_signin(){
            $sign_box.css('marginLeft', 0);
    };

    function show_signup(){
        $sign_box.css('marginLeft', -400);
    };

    function mask_show(){
        $mask.show();
        $('body').css('overflow', 'hidden');
    }


    var $mask = $('.mask');
    // 显示注册界面
    $go_signup.click(function () {
        mask_show();
        show_signup();

    });

    // 显示登录界面
    $go_signin.click(function () {
        mask_show();
        show_signin();
    });

    // 关闭登录注册界面
    $sign_close_btn.click(function () {
        $mask.hide();
        var reset = $mask.find('input[type=reset]');
        reset.trigger('click');
        $signin_error_field.text('');
        $signup_error_field.text('');
        $('body').css('overflow', 'scroll');
    });

    /*  切换登录注册 */
    $change.click(function () {
        if ($sign_box.css('marginLeft') == '-400px'){
            show_signin();
        }else{
            show_signup();
        }
    });


    var $signin_submit =  $('#signin-submit');
    $signin_submit.click(function () {
        $signin_error_field.text('');
        var current_href = window.location.href;
        var $signin = $(this).parents('.signin');
        var username = $signin.find("input[name=username]").val();
        var password = $signin.find("input[name=password]").val().replace(/(^\s*)|(\s*$)/g, '');
        var remember = $signin.find("input[name=remember]").prop('checked');
        var token = $signin.find("input[name=csrfmiddlewaretoken]").val();
        if (username == '' || username==undefined || username==null){
            alert('用户名不能为空');
            return false;
        };

        if (password == '' || password==undefined || password==null){
                alert('密码不能为空');
                return false;
        };
        $.ajax({
            url: '/auth/signin/',
            type: 'post',
            data: {'username': username, 'password': password, 'remember': remember, 'csrfmiddlewaretoken': token},
            success: function (data) {
                if(data.code == '200'){
                    alert('登陆成功');
                    window.location.replace(current_href);
                }else{
                    var message = data.message;
                    $signin_error_field.append('<p>'+ message +'</p>');
                }
            },
            error: function (xhr) {
                console.log(xhr);
            },
        });
        return false;
    });

    
    var $signup_submit = $('#signup-submit');
    $signup_submit.click(function () {
        $signup_error_field.text('');
        var current_href = window.location.href;

        var $signup = $(this).parents('.signup');
        var username = $signup.find("input[name=username]").val();
        var telephone = $signup.find("input[name=telephone]").val();
        var password = $signup.find("input[name=password]").val();
        var password_reply = $signup.find("input[name=password_reply]").val();
        var token = $signup.find("input[name=csrfmiddlewaretoken]").val();

        if (telephone == '' || telephone==undefined || telephone==null){
                alert('手机号不能为空');
                return false;
        };

        if (username == '' || username==undefined || username==null){
            alert('用户名不能为空');
            return false;
        };

        if (password == '' || password==undefined || password==null){
                alert('密码不能为空');
                return false;
        };

        if (password_reply == '' || password_reply==undefined || password_reply==null){
                alert('请再次输入密码');
                return false;
        };

        $.ajax({
            url: '/auth/signup/',
            type: 'post',
            data: {'telephone': telephone, 'username': username, 'password': password, 'password_reply': password_reply, 'csrfmiddlewaretoken': token},
            success: function (data) {
                var code = data.code;
                if (code == '200'){
                    alert('注册成功');
                    window.location.replace(current_href);
                }else{
                    var messages = data.message;
                    var error_messages = '';
                    $.each(messages, function (key, message) {
                        error_messages += '<p>'+ message +'</p>'
                    });
                    $signup_error_field.html(error_messages);
                }
            },
            error: function (xhr) {
                console.log(xhr);
            }
        });

        return false;
    });
    
});

