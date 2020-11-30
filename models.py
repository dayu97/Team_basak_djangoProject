from django.db import models
import cx_Oracle as ora

# Create your models here.
from django.views.decorators.csrf import csrf_protect

database = 'kosmorpa/test00@192.168.0.38:1521/orcl'

def connections():
    try:
        conn = ora.connect(database)
    except Exception as e:
        msg="예외발생"
        print(msg)
    return conn

#장바구니
def cartlist(mid):
    conn = connections()
    cursor = conn.cursor()
    sql = "select c.pamount pamount" \
          ",p.pprice pprice" \
          ",c.pamount*p.pprice total" \
          ", p.pname" \
          ",p.pid " \
          ",c.cart_id " \
          "from tpcart c, tpproduct p " \
          "where c.pid = p.pid and c.mid = :mid"
    cursor.execute(sql,mid=mid)
    result = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return result;


def deletecart(cart_id):
    conn = connections()
    cursor = conn.cursor()
    for e in cart_id:
        sql = "delete from tpcart where cart_id=:cart_id"
        cursor.execute(sql,cart_id=e)
    cursor.close()
    conn.commit()
    conn.close()

#################################################################
#결제
def sel(cart_id):
    conn = connections()
    cursor = conn.cursor()
    res = []
    for e in cart_id:
        sql_select = "select c.pamount pamount" \
          ",p.pprice pprice" \
          ",c.pamount*p.pprice total" \
          ", p.pname,p.pid " \
          ",c.cart_id " \
          "from tpcart c, tpproduct p " \
          "where c.pid = p.pid and cart_id=:cart_id"
    #sql_select = "select c.pamount pamount, p.pprice pprice, c.pamount*p.pprice total, p.pname, p.pid from tpcart c, tpproduct p where c.pid = p.pid and c.mid = :mid"
        cursor.execute(sql_select,cart_id=e)
        res.append(cursor.fetchone())
    cursor.close()
    conn.close()
    return res

###################################################################################
#상품저장
def uploadProduct(lis):
    conn = connections()
    cursor = conn.cursor()
    sql = 'insert into TPPRODUCT values (seq.nextval, :1, :2, :3, :4, :5, :6)'
    print("*****insertList : ", lis)
    cursor.execute(sql, lis)
    cursor.close()
    conn.commit()
    conn.close()


#상품저장
def uploadOrder(lis):
    conn = connections()
    cursor = conn.cursor()
    sql_insert = 'insert into tporders values (or_seq.nextval, :1, :2, sysdate, :4, :5)'
    print("*****insertList : ", lis)
    cursor.execute(sql_insert, lis)
    cursor.close()
    conn.commit()
    conn.close()

#상품삭제
def deleteProduct(pidList):
    print("******************model.py::pID::",pidList)
    conn = connections()
    cursor = conn.cursor()
    sql = "DELETE FROM TPPRODUCT WHERE pID = :pID"
    for e in pidList :
        cursor.execute(sql,pID=e)
    cursor.close()
    conn.commit()
    conn.close()


#차트
def chart():
    conn = connections()
    cursor = conn.cursor()
    # sql = "SELECT tpproduct.pname, count(tporders.pid) from tpproduct left join tporders on tpproduct.pid=tporders.pid group by tpproduct.pname having count(tporders.pid)>0 "
    sql = "SELECT tpproduct.pname, sum(tporders.oamount) as total from tporders left join tpproduct on tpproduct.pid=tporders.pid group by tpproduct.pname having count(tporders.pid) > 0 order by total desc"
    cursor.execute(sql)
    cntvv = cursor.fetchall()
    cursor.close()
    print("************차트=" ,cntvv)
    conn.close()
    return cntvv


#상품상세
def detailProduct(pID):
    print("******************상품상세",detailProduct)
    conn = connections()
    cursor = conn.cursor()
    sql = "SELECT * FROM TPPRODUCT WHERE pID = :pID"
    cursor.execute(sql,pID=pID)
    cntvv = cursor.fetchone()
    cursor.close()
    print("************상품상세=" ,cntvv)
    conn.close()
    return cntvv

