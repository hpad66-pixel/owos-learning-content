(function(){
  "use strict";

  var lastTrigger=null;

  function drawer(kind){
    return document.querySelector('[data-drawer="'+kind+'"]');
  }

  function closeDrawer(panel){
    if(!panel)return;
    panel.classList.remove("open");
    panel.setAttribute("aria-hidden","true");
    document.body.classList.remove("drawer-open");
    if(lastTrigger)lastTrigger.focus();
  }

  function openDrawer(kind,trigger){
    var panel=drawer(kind);
    if(!panel)return;
    document.querySelectorAll("[data-drawer].open").forEach(function(other){
      other.classList.remove("open");
      other.setAttribute("aria-hidden","true");
    });
    lastTrigger=trigger;
    panel.classList.add("open");
    panel.setAttribute("aria-hidden","false");
    document.body.classList.add("drawer-open");
    var close=panel.querySelector("[data-close-drawer]");
    if(close)close.focus();
  }

  function requirementComplete(value){
    var target=document.querySelector('[data-required="'+value+'"]');
    if(!target)return false;
    if(value==="opening-decision")return true;
    if(value==="applied-interaction"){
      if(target.querySelector(".exdone.on"))return true;
      var run=target.querySelector("[data-run]");
      return !!(run&&run.disabled);
    }
    if(value==="work-product"){
      var textareas=target.querySelectorAll("textarea");
      if(textareas.length)return Array.prototype.every.call(textareas,function(field){return field.value.trim().length>0;});
      var rows=target.querySelectorAll(".at-item");
      return rows.length>0&&Array.prototype.every.call(rows,function(row){return row.getAttribute("data-state")==="3";});
    }
    if(value==="final-check")return !!target.querySelector(".ac-fb.on.ok");
    return false;
  }

  function updateCompletion(){
    var values=["opening-decision","applied-interaction","work-product","final-check"];
    var all=true;
    values.forEach(function(value){
      var done=requirementComplete(value);
      all=all&&done;
      var row=document.querySelector('[data-requirement="'+value+'"]');
      if(row)row.classList.toggle("done",done);
    });
    var button=document.querySelector("[data-complete]");
    var status=document.querySelector("[data-completion-status]");
    var nextStatus=all?"All required evidence is complete.":"Complete the required evidence above.";
    if(button&&button.disabled===all)button.disabled=!all;
    if(status&&status.textContent!==nextStatus)status.textContent=nextStatus;
  }

  document.querySelectorAll("[data-open-graph]").forEach(function(button){
    button.addEventListener("click",function(){openDrawer("graph",button);});
  });
  document.querySelectorAll("[data-open-community]").forEach(function(button){
    button.addEventListener("click",function(){openDrawer("community",button);});
  });
  document.querySelectorAll("[data-close-drawer]").forEach(function(button){
    button.addEventListener("click",function(){closeDrawer(button.closest("[data-drawer]"));});
  });
  document.addEventListener("keydown",function(event){
    if(event.key==="Escape")closeDrawer(document.querySelector("[data-drawer].open"));
  });
  document.addEventListener("input",updateCompletion);
  document.addEventListener("click",function(){window.setTimeout(updateCompletion,0);});
  new MutationObserver(updateCompletion).observe(document.body,{subtree:true,childList:true,attributes:true,attributeFilter:["class","data-state","disabled"]});
  updateCompletion();
})();
