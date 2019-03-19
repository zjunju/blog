$(function () {
    var $love_blog_btn = $('#love-blog-btn');
    var blog_pk = $love_blog_btn.attr('data-blog');
    $love_blog_btn.click(function () {
        var self = $(this);
        $.ajax({
            url: '/blogs/love_blog/?blog_pk='+blog_pk,
            type: 'get',
            success: function (data) {
                var code = data.code;
                if (code=='200'){
                    var $span = self.find('span');
                    var text = $span.text();
                    var num = parseInt(text.substring(7)) + 1;
                    var love_num = $('li[title=喜欢数]');
                    $span.text('喜欢这篇博客（'+num+'）');
                    love_num.html('<i class="iconfont icon-xihuan"></i>' + num);
                    alert('点赞成功！');
                }else{
                    alert(data.message);
                }
            },
            error: function (xhr) {
                console.log(xhr);
            }
        })
    });


    // 发布评论
    var $submit_comment = $('#submit-comment');
    $submit_comment.click(function () {
        var $textrea = $submit_comment.siblings('textarea[name=content]');
        var content = $textrea.val();
        if (content.replace(/^\s+|\s+$/g,"") == '' || content.replace(/^\s+|\s+$/g,"") == undefined){
            alert('内容不能为空！')
        }else{
            // data-obj 是获取object_id data-type 是获取 content_type
            var blog_pk = $textrea.attr('data-blogpk');

            var $comment_list = $('.comment-list');
            var token = $textrea.siblings('input[name=csrfmiddlewaretoken]').val();

            $.ajax({
                url: '/comment/',
                type: 'post',
                data: {'blog_pk': blog_pk, 'content': content, 'csrfmiddlewaretoken': token},
                success:function (data) {
                    var code = data.code;
                    var response_data = data.data;
                    if (code == '200'){
                        alert('评论成功');
                        $textrea.val('');
                    }else{
                        alert(data.message);
                    }
                },
                error: function (xhr) {
                    console.log(xhr);
                },
            })
        }
        return false;
    });
    
    // 查看评论的回复
    var $get_reply = $('.show-reply');
    $get_reply.click(function () {
        var comment_pk = $(this).parent().attr('data-comment');
        $.ajax( {
            url: '/comment/get_reply/?root_comment_pk=' + comment_pk,
            type: 'get',
            success: function (data) {
                var code = data.code;
                if (code == '200'){
                    console.log(data.data);
                }else{
                    console.log(data.message);
                }
            },
            error: function (xhr) {
                console.log(xhr)
            },
       });
    });
    
    // 添加回复的表单
    var $reply = $('.reply');
    $reply.click(function () {
        var self = $(this);
        var $each_comment = self.parents('div.each-comment');
        // 获取回复按钮的文本，如果是回复则将reply_form添加进去，否则删除
        var reply_text = self.text();
        if (reply_text == '回复'){
            var username = self.attr('data-username');
            var place_holder = '回复：'.concat(username);
            // 新建一个reply_form
            var $reply_form = $('<div class="reply-form"><form>' +
                '<textarea class="form-control noresize reply-input" placeholder='+place_holder+'></textarea>' +
                '<input type="submit" value="发送" class="btn btn-primary pull-right" data-id="submit-reply" disabled></form></div>');
            $each_comment.append($reply_form);
            // 给textarea触发focus。
            $reply_form.find('textarea').trigger('focus');
            self.text('取消回复');

            // 给发送按钮添加click事件
            var $submit =  $reply_form.find('input[type=submit]');
            $submit.click(function () {
                // 获取回复对象的评论id和回复对象的userpk
                var comment_id = self.attr('data-commenpk');
                var content = $reply_form.find('textarea.reply-input').val();
                console.log(comment_id);
                console.log(content);
                myajax.post({
                    url: '/comment/reply_comment/',
                    data: {'content': content, 'comment_id': comment_id},
                    success: function (data) {
                        var code = data.code;
                        if (code == '200'){
                            console.log('成功');
                        }else{
                            console.log(data.message);
                        }
                    },
                    error:  function (xhr) {
                        console.log(xhr);
                    }
                });
                return false;
            });
        }

        else{
            var $reply_form = $each_comment.find('div.reply-form');
            $reply_form.remove();
            self.text('回复');
        }

        // 添加事件委托，如果textarea有值则按钮可以点，否则不可点。
        $each_comment.delegate('.reply-input', 'propetychange input',function () {
            var val = $('.reply-input').val();
            var $submit = $each_comment.find('input[type=submit]');
            if(val.trim().length > 0){
                $submit.prop('disabled', false);
            }else{
                $submit.prop('disabled', true);
            }
            });
    });
});