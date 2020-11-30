from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_protect

from basak.models import *

















#장바구니
def cart(request):
    if 'user_mid' in request.session:
        mid = request.session['user_mid']
        list = cartlist(mid)
        return render(request,"basak/cart.html",{'cartList':list,'mid':mid})
    else:
        msg = "장바구니는 로그인 이후 이용 가능합니다"
        return redirect('/basak/login',{'msg':msg})

def delete(request):
    cart_id = request.GET['cart_id']
    cart_id = cart_id.split(',')
    deletecart(cart_id)
    return redirect('/basak/cart')


###################################################################
#결제
def pay_suc(request):
    cart_id = request.GET['cart_id']
    print("카트아이디:",cart_id)
    cart_id = cart_id.split(',')
    deletecart(cart_id)
    return render(request,'basak/pay_suc.html')

def pay(request):
    # select count(*) from address_address
    #mid = request.session['1']
    #mid = 1
    cart_id = request.GET['cart_id']
    cart_id = cart_id.split(',')
    add = sel(cart_id)
    #dicts = {'add': add}
    return  render(request,'basak/pay.html',{'add':add})

#####################################################################################
UPLOAD_DIR= '/myapps/basak/static/img/'


def main(request):
    plist = listProduct()
    return render(request, "basak/index.html", {'plist': plist})


def index(request):
    plist = listProduct()
    return render(request, "basak/index.html", {'plist': plist})


def new_write(request):
    return render(request,'basak/new_write.html')


def admin_index(request):
    piechart=chart()
    return render(request,'basak/admin_index.html',{'piechart':piechart})

@csrf_protect
#상품등록페이지이동
def insertProduct(request):
    return render(request,'basak/insertProduct.html')

@csrf_protect
#상품저장
def saveProduct(request):
    pTYPE = request.POST['pTYPE']
    pAMOUNT = request.POST['pAMOUNT']
    pPRICE = request.POST['pPRICE']
    pNAME = request.POST['pNAME']
    pImages1= request.FILES['pIMAGE1']
    pIMAGE1 = pImages1.name
    pImages2=request.FILES['pIMAGE2']
    pIMAGE2 = pImages2.name

    fp1 = open("%s%s" % (UPLOAD_DIR, pIMAGE1), 'wb')
    for chunk in pImages1.chunks():
        fp1.write(chunk)
    fp1.close()

    fp2 = open("%s%s" % (UPLOAD_DIR, pIMAGE2), 'wb')
    for chunk in pImages2.chunks():
        fp2.write(chunk)
    fp2.close()


    pro_list=list([pTYPE, pNAME, pPRICE, pAMOUNT, pIMAGE1, pIMAGE2])
    uploadProduct(pro_list)
    return redirect('/basak/getProductList')

@csrf_protect
#상품목록
def getProductList(request):
    plist=listProduct()
    print(len(plist))
    page_num=0
    if len(plist)%10==0:
        page_num = int(len(plist) / 10 )
    else:
        page_num = int(len(plist) / 10+1 )
    p_num = []
    for i in range(page_num):
        p_num.append(i+1)
    return render(request,'basak/getProductList.html',{'plist':plist,'page_num':p_num})

#상품삭제
def delProduct(request):
    pID = request.POST.getlist('chkID')
    print("**************체크박스:",pID)
    deleteProduct(pID)
    return redirect('/basak/getProductList')

#상품상세
@csrf_protect
def get_Product(request):
    pID = request.POST.get('chkID')
    print("**************상품아이디:",pID)
    detail=detailProduct(pID)
    return render(request,'basak/getProduct.html',{'detail':detail})

