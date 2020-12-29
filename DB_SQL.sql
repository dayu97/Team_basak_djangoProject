
CREATE TABLE TPMEMBER(
    mID VARCHAR2(500) PRIMARY KEY,
    mPW VARCHAR2(15),
    mNAME VARCHAR2(100) ,
    mADDRESS VARCHAR2(500) ,
    mPHONE VARCHAR2(300) ,
    mRDATE DATE DEFAULT SYSDATE
);


CREATE TABLE TPPRODUCT(
    pID NUMBER(4) PRIMARY KEY,
    pTYPE VARCHAR2(30) ,
    pNAME VARCHAR2(100),
    pPRICE NUMBER(20),
    pAMOUNT NUMBER(20),
    pImage1 BLOB,
    pImage2 BLOB

);

CREATE TABLE TPORDERS(
    oID NUMBER(10) PRIMARY KEY,
    pID NUMBER(4)  REFERENCES TPPRODUCT(pID) ,
    mID VARCHAR2(500) REFERENCES TPMEMBER(mID),
    oRDATE DATE DEFAULT SYSDATE,
    odeliveryfee  NUMBER(20),
    OAMOUNT NUMBER(20)
);


CREATE TABLE tpcart(
cart_id NUMBER NOT NULL PRIMARY KEY,
mID VARCHAR2(500) REFERENCES TPMEMBER(mID),
pID NUMBER(4)  REFERENCES TPPRODUCT(pID),
pAMOUNT NUMBER(20) DEFAULT 0
);


CREATE SEQUENCE SEQ
  START WITH 1
  INCREMENT BY 1
  MAXVALUE 10000
  MINVALUE 1
  NOCYCLE;
  
CREATE SEQUENCE OR_SEQ
  START WITH 1
  INCREMENT BY 1
  MAXVALUE 10000
  MINVALUE 1
  NOCYCLE;


CREATE SEQUENCE SEQ_TPCART
    START WITH 10 
    INCREMENT BY 1;


CREATE SEQUENCE SEQ_TPBOARD
    START WITH 1 
    INCREMENT BY 1;


--
--기본 메인페이지 insert문



INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (1, '쿠키', '헌틀리앤팔머스 크래커 7종', 3000, 100,'product_out_1.png', 'product_1_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (2, '쿠키', '다노샵 브라운 라이스 소울 6종', 1500, 100,'product_out_2.png', 'product_2_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (3, '쿠키', '카스테이블워터 영국 크래커 4종', 1790, 150,'product_out_3.png', 'product_3_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (4, '파이', '초코파이 하우스 초코파이 6종 ', 2500, 150,'product_out_4.png', 'product_4_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (5, '쿠키', '댄케이크 싱글서브 버터쿠키 18입', 8100, 200,'product_out_5.png', 'product_5_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (6, '쿠키', '가보뜨 프랑스 크레페덴텔', 4900, 200,'product_out_6.png', 'product_6_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (7, '쿠키', '수제달고나 홈카페 토핑 ', 3790, 100,'product_out_7.png', 'product_7_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (8, '시리얼', '크놀라 그래놀라', 10000, 100,'product_out_8.png', 'product_8_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (9, '쿠키', '플라하반 유기농 오트밀', 13000, 150,'product_out_9.png', 'product_9_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (10, '쿠키', '오뗄두스 사브레', 5000, 150,'product_out_10.png', 'product_10_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (11, '쿠키', '네이처 오다 현미 달칩', 2000, 200,'product_out_11.png', 'product_11_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (12, '쿠키', '쥬니쿠키 사르르 머랭쿠키', 6500, 200,'product_out_12.png', 'product_12_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (13, '쿠키', '라메르풀라르 프랑스 전통쿠키', 4000, 100,'product_out_13.png', 'product_13_detail.jpg');


INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (14, '견과류', '마우나로아 마카다미아', 3000, 100,'product_out_14.png', 'product_14_detail.jpg');


INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (15, '쿠키', 'zott 몬테스낵', 7900, 150,'product_out_15.png', 'product_15_detail.jpg');


INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (16, '스낵', '내추럴 초이스 과일건조칩', 2900, 150,'product_out_16.png', 'product_16_detail.jpg');


INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (17, '스낵', '산니카시오 엑스트라버진 감자칩', 5950, 200,'product_out_17.png', 'product_17_detail.jpg');


INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (18, '초콜렛', '개비스콘 바삭 프로젝트', 100000000, 100,'product_out_18.png', 'product_18_detail.jpg');


INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (19, '초콜렛', '바삭', 15000, 10, 'product_out_19.png', 'product_19_detail.jpg');




INSERT INTO TPBOARD
  (bID, mID, bCATEGORY, bTITLE, bCONTENTS, bRDATE)
VALUES
  (SEQ_TPBOARD.nextval, 'sho120', '회원문의', '타이틀타이틀', '콘텐츠콘텐츠', '');

INSERT INTO TPBOARD
  (bID, mID, bCATEGORY, bTITLE, bCONTENTS, bRDATE)
VALUES
  (SEQ_TPBOARD.nextval, 'sho120', '회원문의', '타이틀타이틀', '콘텐츠콘텐츠', '');

INSERT INTO TPBOARD
  (bID, mID, bCATEGORY, bTITLE, bCONTENTS, bRDATE)
VALUES
  (SEQ_TPBOARD.nextval, 'sho120', '회원문의', '타이틀타이틀', '콘텐츠콘텐츠', '');
  
INSERT INTO TPBOARD
  (bID, mID, bCATEGORY, bTITLE, bCONTENTS, bRDATE)
VALUES
  (SEQ_TPBOARD.nextval, 'sho120', '회원문의', '타이틀타이틀', '콘텐츠콘텐츠', '');

select * from tpboard;

commit


CREATE SEQUENCE SEQ_TPBOARD START WITH 1 INCREMENT BY 1;

commit

INSERT INTO TPBOARD (bID, mID, bCATEGORY, bTITLE, bCONTENTS, bRDATE) VALUES (SEQ_TPBOARD.nextval , 1, 2, 3, 'sdfsad' ,'' )

INSERT INTO TPBOARD (bID, mID, bCATEGORY, bTITLE, bCONTENTS, bRDATE) VALUES (SEQ_TPBOARD.nextval, 'sho120', 1 , 2, 3, '')
  
delete from tpboard;

commit

select bid, bCATEGORY, bTITLE, bCONTENTS, bRDATE from TPBOARD

select bid, bCATEGORY, bTITLE, bCONTENTS, bRDATE from TPBOARD

select p.pNAME, c.pamount, p.pprice, c.pamount*p.pprice, p.pid from tpcart c, tpproduct p where p.pid = c.pid and c.mid = 'sho120'

select bid, bCATEGORY, bTITLE, bCONTENTS, bRDATE from TPBOARD

commit

delete from TPBOARD 

commit

select * from TPBOARD

delete from TPBOARD where bid = 130

select * from TPBOARD

rollback

commit

select * from TPBOARD where bCATEGORY='회원문의' and   bCONTENTS like '%ㅋㅋ%'

select * from TPBOARD where bid = 130 

select bCATEGORY, bTITLE, bCONTENTS from TPBOARD where bid = 131

update TPBOARD set bCATEGORY = bCATEGORY, bTITLE = bTITLE , bCONTENTS= bCONTENTS where bid = bid

select bCATEGORY, mid, bTITLE, bCONTENTS, bRDATE, bid from TPBOARD where bCONTENTS like '%weq%'


select * from TPBOARD

select bCATEGORY, mid, bTITLE, bCONTENTS, bRDATE from TPBOARD where bid = 131
