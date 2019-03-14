$(function () {
    var $btn_span = $('#menu-span');
    $btn_span.click(function () {
        var $menu_ul = $('header .nav .menu');
        $menu_ul.fadeToggle(200);
        // $(this).attr('class', 'iconfont icon-close');
        $(this).toggleClass('icon-close', );
    });
});

