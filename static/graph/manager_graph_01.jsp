<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>


<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],
          ['헌틀리앤팔머스 크래커 7종',     11],
          ['댄케이크 싱글서브 버터쿠키 18입',      2],
          ['오뗄두스 사브레',  2],
          ['마우나로아 마카다미아', 2],
          ['zott 몬테스낵',    7]
        ]);

        var options = {
          title: '많이 팔린 상품'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="piechart" style="width: 650px; height: 400px;"></div>
  </body>
</html>