#상품목록
def listProduct():
    conn = connections()
    cursor = conn.cursor()
    sql = "select pID,pTYPE,pNAME,pPRICE,pAMOUNT,pIMAGE1 from tpproduct order by pID asc"
    cursor.execute(sql)
    plist = cursor.fetchall()
    cursor.close()
    conn.close()
    return plist

def listBoard():
    conn = connections()
    cursor = conn.cursor()
    sql = "select bID,bCATEGORY,bTITLE,mID,brdate from tpBOARD order by bID asc"
    cursor.execute(sql)
    blist = cursor.fetchall()
    cursor.close()
    conn.close()
    return blist

#상품목록
def listOrder():
    conn = connections()
    cursor = conn.cursor()
    sql = "select oid, pid, mid, ordate, odeliveryfee, sum(oamount) as tatal from tporders group by oid, pid, mid, ordate, odeliveryfee order by oid asc"
    cursor.execute(sql)
    olist = cursor.fetchall()
    cursor.close()
    conn.close()
    return olist

#상품수정
def upProduc(uplist):
    conn = connections()
    cursor = conn.cursor()
    sql = "UPDATE TPPRODUCT SET pTYPE=:pTYPE, pNAME=:pNAME, pPRICE=:pPRICE, pAMOUNT=:pAMOUNT WHERE pID=:pID "
    cursor.execute(sql, pTYPE=uplist['pTYPE'], pNAME=uplist['pNAME'], pPRICE=uplist['pPRICE'], pAMOUNT=uplist['pAMOUNT'], pID=uplist['pID'])
    cursor.close()
    conn.commit()
    conn.close()


def getLoginchk(**login):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "select count(*),mname,mphone from TPMEMBER where mid = :mid and mpw = :mpw group by mname,mphone"
    cursor.execute(sql, mid=login['mid'], mpw=login['mpw'])
    datas = cursor.fetchall()
    cursor.close()
    conn.close()
    return datas


def add_member(member_list):
    print(member_list)
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "insert into TPMEMBER values(:1,:2,:3,:4,:5,sysdate)"
    cursor.execute(sql,member_list)
    cursor.close()
    conn.commit()
    conn.close()


def idcheck_cnt(mid) :
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "select count(*) from TPMEMBER where mid = :mid"
    cursor.execute(sql, mid=mid)
    cntvv = cursor.fetchone()
    print(cntvv)
    cursor.close()
    conn.close()
    return cntvv

def del_member(mid):
    print("받았어요!",mid)
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "delete from TPMEMBER where mid = :mid"
    cursor.execute(sql, mid=mid)
    cursor.close()
    conn.commit()
    conn.close()

def update_member(**update):
    print("받았어요!",update['mpw'], update['mname'], update['maddress'], update['mphone'])
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "update TPMEMBER set mpw = :mpw, mname = :mname, maddress = :maddress, mphone = :mphone where mid = :mid"
    cursor.execute(sql, mid=update['mid'],mpw=update['mpw'], mname=update['mname'], maddress=update['maddress'], mphone=update['mphone'])
    cursor.close()
    conn.commit()
    conn.close()

def Memberlist():
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql_select = "SELECT * FROM TPMEMBER ORDER BY mID asc"
    cursor.execute(sql_select)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res

#"getMember"
def getMember1(mID):
    conn = ora.connect(database)
    cursor = conn.cursor()
    update_mem = "SELECT * FROM TPMEMBER WHERE mID=:mID"
    cursor.execute(update_mem,mID=mID)
    datas=cursor.fetchone()
    cursor.close()
    conn.close()
    return datas

#"updateMember"
def updateMember(mID,mPW,mNAME,mADDRESS,mPHONE):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql_update = "UPDATE TPMEMBER SET mPW=:mPW,mNAME=:mNAME,mADDRESS=:mADDRESS,mPHONE=:mPHONE WHERE mID=:mID"
    cursor.execute(sql_update,mID=mID,mPW=mPW,mNAME=mNAME,mADDRESS=mADDRESS,mPHONE=mPHONE)
    cursor.close()
    conn.commit()
    conn.close()

