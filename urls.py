from django.urls import path

from basak import views

urlpatterns=[
    #장바구니
    path('',views.main),
    path('cart',views.cart),
    path('delete',views.delete),

    #결제
    path("pay",views.pay),
    path("pay_suc",views.pay_suc),

    path("index", views.index),
    path("basak", views.index),

    path("product_de", views.product_de),
    path("cart_add", views.cart_add),

    path("admin_index", views.admin_index),

    path("insertProduct", views.insertProduct),
    path("saveProduct", views.saveProduct),
    path("getProductList", views.getProductList),
    path("deleteProduct", views.delProduct),
    path("get_Product", views.get_Product),
    path("updateProduct", views.updateProduct),

    path("getOrderlist", views.getOrderlist),
    path("insertOrder", views.insertOrder),
    path("saveOrder", views.saveOrder),
    path("updateOrder", views.updateOrder),
    path("getOrberUp", views.getOrberUp),
    path("deleteOrder", views.deleteOrder),

    path("login", views.login),
    path("loginform", views.loginform),
    path('logout', views.logout),
    path('admincheck', views.loginform_admin),
    path('signup', views.signup),
    path('signup_check', views.signup_check),
    path('insert_member', views.insert_member),
    path('mypage', views.mypage),
    path('mypage_update', views.mypage_update),
    path('mypage_delete', views.mypage_delete),

    path('board', views.boardSelect),
    path('write',views.write),
    path('detail',views.detail),

    path('boardInsert', views.boardInsert),
    path('boardSelect',views.boardSelect),
    path('delete_board',views.delete_board),
    path('select_board',views.select_board),
    path('update_board',views.update_board),
    path('research',views.research),

    path("getMemberList", views.getMemberList),
    path("getMember", views.getMember),
    path("member_update", views.member_update),
    path("saveMember", views.saveMember),
    path("insertMember", views.insertMember),
    path("deleteMember", views.deleteMember),

]