#상품수정
@csrf_protect
def updateProduct(request):
    uplist={}
    pID = request.POST['pID']
    pTYPE = request.POST['pTYPE']
    pAMOUNT = request.POST['pAMOUNT']
    pPRICE = request.POST['pPRICE']
    pNAME = request.POST['pNAME']
    uplist['pID']=pID
    uplist['pTYPE']=pTYPE
    uplist['pAMOUNT']=pAMOUNT
    uplist['pPRICE']=pPRICE
    uplist['pNAME']=pNAME

    print("**********업뎃값: pId ",pID,"pNAME ",pNAME,"pTYPE ",pTYPE,"pPRICE ",pPRICE,"pAMOUNT ",pAMOUNT)
    print("***********uplist:",uplist)
    upProduc(uplist)
    return redirect('/basak/getProductList')


    # pID = request.POST['pID']
    # pTYPE = request.POST['pTYPE']
    # pAMOUNT = request.POST['pAMOUNT']
    # pPRICE = request.POST['pPRICE']
    # pNAME = request.POST['pNAME']
    #
    # pImages1= request.FILES['pIMAGE1']
    # pIMAGE1 = pImages1.name
    # print("******pImages1",pImages1)
    #
    # pImages2=request.FILES['pIMAGE2']
    # pIMAGE2 = pImages2.name
    # print("******pImages2",pImages2)
    #
    # fp = open("%s%s" % (UPLOAD_DIR, pIMAGE1), 'wb')
    # for chunk in pImages1.chunks():
    #     fp.write(chunk)
    # fp.close()
    #
    # pro_list=list([pTYPE, pNAME, pPRICE, pAMOUNT, pIMAGE1, pIMAGE2])
    # upProduc(pro_list,pID)
    # return redirect('/basak/getProductList')

@csrf_protect
#주문목록
def getOrderlist(request):
    olist=listOrder()
    print('*'*10)
    print(olist)
    print(len(olist))
    page_num=0
    if len(olist)%10==0:
        page_num = int(len(olist) / 10 )
    else:
        page_num = int(len(olist) / 10+1 )
    p_num = []
    for i in range(page_num):
        p_num.append(i+1)
    return render(request,'basak/getOrderlist.html',{'olist':olist,'page_num':p_num})

@csrf_protect
#상품등록페이지이동
def insertOrder(request):
    return render(request,'basak/insertOrder.html')

@csrf_protect
#주문저장
def saveOrder(request):
    pID = request.POST['pID']
    mID = request.POST['mID']
    oDELIVERYFEE = int(request.POST['oDELIVERYFEE'])
    oAMOUNT = int(request.POST['oAMOUNT'])

    or_list=list([pID, mID, oDELIVERYFEE, oAMOUNT])
    uploadOrder(or_list)
    return redirect('/basak/getOrderlist')


def login(request):
    return render(request,'basak/login.html')



@csrf_protect
def loginform(request):
    print("login실행!")
    if 'user_mid' in request.session:
        return redirect('/basak')
    if request.method == 'POST':
        user_mid = request.POST['mid']
        user_mpw = request.POST['mpw']
        print('user_mid:',user_mid)
        print('user_mpw:',user_mpw)

        res = getLoginchk(mid=user_mid,mpw=user_mpw)
        if len(res) > 0:
            print('로그인성공')
            request.session['user_mid'] = user_mid
            request.session['user_mname'] = res[0][1]
            return render(request,'basak/login_ok.html')
        else:
            print("로그인실패")
            msg = '아이디나 비밀번호가 잘못되었습니다.'
            return render(request,"basak/login_false.html",{'error': msg})
    return render(request,'basak/login.html')


def logout(request):
        del request.session['user_mid']
        del request.session['user_mname']
        return redirect('/basak')


@csrf_protect
def loginform_admin(request):
    print("login실행!")
    if 'user_mid' in request.session:
        return redirect('/basak')
    if request.method == 'POST':
        user_mid = request.POST['mid']
        user_mpw = request.POST['mpw']

        admin_id = 'admin'
        admin_pwd = 'admin'

        if user_mid in admin_id and user_mpw in admin_pwd:
            print('로그인성공')
            request.session['user_mid'] = admin_id
            request.session['user_mname'] = '바삭'
            return render(request,'basak/admin_login_ok.html')
        else:
            print("로그인실패")
            msg = '아이디나 비밀번호가 잘못되었습니다.'
            return render(request,"basak/login_false.html",{'error': msg})
    return render(request,'basak/login.html')


def logout_admin(request):
    del request.session['user_mid']
    del request.session['user_mname']
    return redirect('/basak')

def signup(request):
    return render(request,'basak/signup.html')

