
    $(function(){  
    
    
    	    	
    	var member = $('#tab1');
    	
    	var admin = $('#tab2');
    	
    	var memberFrom = $('.loginFrom');
    	
    	var adminFrom = $('.adminFrom');
    	
    	
    	adminFrom.hide();
    	
    	memberFrom.show();
    	
    	
    	
    	member.click(function(){
    		
    		adminFrom.hide();
        	
        	memberFrom.show();    	    
   
    	});	
    	
    	
    	admin.click(function(){
    		
    		adminFrom.show();
        	
        	memberFrom.hide();
    	    
   
    	});	
    	
    	    	   	  
			    		   
    		

   });	 	    