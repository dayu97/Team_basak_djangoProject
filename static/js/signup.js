//-- **************** 【 	유효사항 체크 영역 		】 *****************************

$(function(){


		
//-- **************** 【 	이용약관 유효사항 	】 *****************************
	


					if( $("#agree").is(":checked") == false){

						 $("#agrmessage").text("동의 사항 체크해주세요");

						 $('#agrmessage').show();

					}


//-- **************** 【 	아이디 유효사항 	】 *****************************









            $('#mid').keyup(function(){
                        var idv = $('#mid').val();

                        $.ajax({

                            url:'signup_check?mid='+idv,
                            success:function(data){
                                console.log(data);
                                $('#target').html(data);
                            }
                         });


                        var uid = $("#mid").val( );

                        var regExp = new RegExp(/^[a-z][a-z0-9_]{3,14}$/);


                         if( regExp.test(uid)==false){

                                    $("#idmessage").text("[아이디]는 영소문숫자 1~15글자여야 합니다.");
                                    $('#idmessage').show();
                                }
                         else{
                                    $('#idmessage').text("사용가능함.");
                                    $('#idmessage').show();
                                }

            });






//-- **************** 【 	비밀번호 유효사항 	】 *****************************

            $('#mpw').keyup(function(){
                var pwd = $("#mpw").val( );

                var regExp = new RegExp(/^[a-z0-9]{3,15}$/);


                         if (regExp.test(pwd)==false) {

                             $("#pwmessage").text( "암호는 영소문자8~15자리숫자를 입력해주세요");

                             $('#pwmessage').show();


                            return false;

                             }

                         else{

                              $('#pwmessage').text("사용가능함.");
                              $('#pwmessage').show();


                              }

            });


			 			 
//-- **************** 【 	비밀번호 확인란 유효사항 	】 *****************************
			 

            $('#pwd_con').keyup(function(){

                 if($("#mpw").val() != $("#pwd_con").val()){

                     $("#pwcmessage").text("비밀번호가 다릅니다!");

                     $('#pwcmessage').show();


                     return false;

                 }


				else{

					$('#pwcmessage').text("사용가능함.");
					$('#pwcmessage').show();


						}

            });


//-- **************** 【 	이름 유효사항 	】 *****************************
	

            $('#mname').keyup(function(){
                 var namecheck = $("#mname").val( );

                 var regExp = new RegExp(/^[가-힣]{2,4}$/);

                 if (regExp.test(namecheck)==false) {

                     $("#namemessage").text("이름은 한글 2~4글자 입력해주세요");

                     $('#namemessage').show();


                    return false;

                 }

                 else{

                        $('#namemessage').text("사용가능함.");
                        $('#namemessage').show();


                            }

            });



/* *************  가입 버튼 클릭시 유효사항 체크  *******************    */		
     



			$("#join").click(function(){

					if(signupForm()<=6){

					alert('입력양식을 다시 확인하세요');

					return false;

					}else{
					alert('테스트입니다.');
					return true;

					}
			})


});