def signup_check(request):
    idv = request.GET['mid']
    idvv = idcheck_cnt(idv)
    print("result",idvv[0])
    msg = ''
    if idvv[0] > 0:
        msg = "아이디가 중복됩니다."
    else:
        msg = "중복되지 않은 아이디입니다."
    return render(request,"basak/signup_check.html",{'msg':msg})





@csrf_protect
def insert_member(request):
    idv = request.POST['mid']
    idvv = idcheck_cnt(idv)
    msg = ''

    members = (request.POST['mid'],
               request.POST['mpw'],
               request.POST['mname'],
               request.POST['maddress'],
               request.POST['mphone'],)
    print("몇개인가요?",len(members))

    if '' in members:
        print("몇개인가요?",len(members))
        insert_msg = "성공이 아니다."
        return render(request, "basak/signup_false.html",{'insert_msg':insert_msg})

    elif idvv[0] > 0:
        insert_msg = "성공이 아니다."
        return render(request, "basak/signup_false.html",{'insert_msg':insert_msg})

    else:
        add_member(members)
        insert_msg = "성공이다."
        print(insert_msg)
        return render(request, "basak/joinsu.html", {'insert_msg': insert_msg})

@csrf_protect
def loginform_admin2(request):
    print("login실행!")
    if 'user_mid' in request.session:
        return redirect('/basak')
    if request.method == 'POST':
        user_mid = request.POST['mid']
        user_mpw = request.POST['mpw']

        admin_id = 'admin'
        admin_pwd = 'admin'

        if user_mid in admin_id and user_mpw in admin_pwd:
            print('로그인성공')
            request.session['user_mid'] = admin_id
            request.session['user_mname'] = '바삭'
            return render(request,'basak/admin_login_ok.html')
        else:
            print("로그인실패")
            msg = '아이디나 비밀번호가 잘못되었습니다.'
            return render(request,"basak/login_false.html",{'error': msg})
    return render(request,'basak/login.html')

@csrf_protect
def mypage(request):

    return render(request,'basak/mypage.html')


@csrf_protect
def mypage_update(request):
    mid = request.POST['mid']
    mpw=request.POST['mpw']
    mname=request.POST['mname']
    maddress=request.POST['maddress']
    mphone=request.POST['mphone']

    my = (request.POST['mid'],request.POST['mpw'],request.POST['mname'],request.POST['maddress'],request.POST['mphone'],)

    if '' in my:
        print("mypage수정 실패")
        print("제발와라이",len(my))

        return render(request,"basak/mypage_false.html")

    else:

        update_member(mid=mid, mpw=mpw, mname=mname, maddress=maddress, mphone=mphone)

        res = getLoginchk(mid=mid, mpw=mpw)
        request.session['user_mname'] = res[0][1]

        print('mypage수정 성공!')
        return redirect('/basak')










@csrf_protect
def mypage_delete(request):
    idv = request.POST['mid']
    del_member(idv)
    del request.session['user_mid']
    del request.session['user_mname']
    return redirect('/basak')


#getMember상세페이지
@csrf_protect
def getMember(request):
    mID = request.GET['mID']
    member = getMember1(mID)
    return render(request,'basak/getMember.html',{'member':member})
#getMember업데이트
@csrf_protect
def member_update(request):
    mID= request.POST['mID']
    mPW = request.POST['mPW']
    mNAME = request.POST['mNAME']
    mADDRESS = request.POST['mADDRESS']
    mPHONE = request.POST['mPHONE']
    print(mID,mPW, mNAME, mADDRESS, mPHONE)
    updateMember(mID,mPW,mNAME,mADDRESS,mPHONE)
    return redirect('/basak/getMemberList')

#getMember쓰기
@csrf_protect
def insertMember(request):
    return render(request,"basak/insertMember.html")

@csrf_protect
def saveMember(request):
    mID=request.POST['mID']
    mPW=request.POST['mPW']
    mNAME=request.POST['mNAME']
    mADDRESS=request.POST['mADDRESS']
    mPHONE=request.POST['mPHONE']
    print(mID,mPW,mNAME,mADDRESS,mPHONE)
    inMember(mID,mPW,mNAME,mADDRESS,mPHONE)
    return redirect('/basak/getMemberList')

#getMember리스트
def getMemberList(request):
        items=Memberlist()
        return render(request, "basak/getMemberList.html", {'items': items})
