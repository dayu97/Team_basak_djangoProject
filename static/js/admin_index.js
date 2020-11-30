
$(function(){  
		
		
		

    	$('.productMG').click(function(){
    	
    		$('.rightPage').attr("src", 'getProductList');
    		
    		
    		$('#piechart').css({	
							
						'display':'none' }); 
						
			$('#curve_chart').css({	
							
						'display':'none' }); 
   
   
    	});	
    	
    	
    	$('.orderMG').click(function(){
    	
    		$('.rightPage').attr("src", 'getOrderlist');
    		
    			
    		$('#piechart').css({	
							
						'display':'none' }); 
						
			$('#curve_chart').css({	
							
						'display':'none' }); 
   
   
    	});	
    	
    	
    	$('.memberMG').click(function(){
    	
    		$('.rightPage').attr("src", 'getMemberList');
    		
    			
    		$('#piechart').css({	
							
						'display':'none' }); 
						
			$('#curve_chart').css({	
							
						'display':'none' }); 
   
   
    	});	
    	
    	    	
    	
    	    	   	  
});