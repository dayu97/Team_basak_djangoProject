
/*
$(function() {

	$("#btn_payment").click(function(){
		checkForm()
	});

});
	*/


$(function() {

	$("#oname").val("김다유" );
	$("#ophone2_2").val("1234" );
	$("#ophone2_3").val("5648" );
	$("#oemail1").val("dayu97" );


});


function checkForm(){


    var getCheck= RegExp(/^[a-zA-Z0-9]{4,12}$/);
    var getName= RegExp(/^[가-힣]+$/);



	var addr1 =  $("#addr1").val( );
	var addr2 =  $("#addr2").val( );
	var raddr1 =  $("#rec_addr1").val( );
	var raddr2 =  $("#rec_addr2").val( );
	var oname = $("#oname").val( );
	var rname = $("#rname").val( );
	var nameRegExp = /^[가-힣]{2,4}$/;


//===========================주=문=자===========================

	if(oname==""){
		alert("[주문하시는 분] 이름을 입력해주세요")
		$("#oname").focus();
		return false;

	}


     if (!nameRegExp.test(oname)) {
            alert("이름이 올바르지 않습니다.");
			$("#oname").focus();
            return false;
      }



	if(addr1==""){
		alert("[주문하시는 분] 기본 주소를 입력해주세요")
		$("#addr1").focus();
		return false;

	}

		if(addr2==""){
		alert("[주문하시는 분] 상세 주소를 입력해주세요")
		$("#addr2").focus();
		return false;

	}





//===========================수=취=인===========================

	if(rname==""){
		alert("[받는 분] 이름을 입력해주세요")
		$("#rname").focus();
		return false;

	}


     if (!nameRegExp.test(rname)) {
            alert("이름이 올바르지 않습니다.");
			$("#rname").focus();
            return false;
      }


	if(raddr1==""){
		alert("[받는 분] 기본 주소를 입력해주세요")
		$("#rec_addr1").focus();
		return false;

	}


	if(raddr2==""){
		alert("[받는 분] 상세 주소를 입력해주세요")
		$("#rec_addr2").focus();
		return false;

	}




//==========================================구=매=진=행==========================================
	if( $("#chk_purchase:checked").length==0 ){
		alert("구매 진행에 동의해주세요");
		return false;
	}

        var cart_id = "";
		$("[id^=cartlist]").each(function()
		{
			cart_id = cart_id + ',' + $(this).val()
		})
		    cart_id = cart_id.substr(1,)
			$.ajax({
				type : 'GET',
				url : "pay_suc?cart_id=" + cart_id,
				success : function(){

					location.href="pay_suc";
				},
				error : function(){
					alert("에러");
				}
			});


//        var cart_id = "";
//		$("[id^=cartlist]").each(function()
//		{
//			cart_id = cart_id + ',' + $(this).val()
//		})
//		    cart_id = cart_id.substr(1,)
//			$.ajax({
//				type : 'GET',
//				url : "insertOrder?cart_id=" + cart_id,
//				success : function(){
//					alert(cart_id)
//					alert("선택 항목이 삭제되었습니다!!")
//
//					location.href="pay_suc";
//				},
//				error : function(){
//					alert("에러");
//				}
//			});
	document.frm_order_act.submit();
}



//==========================================우===편===번===호==========================================


function execPostCode() {

	 new daum.Postcode({

           oncomplete: function(data) {

               // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

               // 도로명 주소의 노출 규칙에 따라 주소를 조합한다.
               // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
               var fullRoadAddr = data.roadAddress; // 도로명 주소 변수
               var extraRoadAddr = ''; // 도로명 조합형 주소 변수

               // 법정동명이 있을 경우 추가한다. (법정리는 제외)
               // 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
               if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
                   extraRoadAddr += data.bname;
               }
               // 건물명이 있고, 공동주택일 경우 추가한다.
               if(data.buildingName !== '' && data.apartment === 'Y'){
                  extraRoadAddr += (extraRoadAddr !== '' ? ', ' + data.buildingName : data.buildingName);
               }
               // 도로명, 지번 조합형 주소가 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
               if(extraRoadAddr !== ''){
                   extraRoadAddr = ' (' + extraRoadAddr + ')';
               }
               // 도로명, 지번 주소의 유무에 따라 해당 조합형 주소를 추가한다.
               if(fullRoadAddr !== ''){
                   fullRoadAddr += extraRoadAddr;
               }

               // 우편번호와 주소 정보를 해당 필드에 넣는다.

               document.getElementById('zipcode').value = data.zonecode; //5자리 새우편번호 사용
               document.getElementById('addr1').value = fullRoadAddr;
               document.getElementById('addr2').focus();

               console.log(data);

           }

       }).open();

};


function rec_execPostCode() {

	 new daum.Postcode({

           oncomplete: function(data) {

               // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

               // 도로명 주소의 노출 규칙에 따라 주소를 조합한다.
               // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
               var fullRoadAddr = data.roadAddress; // 도로명 주소 변수
               var extraRoadAddr = ''; // 도로명 조합형 주소 변수

               // 법정동명이 있을 경우 추가한다. (법정리는 제외)
               // 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
               if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
                   extraRoadAddr += data.bname;
               }
               // 건물명이 있고, 공동주택일 경우 추가한다.
               if(data.buildingName !== '' && data.apartment === 'Y'){
                  extraRoadAddr += (extraRoadAddr !== '' ? ', ' + data.buildingName : data.buildingName);
               }
               // 도로명, 지번 조합형 주소가 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
               if(extraRoadAddr !== ''){
                   extraRoadAddr = ' (' + extraRoadAddr + ')';
               }
               // 도로명, 지번 주소의 유무에 따라 해당 조합형 주소를 추가한다.
               if(fullRoadAddr !== ''){
                   fullRoadAddr += extraRoadAddr;
               }

               // 우편번호와 주소 정보를 해당 필드에 넣는다.

               document.getElementById('rec_zipcode').value = data.zonecode; //5자리 새우편번호 사용
               document.getElementById('rec_addr1').value = fullRoadAddr;
               document.getElementById('rec_addr2').focus();

               console.log(data);

           }

       }).open();

};





//=====================주=문=자===정=보=와===동=일=====================

$(function(){
    $('#sameaddr0').click(function(){
      var same = this.checked;
//      $('#oname').val(same ? $('#rname').val():'');
//      $('#zipcode').val(same ? $('#rec_zipcode').val():'');
//      $('#addr1').val(same ? $('#rec_addr1').val():'');
//      $('#addr2').val(same ? $('#rec_addr2').val():'');
//      $('#ophone2_1').val(same ? $('#rphone2_1').val():'');
//      $('#ophone2_2').val(same ? $('#rphone2_2').val():'');

      $('#rname').val(same ? $('#oname').val():'');
      $('#rec_zipcode').val(same ? $('#zipcode').val():'');
      $('#rec_addr1').val(same ? $('#addr1').val():'');
      $('#rec_addr2').val(same ? $('#addr2').val():'');
      $('#rphone2_1').val(same ? $('#ophone2_1').val():'');
      $('#rphone2_2').val(same ? $('#ophone2_2').val():'');
      $('#rphone2_3').val(same ? $('#ophone2_3').val():'');

    });
  });



//=====================새=로=운==주=소=====================

$(function(){
	 $('#sameaddr1').click(function(){
	      var same = this.checked;

	      $('#rname').val('');
	      $('#rec_zipcode').val('');
	      $('#rec_addr1').val('');
	      $('#rec_addr2').val('');
	      $('#rphone2_2').val('');
	      $('#rphone2_3').val('');

	 });
 });
