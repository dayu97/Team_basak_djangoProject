
    
    
   
    

$(document).ready(function(){
	$('.up').click(function() {
		var n = $('.up').index(this);
		var num = $(".cnt:eq(" + n + ")").val();
		num = $(".cnt:eq(" + n + ")").val(num * 1 + 1);
		
	});
	$('.down').click(function() {
		var $this = $('.cnt');
		var n = $('.down').index(this);
		var num = $(".cnt:eq(" + n + ")").val();
		num = $(".cnt:eq(" + n + ")").val(num * 1 - 1);
		alert(num + "num 실제 수");
		
	});
});


/*

$('#option_price').val( num * $('.item_price').find('dt').val() );
		alert($('#option_price').val( num * $('.item_price').find('dt').val() ) + "총 가격");
		alert($('.item_price').find('dt').val() + "dt 태그 가격");
		alert(num + "num 실제 수");


$('#option_price).val( num * $('.item_price').find('dt').val() );
		if ($this.val() < 1)
			$this.val(1);




$(function() {
	alert(1);
	$('.up').click(function() {
		var n = $('.up').index(this);
		var num = $(".cnt:eq(" + n + ")").val();
		num = $(".cnt:eq(" + n + ")").val(num * 1 + 1);
		$('.option_price_display_0').val( num * $('.item_price').find('dt').val() );
		alert($('.option_price_display_0').val( num * $('.item_price').find('dt').val() ) + "총 가격");
		alert($('.item_price').find('dt').val() + "dt 태그 가격");
		alert(num + "num 실제 수");
	});
	$('.down').click(function() {
		var $this = $('.cnt');
		var n = $('.down').index(this);
		var num = $(".cnt:eq(" + n + ")").val();
		num = $(".cnt:eq(" + n + ")").val(num * 1 - 1);
		$('.option_price_display_0').val( num * $('.item_price').find('dt').val() );
		if ($this.val() < 1)
			$this.val(1);
	});
	


    
})
*/