
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
--�⺻ ���������� insert��



INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (1, '��Ű', '��Ʋ�����ȸӽ� ũ��Ŀ 7��', 3000, 100,'product_out_1.png', 'product_1_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (2, '��Ű', '�ٳ뼥 ���� ���̽� �ҿ� 6��', 1500, 100,'product_out_2.png', 'product_2_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (3, '��Ű', 'ī�����̺���� ���� ũ��Ŀ 4��', 1790, 150,'product_out_3.png', 'product_3_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (4, '����', '�������� �Ͽ콺 �������� 6�� ', 2500, 150,'product_out_4.png', 'product_4_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (5, '��Ű', '������ũ �̱ۼ��� ������Ű 18��', 8100, 200,'product_out_5.png', 'product_5_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (6, '��Ű', '������ ������ ũ���䵧��', 4900, 200,'product_out_6.png', 'product_6_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (7, '��Ű', '�����ް� Ȩī�� ���� ', 3790, 100,'product_out_7.png', 'product_7_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (8, '�ø���', 'ũ��� �׷����', 10000, 100,'product_out_8.png', 'product_8_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (9, '��Ű', '�ö��Ϲ� ����� ��Ʈ��', 13000, 150,'product_out_9.png', 'product_9_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (10, '��Ű', '�����ν� ��극', 5000, 150,'product_out_10.png', 'product_10_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (11, '��Ű', '����ó ���� ���� ��Ĩ', 2000, 200,'product_out_11.png', 'product_11_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (12, '��Ű', '�����Ű �縣�� �ӷ���Ű', 6500, 200,'product_out_12.png', 'product_12_detail.jpg');

INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (13, '��Ű', '��޸�Ǯ�� ������ ������Ű', 4000, 100,'product_out_13.png', 'product_13_detail.jpg');


INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (14, '�߰���', '���쳪�ξ� ��ī�ٹ̾�', 3000, 100,'product_out_14.png', 'product_14_detail.jpg');


INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (15, '��Ű', 'zott ���׽���', 7900, 150,'product_out_15.png', 'product_15_detail.jpg');


INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (16, '����', '���߷� ���̽� ���ϰ���Ĩ', 2900, 150,'product_out_16.png', 'product_16_detail.jpg');


INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (17, '����', '���ī�ÿ� ����Ʈ����� ����Ĩ', 5950, 200,'product_out_17.png', 'product_17_detail.jpg');


INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (18, '���ݷ�', '������ �ٻ� ������Ʈ', 100000000, 100,'product_out_18.png', 'product_18_detail.jpg');


INSERT INTO TPPRODUCT
  (PID, PTYPE, PNAME, PPRICE, PAMOUNT, PIMAGE1, PIMAGE2)
VALUES
  (19, '���ݷ�', '�ٻ�', 15000, 10, 'product_out_19.png', 'product_19_detail.jpg');




INSERT INTO TPBOARD
  (bID, mID, bCATEGORY, bTITLE, bCONTENTS, bRDATE)
VALUES
  (SEQ_TPBOARD.nextval, 'sho120', 'ȸ������', 'Ÿ��ƲŸ��Ʋ', '������������', '');

INSERT INTO TPBOARD
  (bID, mID, bCATEGORY, bTITLE, bCONTENTS, bRDATE)
VALUES
  (SEQ_TPBOARD.nextval, 'sho120', 'ȸ������', 'Ÿ��ƲŸ��Ʋ', '������������', '');

INSERT INTO TPBOARD
  (bID, mID, bCATEGORY, bTITLE, bCONTENTS, bRDATE)
VALUES
  (SEQ_TPBOARD.nextval, 'sho120', 'ȸ������', 'Ÿ��ƲŸ��Ʋ', '������������', '');
  
INSERT INTO TPBOARD
  (bID, mID, bCATEGORY, bTITLE, bCONTENTS, bRDATE)
VALUES
  (SEQ_TPBOARD.nextval, 'sho120', 'ȸ������', 'Ÿ��ƲŸ��Ʋ', '������������', '');

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

select * from TPBOARD where bCATEGORY='ȸ������' and   bCONTENTS like '%����%'

select * from TPBOARD where bid = 130 

select bCATEGORY, bTITLE, bCONTENTS from TPBOARD where bid = 131

update TPBOARD set bCATEGORY = bCATEGORY, bTITLE = bTITLE , bCONTENTS= bCONTENTS where bid = bid

select bCATEGORY, mid, bTITLE, bCONTENTS, bRDATE, bid from TPBOARD where bCONTENTS like '%weq%'


select * from TPBOARD

select bCATEGORY, mid, bTITLE, bCONTENTS, bRDATE from TPBOARD where bid = 131