#getMember삭제
@csrf_protect
def deleteMember(request):
    mID = request.POST['mID']
    delect(mID)
    return redirect('/basak/getMemberList')

#삭제
@csrf_protect
def deleteOrder(request):
    oID = request.POST.getlist('ckoID')
    print("oID*************",oID)
    delete_Order(oID)
    return redirect('/basak/getOrderlist')

#수정
@csrf_protect
def updateOrder(request):
    orderlist={}
    oID = request.POST['oID']
    pID = request.POST['pID']
    mID = request.POST['mID']
    oDELIVERYFEE = request.POST['oDELIVERYFEE']
    oAMOUNT = request.POST['oAMOUNT']
    orderlist['oID']=oID
    orderlist['pID']=pID
    orderlist['mID']=mID
    orderlist['oDELIVERYFEE']=oDELIVERYFEE
    orderlist['oAMOUNT']=oAMOUNT
    print(orderlist)
    update_Order(orderlist)
    return redirect('/basak/getOrderlist')

#주문상세페이지
def getOrberUp(request):
    oID = request.POST['ckoID']
    print("oid****************",oID)
    order = getOrder(oID)
    return render(request,'basak/getOrder.html',{'order':order})


#---------------상세 페이지--------------------
# 상세페이지 (이담)
def product_de(request):
        pID = request.GET['pID']
        print('pID :',pID)
        chk = getProduct(pID=pID)
        request.session['pID'] = pID
        request.session['pTYPE'] = chk[0][1]
        request.session['pNAME'] = chk[0][2]
        request.session['pPRICE'] = chk[0][3]
        request.session['pAMOUNT'] = chk[0][4]
        request.session['pIMAGE'] = chk[0][5]
        request.session['pIMAGE2'] = chk[0][6]
        return render(request, 'basak/product_de.html',{'chk':chk,'pID':chk[0][0],'pTYPE':chk[0][1],
                                                        'pNAME':chk[0][2],'pPRICE':chk[0][3],'pAMOUNT':chk[0][4]
                                                        ,'pIMAGE':chk[0][5],'pIMAGE2':chk[0][6]})



def cart_add(request):
    if 'user_mid' in request.session:
        print("**************  : ", request.session['pID'])
        # print("**************  : ", request.GET['count'])
        # print("++++++++++++++++ : ", int(request.session['pAMOUNT']))
        print("%%%%%%%%%%%%%%%%%% : ", request.session['user_mid'])
        pID = request.GET['pID']
        pAMOUNT = request.GET['pAMOUNT']
        mid = request.session['user_mid']
        cart_list = (mid, pID, pAMOUNT)
        add_cart(cart_list)
        return render(request, 'basak/cart_add.html')
    else:
        print("로그인실패")
        return redirect('/basak/login')






















def boardSelect(request):
    showList = ShowAll()
    return render(request, "basak/board.html", {'showList': showList})

@csrf_protect
def boardInsert(request):
    contents = (request.POST['board_writer'],request.POST['category'], request.POST['board_subject'], request.POST['board_content'])
    board_insert(contents)
    return redirect('/basak/boardSelect')

def delete_board(request):
    bid = request.GET['bid']
    board_delete(bid)
    return redirect('/basak/boardSelect')

def select_board(request):
    bid = request.GET['bid']
    det = board_detail(bid)
    return render(request, "basak/detail.html", {'det': det})

@csrf_protect
def update_board(request):
    bid = request.POST['bid']
    category = request.POST['category']
    board_subject = request.POST['board_subject']
    board_content = request.POST['board_content']
    board_update(bid, category, board_subject, board_content)
    return redirect('/basak/boardSelect')

def research(request):
    bid = request.GET['bid']
    category = request.GET['category']
    select_write = request.GET['select_write']
    print(category, select_write, bid)
    arr = board_research(category, select_write, bid)
    print(arr)
    return render(request, 'basak/board2.html', {'arr': arr})

def write(request):
    return render(request, "basak/insert.html")

def search(request):
    return render(request, 'basak/search.html')


def board(request):
    return render(request, 'basak/board.html')

def detail(request):
    return render(request, 'basak/detail.html')





















