  let flag = 1;

  function toggleNav(){
      if (flag === 0){
        document.getElementById("mySidenav").style.width = "150px";
        document.getElementById("main").style.marginLeft = "118px";
        document.getElementById("navtext1").style.display='inline-block';
        document.getElementById("navtext2").style.display='inline-block';
        document.getElementById("navtext3").style.display='inline-block';
        document.getElementById("navtext4").style.display='inline-block';
        document.getElementById("navtext5").style.display='inline-block';
        document.getElementById("navtext6").style.display='inline-block';
        document.getElementById("navtext7").style.display='inline-block';
        flag = 1;
      } else {
        document.getElementById("mySidenav").style.width = "60px";
        document.getElementById("main").style.marginLeft= "60px";
        document.getElementById("navtext1").style.display='none';
        document.getElementById("navtext2").style.display='none';
        document.getElementById("navtext3").style.display='none';
        document.getElementById("navtext4").style.display='none';
        document.getElementById("navtext5").style.display='none';
        document.getElementById("navtext6").style.display='none';
        document.getElementById("navtext7").style.display='none';
        flag = 0;
      }
  }


  $(document).ready( function () {
 
  });