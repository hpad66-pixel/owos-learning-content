(function(){
  "use strict";
  var moduleId=document.body.dataset.module||"";
  var key="dga001:"+moduleId+":retrofit";
  var state={opening:false,artifact:false,applied:false};
  try{state=Object.assign(state,JSON.parse(localStorage.getItem(key)||"{}"));}catch(error){}
  function save(){localStorage.setItem(key,JSON.stringify(state));paintCompletion();}
  function paintCompletion(){
    var button=document.querySelector("[data-complete]");
    if(!button)return;
    var ready=state.opening&&state.artifact&&state.applied;
    button.disabled=!ready;
    var out=document.querySelector("[data-completion-status]");
    if(out)out.textContent=ready?"Opening decision, work product, and applied check are complete. This working lesson is ready for your review.":"Complete the opening decision, save the professional work product, and pass the applied check.";
  }
  document.querySelectorAll("[data-opening-decision] [data-choice]").forEach(function(button){
    button.addEventListener("click",function(){
      var box=button.closest("[data-opening-decision]");
      box.querySelectorAll("[data-choice]").forEach(function(item){item.setAttribute("aria-pressed",item===button?"true":"false");});
      var feedback=box.querySelector("[data-decision-feedback]");
      feedback.innerHTML=button.dataset.feedback||"Decision recorded. Carry your reasoning into the lesson.";
      feedback.classList.add("on");
      state.opening=true;save();
    });
  });
  document.querySelectorAll("form[data-artifact]").forEach(function(form){
    var artifactKey=key+":"+form.dataset.artifact;
    try{
      var saved=JSON.parse(localStorage.getItem(artifactKey)||"{}");
      Object.keys(saved).forEach(function(name){var field=form.elements.namedItem(name);if(field)field.value=saved[name];});
    }catch(error){}
    form.addEventListener("submit",function(event){
      event.preventDefault();
      if(!form.reportValidity())return;
      var data={};new FormData(form).forEach(function(value,name){data[name]=String(value);});
      localStorage.setItem(artifactKey,JSON.stringify(data));
      state.artifact=true;save();
      var status=form.querySelector("[data-artifact-status]");if(status)status.textContent="Saved in this browser. Move the reviewed version into the utility's approved repository.";
    });
    var download=form.querySelector("[data-download]");
    if(download)download.addEventListener("click",function(){
      var lines=[form.dataset.exportTitle||"OWOS DATA GOVERNANCE WORK PRODUCT",""];
      new FormData(form).forEach(function(value,name){lines.push(name.replace(/[-_]/g," ").toUpperCase(),String(value),"");});
      lines.push("EVIDENCE BOUNDARY","This instructional draft requires utility approval, current authority, protected evidence handling, and independent review where required.");
      var blob=new Blob([lines.join("\n")],{type:"text/plain"}),a=document.createElement("a");
      a.href=URL.createObjectURL(blob);a.download=(form.dataset.artifact||"work-product")+".txt";a.click();URL.revokeObjectURL(a.href);
    });
  });
  document.querySelectorAll("[data-final-applied-check]").forEach(function(check){
    var button=check.querySelector("[data-check-applied]");
    if(!button)return;
    button.addEventListener("click",function(){
      var required=Array.from(check.querySelectorAll("input[data-correct]"));
      var ok=required.length>0&&required.every(function(input){return input.checked===(input.dataset.correct==="true");});
      var out=check.querySelector("[aria-live]");
      if(ok){out.textContent=check.dataset.pass||"Your recommendation includes the required evidence and boundary.";state.applied=true;save();}
      else{out.textContent=check.dataset.retry||"Review the evidence, authority, limitation, and next action, then try again.";}
    });
  });
  document.querySelectorAll("[data-resilience-console]").forEach(function(consoleEl){
    var scenarios=JSON.parse(consoleEl.querySelector('script[type="application/json"]').textContent),out=consoleEl.querySelector("[data-console-output]"),path=consoleEl.querySelector("[data-control-path]");
    function paint(index,button){var s=scenarios[index];consoleEl.querySelectorAll("[data-scenario]").forEach(function(b){b.classList.toggle("on",b===button);});out.innerHTML="<strong>"+s.verdict+"</strong>"+s.explanation;path.innerHTML=s.path.map(function(step){return '<article class="'+step.state+'"><b>'+step.label+"</b><span>"+step.detail+"</span></article>";}).join("");}
    consoleEl.querySelectorAll("[data-scenario]").forEach(function(button){button.addEventListener("click",function(){paint(+button.dataset.scenario,button);});});paint(0,consoleEl.querySelector("[data-scenario]"));
  });
  document.querySelectorAll("[data-rights-console]").forEach(function(consoleEl){
    var scenarios=JSON.parse(consoleEl.querySelector('script[type="application/json"]').textContent),out=consoleEl.querySelector("[data-console-output]"),board=consoleEl.querySelector("[data-rights-board]");
    function paint(index,button){var s=scenarios[index];consoleEl.querySelectorAll("[data-scenario]").forEach(function(b){b.classList.toggle("on",b===button);});out.innerHTML="<strong>"+s.decision+"</strong>"+s.reason;board.innerHTML=s.tests.map(function(test){return '<article class="'+(test.pass?"":"alert")+'"><b>'+test.label+"</b><span>"+test.result+"</span></article>";}).join("");}
    consoleEl.querySelectorAll("[data-scenario]").forEach(function(button){button.addEventListener("click",function(){paint(+button.dataset.scenario,button);});});paint(0,consoleEl.querySelector("[data-scenario]"));
  });
  document.querySelectorAll("[data-lifecycle-console]").forEach(function(consoleEl){
    var scenarios=JSON.parse(consoleEl.querySelector('script[type="application/json"]').textContent),out=consoleEl.querySelector("[data-console-output]"),track=consoleEl.querySelector("[data-timeline-track]");
    function paint(index,button){var s=scenarios[index];consoleEl.querySelectorAll("[data-scenario]").forEach(function(b){b.classList.toggle("on",b===button);});out.innerHTML="<strong>"+s.decision+"</strong>"+s.reason;track.innerHTML=s.stages.map(function(stage,i){return '<article class="'+(i===s.active?"active":"")+'"><b>'+stage.label+"</b><small>"+stage.detail+"</small></article>";}).join("");}
    consoleEl.querySelectorAll("[data-scenario]").forEach(function(button){button.addEventListener("click",function(){paint(+button.dataset.scenario,button);});});paint(0,consoleEl.querySelector("[data-scenario]"));
  });
  var lastTrigger=null;
  function setDrawer(name,open,trigger){
    var drawer=document.querySelector('[data-drawer="'+name+'"]'),scrim=document.querySelector(".drawer-scrim");
    if(!drawer)return;
    if(open){lastTrigger=trigger||document.activeElement;drawer.classList.add("open");drawer.setAttribute("aria-hidden","false");scrim.classList.add("open");drawer.querySelector("[data-close-drawer]").focus();}
    else{drawer.classList.remove("open");drawer.setAttribute("aria-hidden","true");if(!document.querySelector(".drawer.open"))scrim.classList.remove("open");if(lastTrigger)lastTrigger.focus();}
  }
  document.querySelectorAll("[data-open-graph]").forEach(function(button){button.addEventListener("click",function(){setDrawer("graph",true,button);});});
  document.querySelectorAll("[data-open-community]").forEach(function(button){button.addEventListener("click",function(){setDrawer("community",true,button);});});
  document.querySelectorAll("[data-close-drawer]").forEach(function(button){button.addEventListener("click",function(){setDrawer(button.closest("[data-drawer]").dataset.drawer,false);});});
  var scrim=document.querySelector(".drawer-scrim");if(scrim)scrim.addEventListener("click",function(){document.querySelectorAll(".drawer.open").forEach(function(drawer){setDrawer(drawer.dataset.drawer,false);});});
  document.addEventListener("keydown",function(event){if(event.key==="Escape")document.querySelectorAll(".drawer.open").forEach(function(drawer){setDrawer(drawer.dataset.drawer,false);});});
  var complete=document.querySelector("[data-complete]");if(complete)complete.addEventListener("click",function(){var out=document.querySelector("[data-completion-status]");if(out)out.textContent="Working completion recorded in this browser. Release and credential events remain disabled.";});
  paintCompletion();
})();
