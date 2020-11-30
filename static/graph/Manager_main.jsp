<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<style>
body{margin:0px;
	}
	
a{
	color:black; 
	text-decoration:none;
	}
h1{font-size:60px;
	text-align:center;
	border-bottom:1px solid gray;
	margin:0px;
	padding:30px
}
ul{font-size:20px;
	border-right:1px solid gray;
	width:140px;
	margin:0px;
	padding:20px;
	padding-left:53px;
}
#grid{
	display:grid;
	grid-template-columns:250px 1fr;
}
.graph{
            
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            height: 30%;
  
        }
.grade{
            
            display: flex;
            align-items: center;
            justify-content: center;
            width: 80%;
            height: 30%;
			 margin-left:100px;
			 margin-top:20px;

  
        }
#article{padding:10px;}
</style>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<!--<string>은 굵은긁씨를 뜻한다. 
					<u>는 밑줄을 뜻한다.-->  

<input type="button" value="메인화면으로 돌아가기" style="float: right;">
<h1><a href="index.html">Title</a></h1>
<div id="grid">
<ul>
	<li><a href="daily.html">1.매출통계</a></li>
	<li><a href="study.html" style="color:red; text-decoration:underLine">2.상품관리</a></li>
	<li><a href="study.html" style="color:red; text-decoration:underLine">3.회원관리</a></li>
</ul>
	<!--ol = Ordered List
	   1.list 형태로 만들어준다.
	   자동적으로 숫자를 붙여주기 때문에 좋다.
		-->
	<!--<ol>
		<li>test</li>
		<li>daily</li>
		<li>study</li>
		<li>picture</li>
	</ol>-->
	<div id="article">
		<H2><STRONG>당신의 매출을 확인해보세요 </STRONG></H2><BR>
		<hr/>


		<div class="graph">
			<div class="graph_01">
				<%@ include file='manager_graph_01.jsp' %>
			</div>
			<div class="graph_03">
				<%@ include file='manger_graph_03.jsp' %>
			</div>
		</div>
					

		<div class="grade">			
			<div style="background-color: #FFFF; border: 2px solid #FFFF; margin-right:200px">				
					<table border=1 style="width: 350px;">
					<th colspan="3">많이 팔린 과자</th>
					<tr>
					<tr><th>순위</th><th>제품명</th><th>매출량</th></tr>
					<tr><td>1</td><td>1</td><td>1</td></tr>
					<tr><td>1</td><td>1</td><td>1</td></tr>
					<tr><td>1</td><td>1</td><td>1</td>
					</tr>
					</table>

			</div>
			<div style="background-color: #FFFF; border: 2px solid #FFFF;">				
					<table border=1 style="width: 350px;">
					<th colspan="3">많이 팔린 과자</th>
					<tr>
					<tr><th>순위</th><th>제품명</th><th>매출량</th></tr>
					<tr><td>1</td><td>1</td><td>1</td></tr>
					<tr><td>1</td><td>1</td><td>1</td></tr>
					<tr><td>1</td><td>1</td><td>1</td>
					</tr>
					</table>

			</div>
		</div>
	</div>
</div>
</body>
</html>