	  
$(function(){
	
	
	
	/*    마우스 가져다 대고 빼는 이벤트    */
	
	var rollover = $(".rollover");
			
		rollover.mouseover(function() {
				
				var pre = $(this).attr('src') 
					
				 var post = pre.replace('out','over');
					
				$(this).attr('src', post) ;				
				
				$(this).css({	
					
					'opacity' : '0.5'
					
					}); 
				
				
				
				

				 // $(this).find('.cartBt').attr("style", 'visibility:visible');
				
			     
			});			
			
			rollover.mouseout(function() {
				
			     $(this).attr("src", $(this).attr("src").replace("over", "out"));
			   
			     $(this).css({	
						
						'opacity' : '1'	
						
				}); 
			     
			     
			    $(this).find(".cartBt").attr("style", 'visibility:visible');
			     
				
			     
			});
			
			
			
			/*    클릭시  오른쪽에 div 뜨는 이벤트   */
			
		 
			rollover.click(function(){
				
		
					 $('#rightGroup').css({	
							
						'display':'block' }); 
					 
					 
					 $('.cartPop').click(function(){
						 
						 $('#rightGroup').css({	
								
								'display':'none' }); 
						 
							
					
							
						}); 
					 
			}); 
			
			
}); 

		
	