#"insertMember"
def inMember(mID,mPW,mNAME,mADDRESS,mPHONE):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql_insert = "INSERT INTO TPMEMBER ( mID,mPW,mNAME,mADDRESS,mPHONE,mRDATE) " \
                 "VALUES (:mID,:mPW,:mNAME,:mADDRESS,:mPHONE,sysdate)"
    cursor.execute(sql_insert, mID=mID, mPW=mPW, mNAME=mNAME, mADDRESS=mADDRESS, mPHONE=mPHONE)
    cursor.close()
    conn.commit()
    conn.close()

#delectMember
def delect(mID):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql_delect = "DELETE FROM TPMEMBER WHERE mID=:mID"
    cursor.execute(sql_delect,mID=mID)
    cursor.close()
    conn.commit()
    conn.close()


#delectOrder
def delete_Order(oID):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "DELETE FROM TPORDERS WHERE oID =:oID"
    for e in oID :
        cursor.execute(sql,oID=e)
    cursor.close()
    conn.commit()
    conn.close()

#"getOrder"
def getOrder(oID):
    conn = ora.connect(database)
    cursor = conn.cursor()
    detail_order = "SELECT * FROM TPORDERS WHERE oID=:oID"
    cursor.execute(detail_order, oID=oID)
    datas = cursor.fetchone()
    cursor.close()
    conn.close()
    return datas

#"updateOrder"
def update_Order(orderlist):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "UPDATE TPORDERS SET pID=:pID, mID=:mID, oDELIVERYFEE=:oDELIVERYFEE, oAMOUNT=:oAMOUNT WHERE oID=:oID"
    cursor.execute(sql,pID=orderlist['pID'], mID=orderlist['mID'], oDELIVERYFEE=orderlist['oDELIVERYFEE'], oAMOUNT=orderlist['oAMOUNT'], oID=orderlist['oID'])
    cursor.close()
    conn.commit()
    conn.close()

#---------------상세 페이지--------------------
# 상세페이지 (이담)
def getProduct(**kwargs) :
    conn = connections()
    cursor = conn.cursor()
    sql = "SELECT * FROM TPPRODUCT WHERE pID = :pID"
    cursor.execute(sql, pID=kwargs['pID'])
    cntvv = cursor.fetchall()
    print('cntvv',cntvv)
    cursor.close()
    conn.close()
    return cntvv


def add_cart(cart_list):
    conn = connections()
    cursor = conn.cursor()
    sql = "insert into TPCART values(SEQ_TPCART.NEXTVAL,(select mid from tpmember where mid= :mid),(select pid from tpproduct where pid= :pid),:3)"
    cursor.execute(sql,cart_list)
    cursor.close()
    conn.commit()
    conn.close()



def ShowAll():
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "select bid, bCATEGORY, bTITLE, bCONTENTS, bRDATE, mid from TPBOARD order by bid"
    cursor.execute(sql)
    query = cursor.fetchall()
    cursor.close()
    conn.close()
    return query

def board_insert(contents):
    print(contents)
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "INSERT INTO TPBOARD (bID, mID, bCATEGORY, bTITLE, bCONTENTS, bRDATE) VALUES (SEQ_TPBOARD.nextval, :1 , :2, :3, :4, sysdate)"
    cursor.execute(sql, contents)
    cursor.close()
    conn.commit()
    conn.close()

def board_delete(bid):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "delete from TPBOARD where bid = :bid"
    cursor.execute(sql, bid=bid)
    cursor.close()
    conn.commit()
    conn.close()

def board_detail(bid):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "select bCATEGORY, mid, bTITLE, bCONTENTS, bRDATE, bid from TPBOARD where bid = :bid"
    cursor.execute(sql, bid=bid)
    query = cursor.fetchone()
    cursor.close()
    conn.close()
    return query

def board_update(bid, category, board_subject, board_content):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "update TPBOARD set bCATEGORY = :category, bTITLE = :board_subject , bCONTENTS= :board_content where bid = :bid "
    cursor.execute(sql, bid=bid, category=category, board_subject=board_subject, board_content=board_content)
    cursor.close()
    conn.commit()
    conn.close()

def board_research(category, select_write, bid):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql = "select bCATEGORY, mid, bTITLE, bCONTENTS, bRDATE, bid from TPBOARD where bCATEGORY=:category and bCONTENTS like '%'|| :select_write ||'%'"
    cursor.execute(sql, category=category, select_write=select_write)
    query = cursor.fetchall()
    cursor.close()
    conn.close()
    return query

